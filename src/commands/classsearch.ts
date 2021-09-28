const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('classsearch')
		.setDescription('looks up a class from the sfsu database'),
	async execute(interaction:any) {
		return interaction.reply({ content: `not implemented yet`, ephemeral: true});
	},
};

export {};