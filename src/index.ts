import { DISCORD_API_TOKEN } from './utils/config'
import { Client, Intents, Message } from 'discord.js'
import { commands } from './commands/bot commands/commands';

;(async () => {
  /*Creating a new client */
  const bot = new Client({
    intents: [
      Intents.FLAGS.GUILDS, // Create threads, may
      Intents.FLAGS.GUILD_MESSAGES, // For reading messages and filiting profanity.
      Intents.FLAGS.GUILD_MESSAGE_TYPING, // To set the bot to tpying when its loading data from a website.
      Intents.FLAGS.DIRECT_MESSAGES, // To notifiy a user when a message is deleted with an explination.
    ],
  })

  await bot.login(DISCORD_API_TOKEN).then(() => {
    console.log(bot.user?.username + " has connected to discord")
    bot.on("messageCreate", (msg: Message) :void => {
      // ....
      // gross but gets the job done for the time being (2am, 9/18/2021)
      const receivedArgs: string[] = msg.content.split(" ")
      var builtArgs:string = ""
      msg.content.split("").map((arg:string) => {
        builtArgs += arg
      })

      // the first element is our command
      var receivedCommand: any = receivedArgs[0]
      // log interpreted command
      console.log("interpreted command:\n", receivedCommand as string, "\n")
      // log interpreted args
      console.log("built args:\n", builtArgs, "\n")
      // remove the command
      builtArgs = builtArgs.replace(receivedCommand as string, "")
      // ToDo: bail out if anything sketchy is detected here..
      //...
      //gross ends here

      // run the nullptr flow
      if (receivedCommand == "!nullptr") {
        new commands(msg).nullptr();
      }

      // run the thread command
      else if (receivedCommand == "!thread") {
        new commands(msg).thread(builtArgs)
      }
      else if (receivedCommand == "!destroy") {
        new commands(msg).threadDestroy()
      }
    })
  })
})()
