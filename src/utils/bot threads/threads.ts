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
        const messageOwner = this.message.author.id
        const messageUsername = this.message.author.username
        var thread: ThreadChannel | null
        try {
            thread = this.message.thread
        }
        catch {
            this.message.delete()
            // this one in particular is temporary logging, will shove this into dictionary later
            console.log("Rejected impossible thread deletion request from: ",
             messageOwner, "(", messageUsername, ")")
            return
        }
        if (thread) {
            const threadID = thread.id
            const threadOwner = thread.ownerId
            console.log(messageOwner, " requested to delete ", threadID)
            if (threadOwner == messageOwner) {
                console.log("Request accepted")
                thread.delete()
                console.log("Request completed")
            }
        }
    }
}