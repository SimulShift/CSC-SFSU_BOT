import { DISCORD_API_TOKEN } from './utils/config'
import { Client, Intents, Message } from 'discord.js'
import { commands } from './bot commands/commands';

;(async () => {
  /*Creating a new client */
  const bot = new Client({
    intents: [
      Intents.FLAGS.GUILDS, // Create threads, may
      Intents.FLAGS.GUILD_MESSAGES, // For reading messages and filiting profanity.
      Intents.FLAGS.GUILD_MESSAGE_TYPING, // To set the bot to tpying when its loading data from a website.
      Intents.FLAGS.DIRECT_MESSAGES, // To notifiy a user when a message is deleted with an explination.
    ],
  })
<<<<<<< HEAD
  await bot.login(DISCORD_API_TOKEN).then(() => {
    console.log(bot.user?.username + " has connected to discord")
    bot.on("message", (msg: Message) => {
      if (msg.content == "!nullptr") {
        new commands(msg).nullptr;
      }
    })
=======
  await bot.login(process.env.DISCORD_API_TOKEN)
  bot.on("messageCreate", (msg: Message) => {
    if (msg.content == "nullptr") {
      new commands(msg).nullptr();
    }
>>>>>>> 07cc602... remove unused import, also remove unused client declaration, also.. actually call the function.. 😅
  })
})()
