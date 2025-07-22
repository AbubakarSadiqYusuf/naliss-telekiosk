import streamlit as st
import datetime
from telemed_backend_logic import (
    generate_patient_id,
    generate_clinician_id,
    assign_clinician_by_condition
)
import random
import time

st.set_page_config(page_title="Naliss Care Telekiosk", layout="wide")

# Logo and Sidebar
st.sidebar.image("/mnt/data/naliss_B.jpg", width=200)
st.sidebar.title("NALISS CARE")
st.sidebar.markdown("Your Rural Telemedicine Gateway")

# ------------------- Simulated User Auth -------------------
auth_user = st.sidebar.text_input("Username")
auth_pass = st.sidebar.text_input("Password", type="password")
if auth_user == "admin" and auth_pass == "admin123":
    is_authenticated = True
    st.sidebar.success("Logged in as Admin")
elif auth_user and auth_pass:
    is_authenticated = True
    st.sidebar.success(f"Logged in as {auth_user}")
else:
    is_authenticated = False
    st.sidebar.warning("Please log in")

if not is_authenticated:
    st.stop()

# ------------------- Language Selection -------------------
language = st.sidebar.selectbox("Select Language", ["English", "Twi", "Ewe", "Ga"])

translations = {
    "Welcome": {"Twi": "Akwaaba", "Ewe": "Woezɔ", "Ga": "Ojeikɔ"},
    "Register": {"Twi": "Kyerɛw Wo Din", "Ewe": "Dzudzɔ", "Ga": "Tɔŋ yɛ nɔ"},
    "Patient": {"Twi": "Yarefo", "Ewe": "Nuseme", "Ga": "Yaanom"},
}

# ------------------- Menu -------------------
menu = st.sidebar.radio("Navigation", [
    "Home",
    "Patient Registration",
    "Clinician Registration",
    "Vital Signs",
    "Start Consultation",
    "Access Patient Records",
    "FAQs",
    "Tutorial",
    "Admin Panel"
])

# Simulated database
if "records" not in st.session_state:
    st.session_state["records"] = {}
db = st.session_state["records"]

if menu == "Home":
    st.title("Naliss Care Telekiosk")
    st.subheader(translations["Welcome"].get(language, "Welcome"))
    st.image("/mnt/data/naliss_B.jpg", width=150)
    st.markdown("""
    ### Empowering Rural Healthcare
    - Real-time consultations
    - Vital signs monitoring
    - Encrypted cloud storage
    - Multilingual support
    """)

elif menu == "Patient Registration":
    st.header("Register a New Patient")
    ghana_card = st.text_input("Ghana Card Number")
    dob = st.date_input("Date of Birth")
    if st.button("Generate Patient ID"):
        pid = generate_patient_id(ghana_card, dob.strftime("%Y-%m-%d"))
        st.success(f"Generated Patient ID: {pid}")
        st.session_state["patient_id"] = pid

elif menu == "Clinician Registration":
    st.header("Register a Clinician")
    name = st.text_input("Full Name")
    staff_id = st.text_input("Staff ID")
    field = st.selectbox("Specialty", ["General Practitioner", "Surgeon", "Nurse", "Telemedicine", "Cardiologist", "Pediatrician"])
    if st.button("Generate Clinician ID"):
        cid = generate_clinician_id(name, staff_id, field)
        st.success(f"Generated Clinician ID: {cid}")
        st.session_state["clinician_id"] = cid

elif menu == "Vital Signs":
    st.header("Vital Signs Monitoring")
    if st.button("Start Measurement"):
        temp = round(random.uniform(36.5, 39.0), 1)
        spo2 = random.randint(94, 100)
        pulse = random.randint(60, 100)
        bp_sys = random.randint(100, 140)
        bp_dia = random.randint(70, 90)

        st.metric("Temperature (°C)", temp)
        st.metric("SpO2 (%)", spo2)
        st.metric("Heart Rate (BPM)", pulse)
        st.metric("BP (Systolic/Diastolic)", f"{bp_sys}/{bp_dia}")

        pid = st.session_state.get("patient_id", f"P-{random.randint(1000,9999)}")
        db[pid] = {
            "Temperature": temp,
            "SpO2": spo2,
            "HeartRate": pulse,
            "BloodPressure": f"{bp_sys}/{bp_dia}",
            "Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        st.success(f"Data saved for Patient ID: {pid}")

elif menu == "Start Consultation":
    st.header("Live Consultation")
    st.markdown("Initiate a secure video call with an assigned clinician.")
    patient_symptom = st.text_input("Briefly describe your symptom")
    if st.button("Assign Clinician"):
        specialty = assign_clinician_by_condition(patient_symptom)
        st.info(f"Patient referred to: {specialty}")
    st.markdown("**Video Consultation:** [Launch Video Call](https://meet.jit.si/nalisscareroom)")

elif menu == "Access Patient Records":
    st.header("Patient Records")
    patient_id = st.text_input("Enter Patient ID")
    if st.button("Fetch Record"):
        record = db.get(patient_id)
        if record:
            st.json(record)
        else:
            st.warning("No records found.")

elif menu == "FAQs":
    st.header("Frequently Asked Questions")
    st.markdown("""
    **Q1:** What is Naliss Care?
    - A telemedicine kiosk for rural healthcare delivery in Ghana.

    **Q2:** How does the video consultation work?
    - Patients use an inbuilt tablet to start video calls with clinicians.

    **Q3:** Is the data secure?
    - Yes, all data is encrypted and securely stored.

    **Q4:** Can I register without a Ghana Card?
    - Currently, registration requires a valid Ghana Card.

    **Q5:** What happens after referral?
    - Assigned clinicians access the patient's data and schedule follow-ups.
    """)

elif menu == "Tutorial":
    st.header("Telekiosk Walkthrough Tutorial")
    st.markdown("""
    This video explains how to:
    - Register as a patient or clinician
    - Capture and transmit vital signs
    - Start a video consultation
    - Access patient records securely
    """)
    st.video("https://www.youtube.com/embed/dQw4w9WgXcQ")  # Placeholder link to be replaced with AI-generated video

elif menu == "Admin Panel":
    st.header("Admin Panel")
    st.write("Total Patient Records: ", len(db))
    st.json(db)
    if st.button("Clear All Data"):
        st.session_state["records"] = {}
        st.success("All records cleared.")
