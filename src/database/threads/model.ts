import mongoose, { Schema, Document } from 'mongoose'

export interface IModel {}

const memberSchema = new Schema({
  _id: Number,
})

const threadSchema = new Schema({
  _id: Number,
  owner: { type: Number, required: true },
  date: { type: Date, required: true, default: Date.now },
})

mongoose.model('memberModel', memberSchema)
mongoose.model('threadModel', threadSchema)

module.exports = { memberModel, threadModel }
