import { ThreadAutoArchiveDuration } from 'discord-api-types'
import { Message } from 'discord.js'
const Discord = require("discord.js")
export class threads {
    message:Message
    constructor(message:Message) {
        this.message = message
    }

    create() :void {
        console.log("trying to create a message")
        this.message.startThread({
            name : "test",
            autoArchiveDuration : ThreadAutoArchiveDuration.OneDay
        }).then(() => {
            return this.message.thread
        })
    }
}