import streamlit as st
import random
import time
import smtplib
from email.mime.text import MIMEText
from streamlit_js_eval import streamlit_js_eval

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="Women Safety App",
    page_icon="🚨",
    layout="wide"
)

# ==========================
# CUSTOM CSS
# ==========================

st.markdown("""
<style>

.big-title{
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:red;
}

.sos-btn button{
    width:100%;
    height:90px;
    font-size:30px;
    background:red !important;
    color:white !important;
    border-radius:20px;
}

.card{
    padding:20px;
    border-radius:20px;
    background:#fff5f5;
    margin-bottom:15px;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# TITLE
# ==========================

st.markdown(
    '<p class="big-title">🚨 Women Safety App</p>',
    unsafe_allow_html=True
)

# ==========================
# USER DETAILS
# ==========================

st.sidebar.header("👩 User Details")

name = st.sidebar.text_input("Your Name")

email = st.sidebar.text_input("Emergency Email")

phone = st.sidebar.text_input("Emergency WhatsApp Number")

# ==========================
# LIVE LOCATION
# ==========================

st.subheader("📍 Live Location")

location = streamlit_js_eval(
    js_expressions="""
    navigator.geolocation.getCurrentPosition(
        (pos) => {
            return {
                latitude: pos.coords.latitude,
                longitude: pos.coords.longitude
            }
        }
    )
    """,
    key="location"
)

lat = None
lon = None

if location:

    lat = location["latitude"]
    lon = location["longitude"]

    st.success(f"Latitude: {lat}")
    st.success(f"Longitude: {lon}")

    maps = f"https://www.google.com/maps?q={lat},{lon}"

    st.markdown(f"[📍 Open Google Maps]({maps})")

else:
    st.warning("Please allow location access.")

# ==========================
# EMAIL CONFIG
# ==========================

SENDER_EMAIL = "YOUR_EMAIL@gmail.com"
SENDER_PASSWORD = "YOUR_APP_PASSWORD"

# ==========================
# SEND EMAIL
# ==========================

def send_email(message):

    try:

        msg = MIMEText(message)

        msg["Subject"] = "Emergency SOS Alert"

        msg["From"] = SENDER_EMAIL

        msg["To"] = email

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login(
            SENDER_EMAIL,
            SENDER_PASSWORD
        )

        server.sendmail(
            SENDER_EMAIL,
            email,
            msg.as_string()
        )

        server.quit()

        st.success("✅ Email Sent Successfully")

    except Exception as e:

        st.error(e)

# ==========================
# SOS BUTTON
# ==========================

st.subheader("🆘 Emergency SOS")

with st.container():

    st.markdown(
        '<div class="sos-btn">',
        unsafe_allow_html=True
    )

    if st.button("🚨 SEND SOS ALERT"):

        if lat and lon:

            emergency_message = f"""
HELP! I am in danger.

Name: {name}

My Live Location:
https://www.google.com/maps?q={lat},{lon}

Please help immediately.
"""

            st.error("🚨 SOS ACTIVATED")

            st.code(emergency_message)

            # SEND EMAIL
            send_email(emergency_message)

            # WHATSAPP
            whatsapp_link = f"https://wa.me/{phone}?text={emergency_message}"

            st.markdown(
                f"[📲 Send WhatsApp Alert]({whatsapp_link})"
            )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

# ==========================
# FAKE CALL
# ==========================

st.subheader("📞 Fake Call")

callers = [
    "Mom",
    "Police",
    "Friend",
    "Brother"
]

if st.button("📲 Receive Fake Call"):

    st.info("Incoming Call...")

    time.sleep(2)

    st.success(
        f"📞 Calling from {random.choice(callers)}"
    )

# ==========================
# EMERGENCY SIREN
# ==========================

st.subheader("🚨 Emergency Siren")

audio_file = open("siren.mp3", "rb")

audio_bytes = audio_file.read()

st.audio(audio_bytes)

# ==========================
# STRESS DETECTION
# ==========================

st.subheader("🎤 AI Stress Detection")

stress = st.slider(
    "Stress Level",
    0,
    100,
    20
)

if st.button("Analyze Stress"):

    if stress < 30:

        st.success("✅ Calm Voice")

    elif stress < 70:

        st.warning("⚠ Moderate Stress")

    else:

        st.error("🚨 Panic Detected")

# ==========================
# NEARBY HELP
# ==========================

st.subheader("🏥 Nearby Help")

if lat and lon:

    police = f"https://www.google.com/maps/search/police+station/@{lat},{lon},15z"

    hospital = f"https://www.google.com/maps/search/hospital/@{lat},{lon},15z"

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            f"[🚓 Nearby Police Stations]({police})"
        )

    with col2:

        st.markdown(
            f"[🏥 Nearby Hospitals]({hospital})"
        )

# ==========================
# SAFETY TIPS
# ==========================

st.subheader("🛡 Safety Tips")

tips = [
    "Share location with trusted people.",
    "Avoid isolated areas.",
    "Use SOS immediately in danger.",
    "Keep emergency contacts ready.",
    "Stay alert while travelling."
]

for tip in tips:

    st.markdown(
        f"""
        <div class="card">
        ✅ {tip}
        </div>
        """,
        unsafe_allow_html=True
    )

# ==========================
# FOOTER
# ==========================

st.markdown("---")

st.caption("Made with ❤️ using Streamlit")
