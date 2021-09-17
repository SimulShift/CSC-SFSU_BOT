import { Client, Intents } from "discord.js"
import 'dotenv/config' // load .env file

(async () => {
  const bot = new Client({ intents: [Intents.FLAGS.GUILDS]})

  await bot.login(process.env.DISCORD_API_TOKEN)
})();
