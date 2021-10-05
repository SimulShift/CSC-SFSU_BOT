import { SlashCommandUserOption } from '@discordjs/builders'
import { CommandInteraction, Permissions } from 'discord.js'

const { SlashCommandBuilder } = require('@discordjs/builders')

module.exports = {
  data: new SlashCommandBuilder()
    .setName('kick')
    .setDescription('Kicks a user from the server.')
    .addUserOption((option: SlashCommandUserOption) =>
      option.setName('target').setDescription('Select a user').setRequired(true)
    ),
  async execute(interaction: CommandInteraction) {
    const callers_permissions: Permissions = <Permissions>(
      interaction.member!.permissions
    )
    const targets_permissions: Permissions = <Permissions>(
      interaction.options.getMember('target')!.permissions
    )
    if (callers_permissions.has(Permissions.FLAGS.KICK_MEMBERS)) {
      if (targets_permissions.has(Permissions.FLAGS.ADMINISTRATOR)) {
        return interaction.reply({
          content: `I wont kick an admin`,
          ephemeral: true,
        })
      } else {
        return interaction.reply({
          content: `https://www.awesomelyluvvie.com/wp-content/uploads/2013/06/KicksRocks.gif`,
          ephemeral: true,
        })
      }
    } else {
        return interaction.reply({
            content: `You do not have permissions to kick members`,
            ephemeral: true,
        })
    }
  },
}

export {}
