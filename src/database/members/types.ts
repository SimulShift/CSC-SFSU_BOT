import { Document, Model, ObjectId } from 'mongoose'

export interface IMember {
  UserID: Number
  lastUpdated?: Date
}

export interface IMemberDocument extends IMember, Document {
  setLastUpdated: (this: IMemberDocument) => Promise<void>
}
export interface IMemberModel extends Model<IMemberDocument> {
  findOneOrCreate: ({ id }: { id: Number }) => Promise<IMemberDocument>
}
