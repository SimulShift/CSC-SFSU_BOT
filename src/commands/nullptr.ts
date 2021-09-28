const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('nullptr')
		.setDescription('Produces a nullptr gif as an embedded message response.'),
	async execute(interaction:any) {
		return interaction.reply({ content: `https://i.makeagif.com/media/9-29-2015/YwGqu_.gif`});
	},
};

export {};