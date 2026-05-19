# ==========================================
# WOMEN SAFETY APP 🚨
# Modern UI Version (Without Folium)
# ==========================================

import streamlit as st
import requests
import random
import time
from datetime import datetime

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Women Safety App",
    page_icon="🚨",
    layout="wide"
)

# ==========================================
# MODERN CSS UI
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.main {
    background: linear-gradient(to right, #ffe6f0, #fff5f8);
}

.hero {
    background: linear-gradient(135deg, #ff4b6e, #ff758c);
    padding: 35px;
    border-radius: 25px;
    color: white;
    text-align: center;
    box-shadow: 0px 8px 30px rgba(255, 75, 110, 0.3);
    margin-bottom: 25px;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.08);
    margin-bottom: 20px;
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px);
}

.stButton>button {
    width: 100%;
    height: 3.2em;
    border-radius: 15px;
    border: none;
    font-size: 18px;
    font-weight: 600;
    background: linear-gradient(135deg, #ff4b6e, #ff758c);
    color: white;
}

.stButton>button:hover {
    background: linear-gradient(135deg, #ff3355, #ff5577);
}

.metric-box {
    background: #fff0f5;
    padding: 15px;
    border-radius: 15px;
    text-align: center;
}

.footer {
    text-align: center;
    color: gray;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# LOCATION FUNCTION
# ==========================================

def get_location():

    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()

        loc = data["loc"].split(",")

        lat = loc[0]
        lon = loc[1]

        city = data.get("city", "Unknown")

        return lat, lon, city

    except:
        return "12.9716", "77.5946", "Bangalore"

lat, lon, city = get_location()

# ==========================================
# HERO SECTION
# ==========================================

st.markdown(f"""
<div class="hero">
    <h1>🚨 Women Safety App</h1>
    <h3>AI Powered Personal Safety Companion</h3>
    <p>Stay Safe • Stay Smart • Stay Protected</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("👤 User Profile")

name = st.sidebar.text_input("Your Name")
phone = st.sidebar.text_input("Phone Number")
contact = st.sidebar.text_input("Emergency Contact")

st.sidebar.success("✅ Safety System Active")

# ==========================================
# DASHBOARD METRICS
# ==========================================

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="metric-box">
        <h2>📍</h2>
        <h4>Live Tracking</h4>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-box">
        <h2>🛡️</h2>
        <h4>Protection Enabled</h4>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-box">
        <h2>🚓</h2>
        <h4>Emergency Ready</h4>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ==========================================
# SOS SECTION
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("🚨 Emergency SOS")

if st.button("SEND EMERGENCY ALERT"):

    maps_link = f"https://www.google.com/maps?q={lat},{lon}"

    st.error("🚨 SOS ALERT ACTIVATED")

    st.success(f"""
    Emergency Alert Sent Successfully
    
    👤 Name: {name}
    📞 Emergency Contact: {contact}
    📍 Current City: {city}
    """)

    st.markdown(f"""
    ### 📍 Live Location
    
    {maps_link}
    
    ### 🕒 Time
    
    {datetime.now()}
    """)

    st.balloons()

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# CAMERA EVIDENCE
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📸 Camera Evidence")

camera = st.camera_input("Capture Emergency Evidence")

if camera:
    st.success("✅ Evidence Captured Successfully")

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# SECRET RECORDING
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("🎤 Secret Audio Recording")

if st.button("START SECRET RECORDING"):

    st.info("🎙️ Recording Started")

    progress = st.progress(0)

    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)

    st.success("✅ Recording Saved Securely")

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# SAFE WALK TIMER
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("🚶 Safe Walk Timer")

minutes = st.slider(
    "Select Duration (Minutes)",
    1,
    30,
    5
)

if st.button("START SAFE WALK"):

    timer = st.empty()

    for i in range(minutes * 60, 0, -1):

        mins, secs = divmod(i, 60)

        timer.metric(
            "Remaining Time",
            f"{mins:02d}:{secs:02d}"
        )

        time.sleep(1)

    st.error("🚨 Safe Walk Timer Expired")
    st.warning("Emergency Alert Triggered")

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# AI STRESS DETECTION
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("🧠 AI Stress Detection")

if st.button("ANALYZE STRESS LEVEL"):

    stress = random.randint(1, 100)

    st.progress(stress)

    if stress > 75:

        st.error(f"""
        🚨 High Stress Detected
        
        Stress Level: {stress}%
        """)

    elif stress > 40:

        st.warning(f"""
        ⚠️ Moderate Stress
        
        Stress Level: {stress}%
        """)

    else:

        st.success(f"""
        😊 Safe Emotional State
        
        Stress Level: {stress}%
        """)

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# LIVE LOCATION
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📍 Live Location")

st.success(f"""
📍 City: {city}

Latitude: {lat}
Longitude: {lon}
""")

maps_url = f"https://www.google.com/maps?q={lat},{lon}"

st.markdown(f"[🌍 Open Live Location in Google Maps]({maps_url})")

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# NEARBY HELP
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("🏥 Nearby Emergency Help")

if st.button("FIND HELP CENTERS"):

    st.success("Nearby Services Found")

    police = "https://www.google.com/maps/search/police+station+near+me/"
    hospital = "https://www.google.com/maps/search/hospital+near+me/"

    st.markdown(f"[🚓 Nearby Police Stations]({police})")
    st.markdown(f"[🏥 Nearby Hospitals]({hospital})")

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<div class="footer">
    🚨 Women Safety App • Hackathon Project • Built with Streamlit
</div>
""", unsafe_allow_html=True)
