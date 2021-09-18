import { ThreadAutoArchiveDuration } from 'discord-api-types'
import { Message, ThreadChannel } from 'discord.js'
const Discord = require("discord.js")
export class threads {
    message:Message // must provide a message
    name:string // must provide a name
    constructor(message:Message, name?:string | null) {
        this.message = message
        if (name) {
            this.name = name
        }
        else {
            this.name = this.message.author.username
        }
    }

    create() :void {
        // ThreadChannel promise
        this.message.startThread({
            name : this.name, // give it the name
            autoArchiveDuration : ThreadAutoArchiveDuration.OneDay // time until archived
        }).then(() => {
            if (this.message.thread) {
                this.message.thread.ownerId = this.message.author.id
            } else {
                console.log("No thread here boss")
            }
            // return the ThreadChannel
            return this.message.thread
        })
    }

    destroy() :void {
        console.log("Trying to delete")
        this.message.channel.delete()
    }
}