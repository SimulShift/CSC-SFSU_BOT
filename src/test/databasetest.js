const dotenv = require('dotenv')
const path = require('path')
const { guildModel, userModel, threadModel } = require('../database/members/members.model')
var mongoose = require('mongoose')
var assert = require('assert')


describe('memberModel', () => {
  let member
  beforeEach(() =>{

  })

})

describe('threadModel', () =>{
  let thread

})

describe('guildModel', () =>{
  let guild

})

describe('MongoDB', () => {
  dotenv.config({ path: path.resolve(`../secrets/.env.development`) })
  const _username = process.env.DB_USERNAME
  const _password = process.env.DB_PASSWORD
  const _cluster = process.env.DB_CLUSTER
  const _dbname = process.env.DB_NAME
  beforeEach((done) => {
    mongoose.connect(
      `mongodb+srv://${_username}:${_password}@${_cluster}.mongodb.net/test?retryWrites=true&w=majority`,
      {
        useNewUrlParser: true,
        useUnifiedTopology: true,
      },
      done
    )})

  afterEach((done) => {
    mongoose.connection.close(done)
    mongoose.deleteModel(/.+/)
  })

  after((done) => {
    mongoose.connect(
      `mongodb+srv://${_username}:${_password}@${_cluster}.mongodb.net/test?retryWrites=true&w=majority`,
      {
        useNewUrlParser: true,
        useUnifiedTopology: true,
      },
      done //callback to ensure database connects before moving on the test case
    )
    mongoose.connection.close()
  })

  it('connects', () => {
    assert.equal(mongoose.connection.readyState, 1)
  })

})
