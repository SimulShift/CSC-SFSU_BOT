import { Client, Intents } from "discord.js"
import 'dotenv/config' // load .env file

(async () => {
  const BOT = new Client({ intents: [Intents.FLAGS.GUILDS]})

  await BOT.login(process.env.DISCORD_API_TOKEN)
})();
