const { SlashCommandBuilder } = require('@discordjs/builders')

interface Professor {
	"name": String,
	"university": String,
	"department": String,
	"rating": String,
	"rating_count": String,
	"wouldtakeagain": String,
	"difficulty": String,
	}

const contentBuilder = (_data: String): String => {
  const results: [Professor] = JSON.parse(_data.toString())
  if (!results[0]) return 'Nothing found'
  let content: String = 'Here\'s what I found'
  for (let c in results) {
    content += '\n'
    const prof: Professor = results[c]
    content += `${prof.name} ${prof.department} ${prof.rating} ${prof.wouldtakeagain} ${prof.rating_count} ${prof.difficulty}`
  }
  return content
}

module.exports = {
  data: new SlashCommandBuilder()
    .setName('professorsearch')
    .setDescription('looks up a professor from Rate My Professor')
    .addStringOption((option: any) =>
      option
        .setName('professor')
        .setDescription('The professor to search for')
        .setRequired(true)
    ),
  async execute(interaction: any) {
    await interaction.deferReply()
    const professorname = interaction.options.getString('professor')
	console.log(professorname)
    const { spawn } = require('child_process')
    const classSearch = spawn('python', [
      './python/ProfessorSearch.py',
      `${professorname}`,
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
