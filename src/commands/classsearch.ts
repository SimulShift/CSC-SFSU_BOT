const { SlashCommandBuilder } = require('@discordjs/builders')

module.exports = {
  data: new SlashCommandBuilder()
    .setName('classsearch')
    .setDescription('looks up a class from the sfsu database'),
  async execute(interaction: any) {
    // defer reply to allow the program time to run
    let results: any = {}
    const { spawn } = require('child_process')
    const classSearch = spawn('python', ['./python/ClassSearch.py', 'csc210'])
    classSearch.stdout
      .on('data', (data: any) => {
        return interaction.reply({
            content: `\`\`\`JSON${data}\`\`\``,
            ephemeral: true,
          })
      })
      .catch((err: any) => {
        return interaction.reply({
            content: `${err}`,
            ephemeral: true,
          })
      })


  },
}

export {}
