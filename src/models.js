const mongoose = require('mongoose')
const { Schema } = mongoose

const memberSchema = new Schema({
  _id: Number,
})

const threadSchema = new Schema({
  _id: Number,
  owner: Number,
  date: { type: Date, default: Date.now },
})

const guildSchema = new Schema({
  _id: Number,
  members: [memberSchema],
  threads: [threadSchema],
})

module.exports = guildSchema
