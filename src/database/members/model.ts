import { model } from 'mongoose'
import { IMemberDocument } from './types'
import MemberSchema from './schema'

export const MemberModel = model<IMemberDocument>('members', MemberSchema)
