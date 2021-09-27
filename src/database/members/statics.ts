import { IMemberDocument, IMemberModel } from './types'

export async function findOneOrCreate (
  id: Number
): Promise<IMemberDocument> {
  const record = await this.findOne({ id })
  if (record) {
    return record
  } else {
    return this.create({ id })
  }
}
