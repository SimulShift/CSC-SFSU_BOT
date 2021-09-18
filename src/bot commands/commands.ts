import { Message } from 'discord.js'
const Discord = require("discord.js")
export class commands {
    content:string = "https://i.makeagif.com/media/9-29-2015/YwGqu_.gif"
    message:Message
    constructor(message:Message) {
        this.message = message
    }

    async nullptr() {
        await this.message.reply(this.content)
    }
}
