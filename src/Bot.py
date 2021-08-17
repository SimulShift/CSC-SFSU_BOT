import discord

from UserProfile import UserProfile

class Bot(discord.Client):
    
    def __init__(self, token, *args, **kwargs):

        # set up stuff
        super().__init__(*args, **kwargs)   # since Bot is a subclass of discord.Client, we gotta call its parents' ctors, ignore args

        self.profiles = {} # empty dictionary

        # start execution
        self.run(token)

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

        channel = self.get_channel(876926597624655923)
        await channel.send('im alive!!')

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        # the channel the message was sent in
        activeChannel = message.channel

        await self.swag(message)
        self.handleVulgarLanguage(message)

        
    async def swag(self, message):
        isNotOurMessage = message.author.id != self.user.id

        # if the incoming message wasnt sent by the bot
        if isNotOurMessage and "swag" in message.content:
            senderID = message.author.id

            if (senderID in self.profiles):
                self.profiles[senderID].strikes += 1        # if we have a profile on this user, edit existing values
            else:
                self.profiles[senderID] = UserProfile()     # else, create a profile for them

            swagEmoji = ":moneybag:"

            for i in range(self.profiles[senderID].strikes):
                swagEmoji *= 2

            await message.channel.send(swagEmoji)

    def handleVulgarLanguage(self, message):
        # do database stuff
        vulgarLanguage = ['shit', 'fuck']
