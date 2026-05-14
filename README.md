# 🔐 Securify

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-black?style=flat&logo=flask)
![JavaScript](https://img.shields.io/badge/JavaScript-Frontend-yellow?style=flat&logo=javascript)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=flat)

Privacy-First, AI-Assisted Identity Verification with Context-Aware Trust Analysis

---

## 🔗 Live Demo
- **Frontend**: https://securifyy.netlify.app
- **Backend API**: https://securify-production-aa92.up.railway.app

---

## 📌 Features
- AI-based face recognition for agent identity verification
- Dynamic trust score system (increases/decreases based on results)
- Login and registration system
- Real-time verification result with confidence score
- Dashboard with success/fail statistics
- Privacy-first: uploaded images deleted immediately after verification

---

## 🧠 How It Works
1. User logs in at the frontend
2. Enters an Agent ID and uploads a photo
3. Backend compares the photo against registered agent faces
4. Returns verification result with confidence score
5. Agent trust score updates dynamically based on result

---

## 🛠️ Tech Stack
| Layer | Tool |
|---|---|
| Backend | Python, Flask |
| Face Recognition | face_recognition / deepface |
| Frontend | HTML, CSS, JavaScript |
| Backend Hosting | Railway |
| Frontend Hosting | Netlify |

---

## 🚀 Run Locally
```bash
git clone https://github.com/anjalithakurrr/Securify
cd Securify/backend
pip install -r requirements.txt
python app.py
```
Then open `https://securifyy.netlify.app` or `frontend/pages/login.html`

Login: `admin` / `admin123`

---

## 📂 Project Structure
Securify/
├── backend/
│   ├── known_faces/     ← registered agent photos
│   ├── app.py           ← Flask API
│   ├── face_match.py    ← face recognition logic
│   ├── database.json    ← agent data
│   └── requirements.txt
├── frontend/
│   ├── pages/           ← HTML pages
│   ├── CSS/             ← styles
│   └── js/              ← API calls
└── README.md

---

## 👥 Team
- **Anjali Thakur** — Backend, face recognition, verification logic, deployment
- **Navya Aggarwal** — Frontend UI, documentation
