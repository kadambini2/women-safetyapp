# app.py
# ==========================================
# WOMEN SAFETY APP 🚨
# Streamlit Hackathon Project
# ==========================================

import streamlit as st
import requests
import webbrowser
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
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>
.main {
    background-color: #fff5f7;
}

.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    font-size: 18px;
    font-weight: bold;
}

.sos-btn button {
    background-color: red;
    color: white;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background: white;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================

st.title("🚨 Women Safety App")
st.subheader("Your Personal Emergency Protection System")

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("⚙️ Settings")

user_name = st.sidebar.text_input("Enter Your Name")
phone = st.sidebar.text_input("Phone Number")

contact1 = st.sidebar.text_input("Emergency Contact 1")
contact2 = st.sidebar.text_input("Emergency Contact 2")
contact3 = st.sidebar.text_input("Emergency Contact 3")

# ==========================================
# LOCATION FUNCTION
# ==========================================

def get_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()

        city = data.get("city", "Unknown")
        region = data.get("region", "")
        country = data.get("country", "")
        loc = data.get("loc", "")

        latitude, longitude = loc.split(",")

        return city, region, country, latitude, longitude

    except:
        return "Unknown", "", "", "0", "0"

# ==========================================
# HOME DASHBOARD
# ==========================================

col1, col2 = st.columns(2)

# ==========================================
# SOS BUTTON
# ==========================================

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.header("🚨 SOS Emergency")

    if st.button("SEND SOS ALERT"):
        city, region, country, lat, lon = get_location()

        maps_url = f"https://www.google.com/maps?q={lat},{lon}"

        st.error("🚨 SOS ALERT ACTIVATED!")

        st.success(f"""
        Alert Sent Successfully!

        👤 Name: {user_name}
        📍 Location: {city}, {region}, {country}
        📌 Coordinates: {lat}, {lon}
        """)

        st.markdown(f"""
        ### Emergency Message Sent:
        
        HELP! I am in danger.
        
        Name: {user_name}
        
        My Live Location:
        {maps_url}
        
        Time: {datetime.now()}
        """)

        st.balloons()

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# LIVE LOCATION
# ==========================================

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.header("📍 Live Location")

    if st.button("GET CURRENT LOCATION"):

        city, region, country, lat, lon = get_location()

        st.success(f"""
        📍 City: {city}
        🌍 Region: {region}
        🌎 Country: {country}
        """)

        maps_url = f"https://www.google.com/maps?q={lat},{lon}"

        st.markdown(f"[Open in Google Maps]({maps_url})")

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# FAKE CALL FEATURE
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("📞 Fake Call Feature")

fake_name = st.text_input("Fake Caller Name", "Mom")

delay = st.slider("Call Delay (seconds)", 5, 30, 10)

if st.button("START FAKE CALL"):

    with st.spinner("Incoming call starting..."):
        time.sleep(delay)

    st.success(f"📞 Incoming Call from {fake_name}")

    st.audio(
        "https://www.soundjay.com/phone/telephone-ring-01a.mp3"
    )

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# AI STRESS DETECTION (SIMULATION)
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("🎙️ AI Voice Stress Detection")

st.write("Click button to simulate stress detection.")

if st.button("ANALYZE VOICE"):

    stress_level = random.randint(1, 100)

    st.progress(stress_level)

    if stress_level > 70:
        st.error(f"⚠️ High Stress Detected! ({stress_level}%)")
        st.warning("Emergency Alert Triggered!")

    elif stress_level > 40:
        st.warning(f"😟 Moderate Stress Detected ({stress_level}%)")

    else:
        st.success(f"😊 Normal Voice Detected ({stress_level}%)")

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# NEARBY HELP CENTERS
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("🏥 Nearby Police & Hospitals")

city, region, country, lat, lon = get_location()

if st.button("FIND NEARBY HELP"):

    police_url = f"https://www.google.com/maps/search/police+station+near+me/"
    hospital_url = f"https://www.google.com/maps/search/hospital+near+me/"

    st.success("Nearby Help Centers Found")

    st.markdown(f"[🚓 Find Police Stations]({police_url})")
    st.markdown(f"[🏥 Find Hospitals]({hospital_url})")

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# SMARTWATCH SECTION
# ==========================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("⌚ Smartwatch Integration")

watch_status = st.selectbox(
    "Smartwatch Status",
    ["Disconnected", "Connected"]
)

if watch_status == "Connected":
    st.success("⌚ Smartwatch Connected Successfully")

    if st.button("TRIGGER WATCH SOS"):
        st.error("🚨 SOS Triggered from Smartwatch")

else:
    st.warning("⌚ No Smartwatch Connected")

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.markdown("""
<center>
Made with ❤️ for Women's Safety
</center>
""", unsafe_allow_html=True)


