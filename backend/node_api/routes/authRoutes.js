import express from 'express';
import { registerUser, loginUser } from '../controllers/authController.js';

const router = express.Router();

// @route   POST /api/register
// @desc    Register new user
router.post('/register', registerUser);

// @route   POST /api/login
// @desc    Login user
router.post('/login', loginUser);

export default router;
