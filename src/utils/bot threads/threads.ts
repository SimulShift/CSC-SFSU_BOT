import { ThreadAutoArchiveDuration } from 'discord-api-types'
import { Message, ThreadChannel } from 'discord.js'
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
            try {
                if (this.message.thread) {
                    this.message.thread.ownerId = this.message.author.id
                }
            } 
            catch {
                console.log("Failed to set owner id:\n", this.message.author.id,"\n")
            }
            // return the ThreadChannel
            return this.message.thread
        })
    }

    destroy() :void {
        var thread: ThreadChannel | null
        try {
            thread = this.message.thread
        }
        catch {
            this.message.delete()
            return
        }
        if (thread) {
            if (thread.ownerId == this.message.author.id) {
                thread.delete()
            }
        }
    }
}