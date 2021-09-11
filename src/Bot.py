import threading
from discord.enums import MessageType
from dotenv import load_dotenv
from os import getenv
import discord
from discord.ext.commands import Bot
from discord import Intents
from ClassSearch import ClassSearchResultsKeys, advancedSearch, quickSearch
from threading import Thread
intents = Intents.all()
sema = threading.Semaphore
# $pip install "pymongo[srv]"
from pymongo import MongoClient

# $ pip install alt-profanity-check
# $ pip install scikit-learn==0.20.2
import profanity_check

PROF_THRESHOLD = 0.9

# load .env file
load_dotenv()

# load the Database
print("Loading Database")
db_name = getenv("DB_NAME")
db_pw = getenv("DB_PW")
db_url = getenv("DB_URL")
db_client = MongoClient(f"mongodb+srv://{db_name}:{db_pw}@{db_url}")
db = db_client.discord

# load the Bot
print("Loading Bot")
bot = Bot(intents=intents, command_prefix="!")
token = getenv("DISCORD_API_TOKEN")

async def strike(member):
    db.accounts.update_one(
        {"user_id": member.id}, {"$inc": {f"strikes.{member.guild.id}": 1}}, upsert=True
    )


# checks if a message has profanity and removes it if it does. Also sends the member a message explaing why it was removed.
async def check_profanity(message):
    # Dont bother checking DM's
    if not message.guild:
        return

    # calculate the chance that its a profane string
    profanity_probability = profanity_check.predict_prob([message.content])[0]
    if profanity_probability >= PROF_THRESHOLD:
        try:
            # remove the message and explain why
            await message.delete(delay=None)
            await message.author.send(
                content=f"Hey, I removed the following message because I thought it was profane. \n ```{message.content}```"
            )
        except discord.Forbidden as e:
            print(e, "Please grant the bot manage_messages permission")
        except discord.NotFound as e:
            print(e)
        except discord.HTTPException as e:
            print(e)
        except Exception as e:
            print(e)


# adds a member into the accounts database
async def add_member(member):
    db.accounts.insert_one(
        {
            "user_id": member.id,
            "strikes": {
                f"{member.guild.id}": 0,
            },
        }
    )
    print(f"Account created for {member.name}")


# run when bot connects to a server
@bot.event
async def on_ready():
    print(f"{bot.user} has connected to discord")


@bot.event
async def on_member_join(member):
    print(f"{member} sent a message")
    # When a user joins check if he has an account
    account = db.accounts.find_one({"user_id": member})
    # If there is no account create one.
    if account is None:
        add_member(member)


# run on every message
@bot.event
async def on_message(message):
    content = message.content
    author_id = message.author
    print(f"{author_id} sent a message {content}")
    await bot.process_commands(message)
    # Keep the bot from checking its own messages.
    if author_id.bot:
        print(f"{author_id} will not be checked for membership.")
        return

    # Check if this author has an account
    author_id_value = author_id.id
    account = db.accounts.find_one({"user_id": author_id_value})
    # If there is no account create one.
    if account is None:
        print(f"{author_id} is a message author with no account, trying to add...")
        await add_member(author_id)

    # check and handle if the message is profane.
    await check_profanity(message)


# check edited messages
@bot.event
async def on_message_edit(before, after):
    await check_profanity(after)


# runs when bot is disconnected
@bot.event
async def on_disconnect():
    print(f"{bot.user} has been disconnected from discord")


@bot.command()
async def nullptr(ctx):
    await ctx.channel.send("https://i.makeagif.com/media/9-29-2015/YwGqu_.gif")


@bot.command()
async def cs(ctx, arg):
    await classsearch(ctx, arg)


@bot.command()
async def classsearch(ctx, arg):
    await ctx.message.delete(delay=1)
    # Send an inital message here
    message = await ctx.channel.send(f"Searching for {arg} . . .", delete_after=120)

    # Try to search the database.
    try:
        results = await quickSearch(arg)
    except Exception as e:
        print(e)
        await message.edit(content=f"No results for {arg}", delete_after=30)
        return
           
    if len(results) > 15 : 
        text = "*too many results, printing the first 15 \n```" 
    else: text = "```"

    for c in results[:15]:
        # You can modify the lay out of the table by changing the numbers. 
        # The first number limits the size and the second one pads it with 
        # spaces to make a nice table
        text += f'{c["CourseNumber"][:13]:15}'\
                f'{c["Days"][:10]:12}'\
                f'{c["Time"][:20]:22}'\
                f'{c["Professor"][:19]:21}'\
                f'{c["Dates"][:25]:27}'\
                f'{c["Location"]}\n'

    text += "```"
    await message.edit(content=text, delete_after=120)

bot.run(token)