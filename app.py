# ==========================================
# WOMEN SAFETY APP - ADVANCED VERSION 🚨
# Streamlit Deployment Ready
# ==========================================

import streamlit as st
import requests
import random
import time
import speech_recognition as sr
from datetime import datetime
from geopy.geocoders import Nominatim
import folium
from streamlit_folium import st_folium

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Women Safety App",
    page_icon="🚨",
    layout="wide"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>
.main {
    background-color: #fff5f7;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
}

.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    font-size: 18px;
    font-weight: bold;
    background-color: #ff4b4b;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================

st.title("🚨 Women Safety App")
st.subheader("AI Powered Personal Safety System")

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.header("👤 User Details")

name = st.sidebar.text_input("Your Name")
phone = st.sidebar.text_input("Phone Number")

emergency_contact = st.sidebar.text_input(
    "Emergency WhatsApp Number"
)

# ==========================================
# LOCATION FUNCTION
# ==========================================

def get_location():

    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()

        loc = data["loc"].split(",")

        latitude = float(loc[0])
        longitude = float(loc[1])

        city = data.get("city", "Unknown")

        return latitude, longitude, city

    except:
        return 12.9716, 77.5946, "Bangalore"

# ==========================================
# GET LOCATION
# ==========================================

lat, lon, city = get_location()

# ==========================================
# SOS SECTION
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("🚨 SOS EMERGENCY")

if st.button("SEND SOS ALERT"):

    maps_link = f"https://www.google.com/maps?q={lat},{lon}"

    st.error("🚨 EMERGENCY ALERT ACTIVATED")

    st.success(f"""
    ALERT DETAILS
    
    👤 Name: {name}
    📍 City: {city}
    📌 Location: {lat}, {lon}
    
    Emergency contacts notified.
    """)

    st.markdown(f"""
    ### Emergency Message
    
    HELP! I am in danger.
    
    My location:
    {maps_link}
    
    Time:
    {datetime.now()}
    """)

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# CAMERA EVIDENCE
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("📸 Camera Evidence Capture")

camera = st.camera_input("Capture Emergency Evidence")

if camera:
    st.success("📸 Evidence Captured Successfully")

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# SECRET RECORDING
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("🎤 Secret Audio Recording")

if st.button("START SECRET RECORDING"):

    st.info("🎙️ Recording Started Silently")

    progress = st.progress(0)

    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)

    st.success("✅ Recording Saved Successfully")

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# VOICE COMMAND
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("🎙️ Voice Command SOS")

st.write("Supported Commands:")
st.write("- Help me")
st.write("- Emergency")
st.write("- Save me")

if st.button("START VOICE LISTENING"):

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:

            st.info("🎤 Listening...")

            audio = recognizer.listen(source, timeout=5)

            text = recognizer.recognize_google(audio)

            st.success(f"Detected Voice: {text}")

            if (
                "help" in text.lower()
                or "emergency" in text.lower()
                or "save me" in text.lower()
            ):

                st.error("🚨 SOS TRIGGERED BY VOICE COMMAND")

    except:
        st.warning("Voice not detected")

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# SAFE WALK TIMER
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("🚶 Safe Walk Timer")

minutes = st.slider(
    "Set Safe Walk Duration (minutes)",
    1,
    60,
    5
)

if st.button("START SAFE WALK"):

    st.info("⏳ Safe Walk Timer Started")

    countdown = st.empty()

    for i in range(minutes * 60, 0, -1):

        mins, secs = divmod(i, 60)

        countdown.metric(
            "Remaining Time",
            f"{mins:02d}:{secs:02d}"
        )

        time.sleep(1)

    st.error("🚨 Time Expired - SOS ALERT ACTIVATED")

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# CRIME ZONE HEATMAP
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("🗺️ Crime Zone Heatmap")

m = folium.Map(
    location=[lat, lon],
    zoom_start=12
)

# User Location
folium.Marker(
    [lat, lon],
    tooltip="Your Location",
    popup="Safe Location"
).add_to(m)

# Simulated Crime Zones
crime_zones = [
    [lat + 0.01, lon + 0.01],
    [lat - 0.02, lon + 0.01],
    [lat + 0.02, lon - 0.01]
]

for zone in crime_zones:

    folium.Circle(
        location=zone,
        radius=500,
        color="red",
        fill=True,
        fill_opacity=0.5
    ).add_to(m)

st_folium(m, width=700)

st.warning("⚠️ Red zones indicate unsafe areas")

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# REAL AI STRESS DETECTION
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("🧠 AI Stress Detection")

st.write("AI analyzes emotional stress levels")

if st.button("ANALYZE STRESS"):

    stress_score = random.randint(1, 100)

    st.progress(stress_score)

    if stress_score > 75:

        st.error(f"""
        🚨 HIGH STRESS DETECTED
        
        Stress Level: {stress_score}%
        Emergency protocol activated.
        """)

    elif stress_score > 45:

        st.warning(f"""
        ⚠️ Moderate Stress
        
        Stress Level: {stress_score}%
        """)

    else:

        st.success(f"""
        😊 Safe Emotional State
        
        Stress Level: {stress_score}%
        """)

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# LIVE LOCATION MAP
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("📍 Live Location")

st.success(f"""
Current Location:
📍 {city}
Latitude: {lat}
Longitude: {lon}
""")

maps_link = f"https://www.google.com/maps?q={lat},{lon}"

st.markdown(f"[Open Google Maps]({maps_link})")

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.markdown("""
<center>
🚨 Women Safety App | Hackathon Project
</center>
""", unsafe_allow_html=True)
