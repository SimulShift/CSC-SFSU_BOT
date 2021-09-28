import { config } from './utils/config'
import { Client, Collection, Message } from 'discord.js'
import mongoose from 'mongoose'
import fs from 'fs'

console.log(`Loading Bot`)
const bot = new Client({ intents: config.discord.intents })

console.log(`Loading commands`)
const commands = new Collection()
const commandFiles = fs
  .readdirSync('./commands')
  .filter((file) => file.endsWith('.js') || file.endsWith('.ts'))

for (const file of commandFiles) {
  const command = require(`./commands/${file}`)
  console.log(`  -${command.data.name}`)
  // Set a new item in the Collection
  // With the key as the command name and the value as the exported module
  commands.set(command.data.name, command)
}

bot.on('interactionCreate', async (interaction) => {
  if (!interaction.isCommand()) return
  const commmand: any = commands.get(interaction.commandName)
  if (!commmand) return
  try {
    console.log(`${interaction.user.username} called ${interaction.commandName}`)
    await commmand.execute(interaction)
  } catch (error) {
    await interaction.reply({
      content: 'There was an error while executing this command!',
      ephemeral: true,
    })
  }
})

// Connect to Database
mongoose
  .connect(config.mongo.url, config.mongo.options)
  .then((result) => {
    console.log('Connected to MongoDB')
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
