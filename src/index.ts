import { config } from './utils/config'
import { Client, Message } from 'discord.js'
import mongoose from 'mongoose'

const bot = new Client({ intents: config.discord.intents })

bot.on('interactionCreate', async (interaction) => {
  if (!interaction.isCommand()) return

  if (interaction.commandName === 'nullptr') {
    interaction.reply('https://i.makeagif.com/media/9-29-2015/YwGqu_.gif')
  } else if (interaction.commandName === 'professorsearch') {
    interaction.reply({
      content: `${interaction.commandName} has not been implimented `,
      ephemeral: true,
    })
  } else if (interaction.commandName === 'classsearch') {
    interaction.reply({
      content: `${interaction.commandName} has not been implimented `,
      ephemeral: true,
    })
  }
})

// Connect to Database
mongoose
  .connect(config.mongo.url, config.mongo.options)
  .then((result) => {
    console.log('Connected to MongoDB!')
  })
  .catch((error) => {
    console.error(error)
  })

// Connect to Discord
bot
  .login(config.discord.apiToken)
  .then(() => {
    console.log(bot.user?.username + ' has connected to discord')
  })
  .catch((error) => {
    console.error(error)
  })

