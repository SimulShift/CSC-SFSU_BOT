import { DISCORD_API_TOKEN, client } from './utils/config'
import { Client, Intents, Message } from 'discord.js'
import { commands } from './commands/bot commands/commands';

const dotenv = require('dotenv')
const path = require('path')
let _envPath

switch (process.env.NODE_ENV) {
  case 'production':
    _envPath = path.resolve(`${__dirname}/../../secrets/.env.production`)
    break
  default:
    _envPath = path.resolve(`${__dirname}/../../secrets/.env.development`)
}
dotenv.config({ path: _envPath })


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
  
  await client.connect()
  const database = client.db('discord')
  database.listCollections().forEach((thing) => {
    console.log("collection name:\n", thing.name)
  })
  database.collection("accounts").find().forEach((document)=> {
    console.log("document:\n", document)
  })

  await bot.login(DISCORD_API_TOKEN).then(() => {
    console.log(bot.user?.username + " has connected to discord")
    bot.on("message", (msg: Message) => {
      if (msg.content == "!nullptr") {
        new commands(msg).nullptr();
      }
    })
  })
})()
