const dotenv = require('dotenv')
const path = require('path')
let _envPath

switch (process.env.NODE_ENV) {
  case 'production':
    _envPath = path.resolve(`${__dirname}/../../secrets/.env.production`)
    break
  default:
    _envPath = path.resolve(`${__dirname}/../../secrets/.env.development`)
}
dotenv.config({ path: _envPath })

export const DISCORD_API_TOKEN = process.env.DISCORD_API_TOKEN
export const DISCORD_GUILD_ID = process.env.DISCORD_GUILD_ID
export const DISCORD_CLIENT_ID = process.env.DISCORD_CLIENT_ID
