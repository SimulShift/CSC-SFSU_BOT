const { SlashCommandBuilder } = require('@discordjs/builders')
const { REST } = require('@discordjs/rest')
const { Routes } = require('discord-api-types/v9')
const {
  DISCORD_CLIENT_ID,
  DISCORD_GUILD_ID,
  DISCORD_API_TOKEN,
} = require('../utils/config')

const commands = [
  new SlashCommandBuilder()
    .setName('ClassSearch')
    .setDescription('Searches the SFSU class list for the classes.'),
  new SlashCommandBuilder()
    .setName('ProfessorSearch')
    .setDescription('Searches Rate My Professor for a professor.'),
].map((command) => command.toJSON())

const rest = new REST({ version: '9' }).setToken(token)

;(async () => {
  try {
    await rest.put(Routes.applicationGuildCommands(clientId, guildId), {
      body: commands,
    })

    console.log('Successfully registered application commands.')
  } catch (error) {
    console.error(error)
  }
})()
