import { ThreadAutoArchiveDuration } from 'discord-api-types'
import { Emoji, Message, MessageReaction, ReactionEmoji, ThreadChannel, ThreadChannelResolvable } from 'discord.js'
const Discord = require("discord.js")
export class threads {
    message:Message // must provide a message
    name:string // must provide a name
    static currentThread?:ThreadChannel = undefined // gross 
    static currentThreadOwner?:string = undefined // likewise gross
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
                console.log(
                    "Assigned a thread to:\n",
                    "username:\n",
                    this.message.author.username,
                    "\n",
                    "id:\n",
                    this.message.id
                )
                // store the ThreadChannel for now
                threads.currentThread = this.message.thread
                // store the username for now
                threads.currentThreadOwner = this.message.author.username
            }
            // return the ThreadChannel
            return this.message.thread
        })
    }

    destroy() :void {
        if (!this.message.hasThread) {
            this.message.react("😡")
            return
        }
        const requester = this.message.author.username
        if (threads.currentThread) {
            if (requester == threads.currentThreadOwner) {
                console.log(
                    "Accepting the delete request!\n",
                    "Message author id:\n",
                    requester,
                    "Thread owner id:\n",
                    threads.currentThread.ownerId
                )
                console.log(threads.currentThread.toJSON())
                threads.currentThread.delete()
            }
            console.log(
                "Rejecting the request from:\n",
                requester
            )
        }
    }
}