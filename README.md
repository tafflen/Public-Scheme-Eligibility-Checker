# NOVA - Government Scheme Eligibility Checker

An AI-powered, offline-first app that helps Indian citizens instantly check which government welfare schemes they are eligible for, with voice support and fraud protection built in.

## What This App Does

- Citizens enter basic details (age, gender, income, occupation) once
- The app instantly checks them against a database of central and state government schemes
- Shows clear results: Eligible, Partially Eligible, or Not Eligible, with reasons why
- A voice assistant lets users speak commands like "check my schemes" and hear results out loud
- Works offline for core features, so it's usable even without a stable internet connection

---

## How to Run

### 1. Backend (FastAPI + SQLite)

\`\`\`bash
cd backend

pip install fastapi uvicorn sqlalchemy

uvicorn app:app --reload
\`\`\`

Backend runs at: `http://127.0.0.1:8000`
API docs available at: `http://127.0.0.1:8000/docs`

### 2. Frontend (React)

\`\`\`bash
cd frontend

npm install

npm start
\`\`\`

Frontend runs at: `http://localhost:3001`

Make sure the backend is running before using the app, since the eligibility checker fetches data from it.

---

## Tech Stack

**React**
A JavaScript library for building user interfaces. We used it to build a fast, responsive frontend that works smoothly even on low-end smartphones.

**FastAPI (Python)**
A modern Python framework for building APIs. It's fast, easy to scale, and handles multiple requests efficiently, which is what powers our eligibility-checking logic behind the scenes.

**SQLite**
A lightweight, file-based database that doesn't need a separate server to run. It stores our scheme and user data directly, which is what makes offline-first functionality possible.

**SQLAlchemy**
A Python library that lets our backend talk to the SQLite database using simple Python code instead of writing raw SQL queries.

**Web Speech API**
A browser-based tool that converts speech to text and text to speech. It powers our voice assistant, letting users speak commands and hear responses without typing.

**Rule-Based Eligibility Engine**
Instead of using an unpredictable AI model to decide eligibility, we built transparent rule-based logic (plain if-else conditions comparing user details to scheme criteria) so every decision can be explained and trusted.

---

## Project Structure

\`\`\`
public Scheme/
├── backend/
│   ├── app.py               # FastAPI app entry point
│   ├── database.py          # DB connection setup
│   ├── modals/               # Data models (Scheme, User)
│   ├── routes/               # API endpoints
│   └── services/              # Business logic (eligibility, seeding)
├── frontend/
│   ├── src/
│   │   ├── components/        # React components (Form, Voice Assistant, etc.)
│   │   ├── App.js
│   │   └── App.css
└── README.md
\`\`\`

---

## Notes

- This is a hackathon prototype. Scheme data is manually seeded for demonstration purposes.
- Voice assistant currently uses the browser's built-in speech engine, which requires internet for speech recognition. A fully offline version (using Vosk and Piper) is planned for future development.
