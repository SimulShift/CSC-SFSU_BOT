import { Client, Intents } from 'discord.js'
import 'dotenv/config' // load .env file

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

<<<<<<< Updated upstream
  await bot.login(process.env.DISCORD_API_TOKEN)
=======
  bot.once('ready', () => {
    console.log('Ready!')
  })

  await bot.login(process.env.DISCORD_API_TOKEN).then(() => {
    console.log(bot.user?.username + ' has logged in')
  })
>>>>>>> Stashed changes
})()
