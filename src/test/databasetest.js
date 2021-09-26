const dotenv = require('dotenv')
const path = require('path')
var mongoose = require('mongoose')
var assert = require('assert')

console.log(path.resolve(`../secrets/.env.development`))

describe('MongoDB', () => {
  dotenv.config({ path: path.resolve(`../secrets/.env.development`) })
  const _username = process.env.DB_USERNAME
  const _password = process.env.DB_PASSWORD
  const _cluster = process.env.DB_CLUSTER
  const _dbname = process.env.DB_NAME
  let db
  beforeEach(() => {
    db = mongoose.createConnection(
      `mongodb+srv://${_username}:${_password}@${_cluster}.mongodb.net/${_dbname}?retryWrites=true&w=majority`,
      {
        useNewUrlParser: true,
        useUnifiedTopology: true,
      }
    )
    db.on('error', console.error.bind(console, 'connection error: '))
    db.once('open', () => {})
  })
  afterEach(() => {
    db.close()
    mongoose.deleteModel(/.+/)
  })
  it('connects', () => {
    assert.ok(db)
  })
})
