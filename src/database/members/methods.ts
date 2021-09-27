import { Document } from "mongoose";
import { IMemberDocument } from "./types";

export async function setLastUpdated(this: IMemberDocument): Promise<void> {
  const now = new Date();
  if (!this.lastUpdated || this.lastUpdated < now) {
    this.lastUpdated = now;
    await this.save();
  }
}
