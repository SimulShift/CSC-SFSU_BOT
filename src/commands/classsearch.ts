const { SlashCommandBuilder } = require('@discordjs/builders')

interface Course {
  coursenumber: String
  type: String
  title: String
  units: String
  classnumber: String
  days: String
  time: String
  date: String
  location: String
  instructor: String
  seats: String
  waitlist: String
}

const contentBuilder = (_data: String): String => {
  const results: [Course] = JSON.parse(_data.toString())
  if (!results[0]) return 'Nothing found'
  let content: String = 'Here\'s what I found'
  for (let c in results) {
    content += '\n'
    const course: Course = results[c]
    content += `${course.coursenumber} ${course.instructor} ${course.days} ${course.time}`
  }
  return content
}

module.exports = {
  data: new SlashCommandBuilder()
    .setName('classsearch')
    .setDescription('looks up a class from the sfsu database')
    .addStringOption((option: any) =>
      option
        .setName('coursenumber')
        .setDescription('The Course Number to Search For')
        .setRequired(true)
    ),
  async execute(interaction: any) {
    await interaction.deferReply()
    const coursenumber = interaction.options.getString('coursenumber')
    const { spawn } = require('child_process')
    const classSearch = spawn('python', [
      './python/ClassSearch.py',
      `${coursenumber}`,
    ])

    classSearch.stdout.on('data', (data: string) => {
      return interaction.editReply({
        content: contentBuilder(data),
        ephemeral: true,
      })
    })
  },
}

export {}
