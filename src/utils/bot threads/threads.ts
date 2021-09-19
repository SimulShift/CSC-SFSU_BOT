import { ThreadAutoArchiveDuration } from 'discord-api-types'
import { Message, ThreadChannel, ThreadChannelResolvable } from 'discord.js'
const Discord = require("discord.js")
export class threads {
    message:Message // must provide a message
    name:string // must provide a name
    static thread?:ThreadChannel = undefined
    constructor(message:Message, name?:string | null) {
        this.message = message
        if (name) {
            this.name = name
        }
        else {
            this.name = this.message.author.username
        }
        if(message.guild) {
            console.log("guild is:\n", message.guild)
        }
        console.log("User ID:\n", message.id)
    }

    create() :void {
        // ThreadChannel promise
        this.message.startThread({
            name : this.name, // give it the name
            autoArchiveDuration : ThreadAutoArchiveDuration.OneDay // time until archived
        }).then(() => {
            if (this.message.thread) {
                console.log("Joining thread")
                this.message.thread.join()
                console.log
                (
                    "Assigned a thread to:\n",
                    "username:\n",
                    this.message.author.username,
                    "\n",
                    "id:\n",
                    this.message.id
                )
                // store the ThreadChannel for now
                threads.thread = this.message.thread
            }
            // return the ThreadChannel
            return this.message.thread
        })
    }

    destroy() :void {
        console.log("Trying to delete")
        if (threads.thread) {
            console.log("We have a thread!")
            console.log(threads.thread.toJSON())
            threads.thread.delete()
        }
    }
}