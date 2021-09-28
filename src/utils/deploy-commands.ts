// This is saved on discords servers so only need
const { SlashCommandBuilder } = require('@discordjs/builders')
const { REST } = require('@discordjs/rest')
const { Routes } = require('discord-api-types/v9')
const { config } = require('./config')

console.log(config)
const commands = [
  new SlashCommandBuilder()
    .setName('classsearch')
    .setDescription('Searches the SFSU class list for the classes.'),
  new SlashCommandBuilder()
    .setName('professorsearch')
    .setDescription('Searches Rate My Professor for a professor.'),
  new SlashCommandBuilder()
    .setName('nullptr')
    .setDescription('Produces a nullptr gif as an embedded message response'),
].map((command) => command.toJSON())

const rest = new REST({ version: '9' }).setToken(config.discord.apiToken)

rest
  .put(
    Routes.applicationGuildCommands(
      config.discord.clientID,
      config.discord.guildID,
    ),
    { body: commands }
  )
  .then(() => console.log('Successfully registered application commands.'))
  .catch(console.error)
