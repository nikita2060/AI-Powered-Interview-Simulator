import express from "express";
import axios from "axios";
import Interview from "./models/Interview.js";

const router = express.Router();

// Start AI Interview
router.post("/start", async (req, res) => {
  const { userId, question } = req.body;

  try {
    const response = await axios.post("http://127.0.0.1:5000/ai/interview", { question });

    const interview = new Interview({
      userId,
      responses: [{ question, answer: response.data.answer, rating: null }]
    });

    await interview.save();
    res.json(interview);
  } catch (error) {
    res.status(500).json({ msg: "AI Service Unavailable" });
  }
});

export default router;
