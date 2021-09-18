import { ThreadAutoArchiveDuration } from 'discord-api-types'
import { Client, Message, Options, ThreadChannel, ThreadManager, ThreadMember, ThreadMemberFlags, ThreadMemberManager } from 'discord.js'
const Discord = require("discord.js")
export class commands {
    //content:string = "https://i.makeagif.com/media/9-29-2015/YwGqu_.gif"
    message:Message
    bot:Client
    constructor(bot:Client, message:Message) {
        this.message = message
        this.bot = bot
    }

    create() {
        this.message.startThread({
            name : "test",
            autoArchiveDuration : ThreadAutoArchiveDuration.OneDay
        })
    }
}