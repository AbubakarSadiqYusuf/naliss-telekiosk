# Naliss Care Telekiosk

**A smart, modular telemedicine web application for rural healthcare delivery in Ghana.**

## 🌍 Project Description

Naliss Care Telekiosk is a secure, open-source telemedicine station designed for underserved communities. It provides:

- **Real-time remote consultations** via video conferencing
- **Vital sign monitoring** with wearable or simulated devices
- **Patient and clinician registration**
- **Encrypted cloud-based patient record management**
- **Language localization** (Twi, Ewe, Ga, English)
- **An educational tutorial and FAQ**

This project supports Ghana's digital health strategy and aligns with SDG 3: Good Health and Well-being.

---

## 🚀 Features

- 🧑‍⚕️ Clinician & Patient Registration
- 📊 Vital Signs: Temperature, SpO2, Heart Rate, Blood Pressure
- 🎥 Encrypted Video Consultations (Jitsi)
- ☁️ Simulated Cloud Storage (via `session_state`)
- 🌐 Multilingual UI: English, Twi, Ewe, Ga
- 📚 FAQs & AI-Generated Walkthrough Tutorial

---

## 📁 Project Structure

naliss_telekiosk/
├── app.py # Main Streamlit application
├── telemed_backend_logic.py # Backend logic for ID generation & referral
├── naliss_B.jpg # Logo used in sidebar
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## ✅ Requirements

Install dependencies using:

```bash
pip install -r requirements.txt

## Running the App Locally
streamlit run app.py

##Tutorial
Watch the full walkthrough video:

##🛡️ Security & Privacy
All data is stored temporarily in-session (demo).

In production, integrate with a secure cloud database (e.g., Firebase, Supabase).

Authentication is currently basic; use Firebase Auth or similar for real apps.

##🤝 Authors
This solution is part of a final-year Biomedical Engineering project (BMEN416 - University of Ghana).

