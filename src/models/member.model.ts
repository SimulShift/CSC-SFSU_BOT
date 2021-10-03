import { Document, Model, model, Types, Schema, Query } from 'mongoose'

// Typescript Interface
export interface IMember extends Document {
  id: Number
}

// Mongoose Schema
export const MemberSchema = new Schema({
  id: {
    type: Number,
    required: true,
  },
})

// Mongoose Model
const Member = model<IMember>('Member', MemberSchema)

export default Member
