import { Schema } from 'mongoose'
import { findOneOrCreate } from './statics'
import { setLastUpdated } from './methods'

const MemberSchema = new Schema({
  snowflake: { 
    UserID: Number, 
    required: true 
  },
  lastUpdated: {
    type: Date,
    default: new Date(),
  },
})

MemberSchema.statics.findOneOrCreate = findOneOrCreate;

MemberSchema.methods.setLastUpdated = setLastUpdated;

export default MemberSchema
