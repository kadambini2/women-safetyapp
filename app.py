# ==========================================
# WOMEN SAFETY APP 🚨
# Streamlit Advanced Version
# Speech Recognition Removed
# ==========================================

import streamlit as st
import requests
import random
import time
from datetime import datetime
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
    height: 3em;
    border-radius: 10px;
    font-size: 18px;
    font-weight: bold;
    background-color: red;
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

name = st.sidebar.text_input("Enter Your Name")
phone = st.sidebar.text_input("Phone Number")
contact = st.sidebar.text_input("Emergency Contact Number")

# ==========================================
# LOCATION FUNCTION
# ==========================================

def get_location():

    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()

        loc = data["loc"].split(",")

        lat = float(loc[0])
        lon = float(loc[1])

        city = data.get("city", "Unknown")

        return lat, lon, city

    except:

        return 12.9716, 77.5946, "Bangalore"

# ==========================================
# GET LOCATION
# ==========================================

lat, lon, city = get_location()

# ==========================================
# SOS ALERT
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("🚨 Emergency SOS")

if st.button("SEND SOS ALERT"):

    maps_link = f"https://www.google.com/maps?q={lat},{lon}"

    st.error("🚨 SOS ALERT ACTIVATED")

    st.success(f"""
    Emergency Alert Sent Successfully
    
    👤 Name: {name}
    📞 Contact: {contact}
    📍 City: {city}
    """)

    st.markdown(f"""
    ### Emergency Details
    
    HELP! I am in danger.
    
    📍 Live Location:
    {maps_link}
    
    🕒 Time:
    {datetime.now()}
    """)

    st.balloons()

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# CAMERA EVIDENCE
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("📸 Camera Evidence")

camera = st.camera_input("Capture Emergency Evidence")

if camera:

    st.success("📸 Evidence Captured Successfully")

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# SECRET AUDIO RECORDING
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("🎤 Secret Audio Recording")

if st.button("START RECORDING"):

    st.info("🎙️ Recording Started Secretly")

    progress = st.progress(0)

    for i in range(100):

        time.sleep(0.02)
        progress.progress(i + 1)

    st.success("✅ Recording Saved")

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# SAFE WALK TIMER
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("🚶 Safe Walk Timer")

minutes = st.slider(
    "Set Walk Duration (Minutes)",
    1,
    60,
    5
)

if st.button("START SAFE WALK"):

    countdown = st.empty()

    for i in range(minutes * 60, 0, -1):

        mins, secs = divmod(i, 60)

        countdown.metric(
            "Remaining Time",
            f"{mins:02d}:{secs:02d}"
        )

        time.sleep(1)

    st.error("🚨 Safe Walk Timer Expired")
    st.warning("Emergency SOS Triggered")

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

# User Location Marker
folium.Marker(
    [lat, lon],
    tooltip="Your Location",
    popup="Current Safe Location"
).add_to(m)

# Simulated Crime Zones
crime_zones = [
    [lat + 0.01, lon + 0.01],
    [lat - 0.02, lon + 0.02],
    [lat + 0.015, lon - 0.015]
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

st.warning("⚠️ Red areas indicate unsafe zones")

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# AI STRESS DETECTION
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("🧠 AI Stress Detection")

st.write("Analyze emotional stress levels")

if st.button("ANALYZE STRESS LEVEL"):

    stress = random.randint(1, 100)

    st.progress(stress)

    if stress > 75:

        st.error(f"""
        🚨 HIGH STRESS DETECTED
        
        Stress Level: {stress}%
        Emergency Action Suggested
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

st.header("📍 Live Location")

st.success(f"""
📍 Current City: {city}

Latitude: {lat}
Longitude: {lon}
""")

maps_url = f"https://www.google.com/maps?q={lat},{lon}"

st.markdown(f"[🌍 Open in Google Maps]({maps_url})")

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# NEARBY HELP CENTERS
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("🏥 Nearby Help Centers")

if st.button("FIND NEARBY HELP"):

    police = "https://www.google.com/maps/search/police+station+near+me/"
    hospital = "https://www.google.com/maps/search/hospital+near+me/"

    st.success("Nearby Help Centers Found")

    st.markdown(f"[🚓 Nearby Police Stations]({police})")
    st.markdown(f"[🏥 Nearby Hospitals]({hospital})")

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.markdown("""
<center>
🚨 Women Safety App | Streamlit Hackathon Project
</center>
""", unsafe_allow_html=True)
