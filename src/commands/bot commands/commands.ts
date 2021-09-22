import { Message } from 'discord.js'
import { threads } from '../../utils/bot threads/threads'

const Discord = require("discord.js")
export class commands {
    message:Message // every command will need a message, we will pass this around
    constructor(message:Message) {
        this.message = message
    }

    async nullptr() {
        // the nullptr gif url
        const content:string = "https://i.makeagif.com/media/9-29-2015/YwGqu_.gif"
        // send the message
        await this.message.reply(content)
    }

    async thread(named:string) {
        // we received a name
        var received = named
        // if our thread name is empty, the bot will crash
        if (received.length == 0) {
            // default name of thread will just be our user name
            received = this.message.author.username
        }
        // create the thread
        await new threads(this.message, received).create()
    }

    async threadDestroy() {
        await new threads(this.message).destroy()
    }
}