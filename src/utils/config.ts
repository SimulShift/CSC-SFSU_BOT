const dotenv = require('dotenv')
const path = require('path')
const mongoose = require('mongoose')

const _envpath = (): string => {
  switch (process.env.NODE_ENV) {
    case 'production':
      return path.resolve(`${__dirname}/../../secrets/.env.production`)
    case 'test':
      return path.resolve(`${__dirname}/../../secrets/.env.test`)
    case 'development':
    default:
      return path.resolve(`${__dirname}/../../secrets/.env.development`)
  }
}

dotenv.config({ path: _envpath() })
const _username = process.env.DB_USERNAME
const _password = process.env.DB_PASSWORD
const _cluster = process.env.DB_CLUSTER
const _dbname = process.env.DB_NAME

mongoose.connect(
  `mongodb+srv://${_username}:${_password}@${_cluster}.mongodb.net/${_dbname}?retryWrites=true&w=majority`,
  {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  }
)
mongoose.connection.on(
  'error',
  console.error.bind(console, 'connection error: ')
)
mongoose.connection.once('open', () =>
  console.log(
    `Connected to mongodb+srv://${_username}@${_cluster}.mongodb.net/${_dbname}`
  )
)

export const db = mongoose.connection
export const DISCORD_API_TOKEN = process.env.DISCORD_API_TOKEN
export const DISCORD_GUILD_ID = process.env.DISCORD_GUILD_ID
export const DISCORD_CLIENT_ID = process.env.DISCORD_CLIENT_ID
