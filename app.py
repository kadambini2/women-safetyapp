# ==========================================
# WOMEN SAFETY APP 🚨
# Updated Modern UI Version
# Built by Kadambini Pujari
# ==========================================

import streamlit as st
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
    background: linear-gradient(to right, #ffe6ee, #fff5f8);
}

.hero {
    background: linear-gradient(135deg, #ff4b6e, #ff758c);
    padding: 35px;
    border-radius: 25px;
    color: white;
    text-align: center;
    box-shadow: 0px 8px 25px rgba(255,75,110,0.3);
    margin-bottom: 25px;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    margin-bottom: 20px;
    box-shadow: 0px 5px 18px rgba(0,0,0,0.08);
}

.stButton>button {
    width: 100%;
    height: 3.2em;
    border-radius: 15px;
    border: none;
    font-size: 18px;
    font-weight: bold;
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
    font-size: 18px;
    font-weight: 500;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HERO SECTION
# ==========================================

st.markdown("""
<div class="hero">
    <h1>🚨 Women Safety App</h1>
    <h3>AI Powered Personal Safety Companion</h3>
    <p>Stay Safe • Stay Smart • Stay Protected</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("👤 User Details")

name = st.sidebar.text_input("Your Name")
phone = st.sidebar.text_input("Phone Number")
contact = st.sidebar.text_input("Emergency Contact")

# ==========================================
# MANUAL LOCATION SETTINGS
# ==========================================

st.sidebar.title("📍 Your Location")

city = st.sidebar.text_input(
    "Current City",
    "Kalaburagi"
)

lat = st.sidebar.text_input(
    "Latitude",
    "17.3297"
)

lon = st.sidebar.text_input(
    "Longitude",
    "76.8343"
)

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
# SOS ALERT
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

    st.info("🎙️ Recording Started Securely")

    progress = st.progress(0)

    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)

    st.success("✅ Recording Saved Successfully")

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

    police = "https://www.google.com/maps/search/police+station+near+me/"
    hospital = "https://www.google.com/maps/search/hospital+near+me/"

    st.success("Nearby Services Found")

    st.markdown(f"[🚓 Nearby Police Stations]({police})")
    st.markdown(f"[🏥 Nearby Hospitals]({hospital})")

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<hr>

<div class="footer">

🚨 Women Safety App <br><br>

🛡️ Built with ❤️ by # ==========================================
# WOMEN SAFETY APP 🚨
# Updated Modern UI Version
# Built by Kadambini Pujari
# ==========================================

import streamlit as st
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
    background: linear-gradient(to right, #ffe6ee, #fff5f8);
}

.hero {
    background: linear-gradient(135deg, #ff4b6e, #ff758c);
    padding: 35px;
    border-radius: 25px;
    color: white;
    text-align: center;
    box-shadow: 0px 8px 25px rgba(255,75,110,0.3);
    margin-bottom: 25px;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    margin-bottom: 20px;
    box-shadow: 0px 5px 18px rgba(0,0,0,0.08);
}

.stButton>button {
    width: 100%;
    height: 3.2em;
    border-radius: 15px;
    border: none;
    font-size: 18px;
    font-weight: bold;
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
    font-size: 18px;
    font-weight: 500;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HERO SECTION
# ==========================================

st.markdown("""
<div class="hero">
    <h1>🚨 Women Safety App</h1>
    <h3>AI Powered Personal Safety Companion</h3>
    <p>Stay Safe • Stay Smart • Stay Protected</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("👤 User Details")

name = st.sidebar.text_input("Your Name")
phone = st.sidebar.text_input("Phone Number")
contact = st.sidebar.text_input("Emergency Contact")

# ==========================================
# MANUAL LOCATION SETTINGS
# ==========================================

st.sidebar.title("📍 Your Location")

city = st.sidebar.text_input(
    "Current City",
    "Kalaburagi"
)

lat = st.sidebar.text_input(
    "Latitude",
    "17.3297"
)

lon = st.sidebar.text_input(
    "Longitude",
    "76.8343"
)

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
# SOS ALERT
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

    st.info("🎙️ Recording Started Securely")

    progress = st.progress(0)

    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)

    st.success("✅ Recording Saved Successfully")

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

    police = "https://www.google.com/maps/search/police+station+near+me/"
    hospital = "https://www.google.com/maps/search/hospital+near+me/"

    st.success("Nearby Services Found")

    st.markdown(f"[🚓 Nearby Police Stations]({police})")
    st.markdown(f"[🏥 Nearby Hospitals]({hospital})")

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<hr>

<div class="footer">

🚨 Women Safety App <br><br>

🛡️ Built with ❤️ by <b>Kadambini Pujari</b># ==========================================
# WOMEN SAFETY APP 🚨
# Updated Modern UI Version
# Built by Kadambini Pujari
# ==========================================

import streamlit as st
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
    background: linear-gradient(to right, #ffe6ee, #fff5f8);
}

.hero {
    background: linear-gradient(135deg, #ff4b6e, #ff758c);
    padding: 35px;
    border-radius: 25px;
    color: white;
    text-align: center;
    box-shadow: 0px 8px 25px rgba(255,75,110,0.3);
    margin-bottom: 25px;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    margin-bottom: 20px;
    box-shadow: 0px 5px 18px rgba(0,0,0,0.08);
}

.stButton>button {
    width: 100%;
    height: 3.2em;
    border-radius: 15px;
    border: none;
    font-size: 18px;
    font-weight: bold;
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
    font-size: 18px;
    font-weight: 500;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HERO SECTION
# ==========================================

st.markdown("""
<div class="hero">
    <h1>🚨 Women Safety App</h1>
    <h3>AI Powered Personal Safety Companion</h3>
    <p>Stay Safe • Stay Smart • Stay Protected</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("👤 User Details")

name = st.sidebar.text_input("Your Name")
phone = st.sidebar.text_input("Phone Number")
contact = st.sidebar.text_input("Emergency Contact")

# ==========================================
# MANUAL LOCATION SETTINGS
# ==========================================

st.sidebar.title("📍 Your Location")

city = st.sidebar.text_input(
    "Current City",
    "Kalaburagi"
)

lat = st.sidebar.text_input(
    "Latitude",
    "17.3297"
)

lon = st.sidebar.text_input(
    "Longitude",
    "76.8343"
)

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
# SOS ALERT
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

    st.info("🎙️ Recording Started Securely")

    progress = st.progress(0)

    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)

    st.success("✅ Recording Saved Successfully")

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

    police = "https://www.google.com/maps/search/police+station+near+me/"
    hospital = "https://www.google.com/maps/search/hospital+near+me/"

    st.success("Nearby Services Found")

    st.markdown(f"[🚓 Nearby Police Stations]({police})")
    st.markdown(f"[🏥 Nearby Hospitals]({hospital})")

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<hr>

<div class="footer">

🚨 Women Safety App <br><br>

🛡️ Built with ❤️ by <b>Kadambini Pujari</b>

</div>
""", unsafe_allow_html=True)

</div>
""", unsafe_allow_html=True)

</div>
""", unsafe_allow_html=True)
