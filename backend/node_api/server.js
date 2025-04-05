import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import connectDB from "./database.js";
import authRoutes from "./routes/authRoutes.js";
import interviewRoutes from "./interviewRoutes.js";

dotenv.config();
const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json());

// Routes
app.use("/api/auth", authRoutes);
app.use("/api/interview", interviewRoutes);

// Connect to MongoDB
connectDB();

// Start Server
app.listen(PORT, () => console.log(`✅ Server running on port ${PORT}`));
