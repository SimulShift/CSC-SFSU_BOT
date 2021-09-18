import { ThreadAutoArchiveDuration } from 'discord-api-types'
import { Message } from 'discord.js'
const Discord = require("discord.js")
export class threads {
    message:Message // must provide a message
    name:string // must provide a name
    constructor(message:Message, name:string) {
        this.message = message
        this.name = name
    }

    create() :void {
        // ThreadChannel promise
        this.message.startThread({
            name : this.name, // give it the name
            autoArchiveDuration : ThreadAutoArchiveDuration.OneDay // time until archived
        }).then(() => {
            // return the ThreadChannel
            return this.message.thread
        })
    }
}