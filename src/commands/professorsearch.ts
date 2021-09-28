const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('professorsearch')
		.setDescription('looks up a professor from rate my professor'),
	async execute(interaction:any) {
		return interaction.reply({ content: `not yet implemented`, ephemeral: true});
	},
};

export {};