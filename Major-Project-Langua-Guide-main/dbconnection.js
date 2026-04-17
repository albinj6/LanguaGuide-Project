const mongoose = require("mongoose");
const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");

const app = express();
const port = 3000;

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// ✅ Connect to MongoDB
const mongoURI = "mongodb+srv://athulpshibu2003:Athul%40mongodb@cluster0.858ol.mongodb.net/Languaguide";
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log("✅ Connected to MongoDB"))
    .catch(err => console.error("❌ MongoDB connection error:", err));

// ✅ User Schema (Stores user details)
const userSchema = new mongoose.Schema({
  name: String,
  email: { type: String, unique: true },
  phone: String,
  dob: String,
  age: Number,
  gender: String,
  city: String,
  state: String,
  country: String,
  educationLevel: String,
});

const User = mongoose.model("User", userSchema, "UserData");

// ✅ Selection Schema (Stores language, level & achievement)
const selectionSchema = new mongoose.Schema({
  userId: mongoose.Schema.Types.ObjectId, // Links to User ID
  email: String, // Store user email
  language: String,
  level: String,
  achievement: String,
});

const Selection = mongoose.model("Selection", selectionSchema, "Selections");

// ✅ 1️⃣ Save User Details (From user.html)
app.post("/submit", async (req, res) => {
    const { name, email, phone, dob, age, gender, city, state, country, educationLevel } = req.body;

    try {
        let user = await User.findOne({ email });

        if (user) {
            return res.status(400).json({ error: "User already exists!" });
        }

        user = new User({ name, email, phone, dob, age, gender, city, state, country, educationLevel });
        await user.save();

        res.status(201).json({ message: "User details saved successfully!" });
    } catch (error) {
        console.error("❌ Error saving user:", error);
        res.status(500).json({ error: "Failed to save user." });
    }
});

// ✅ 2️⃣ Save Language Selection (From page2.html)
app.post("/save-language", async (req, res) => {
    const { email, language } = req.body;

    try {
        const user = await User.findOne({ email });

        if (!user) return res.status(404).json({ error: "User not found!" });

        await Selection.findOneAndUpdate({ email }, { userId: user._id, language }, { upsert: true });

        res.status(201).json({ message: "Language saved successfully!" });
    } catch (error) {
        console.error("❌ Error saving language:", error);
        res.status(500).json({ error: "Failed to save language." });
    }
});

// ✅ 3️⃣ Save Level Selection (From level.html)
app.post("/save-level", async (req, res) => {
    const { email, level } = req.body;

    try {
        const user = await User.findOne({ email });

        if (!user) return res.status(404).json({ error: "User not found!" });

        await Selection.findOneAndUpdate({ email }, { level }, { upsert: true });

        res.status(201).json({ message: "Level saved successfully!" });
    } catch (error) {
        console.error("❌ Error saving level:", error);
        res.status(500).json({ error: "Failed to save level." });
    }
});

// ✅ 4️⃣ Save Achievement Selection (From achieve.html)
app.post("/save-achievement", async (req, res) => {
    const { email, achievement } = req.body;

    try {
        const user = await User.findOne({ email });

        if (!user) return res.status(404).json({ error: "User not found!" });

        await Selection.findOneAndUpdate({ email }, { achievement }, { upsert: true });

        res.status(201).json({ message: "Achievement saved successfully!" });
    } catch (error) {
        console.error("❌ Error saving achievement:", error);
        res.status(500).json({ error: "Failed to save achievement." });
    }
});

// ✅ Start Server
app.listen(port, () => console.log(`🚀 Server running at http://localhost:${port}`));
