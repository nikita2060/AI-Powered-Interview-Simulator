import mongoose from "mongoose";

const InterviewSchema = new mongoose.Schema({
  userId: { type: mongoose.Schema.Types.ObjectId, ref: "User" },
  responses: [{ question: String, answer: String, rating: Number }],
  createdAt: { type: Date, default: Date.now },
});

const Interview = mongoose.model("Interview", InterviewSchema);
export default Interview;
