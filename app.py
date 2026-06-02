import streamlit as st
from recommender import recommend_places
from chatbot import chatbot_response
import os

# ==============================
# PAGE CONFIG
# ==============================

st.set_page_config(
    page_title="Travel Explorer AI",
    page_icon="🌍",
    layout="wide"
)

# ==============================
# CUSTOM CSS
# ==============================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600;700&display=swap');
            
/* Main Background */
.stApp{
    background-color:#f8fafc;
    font-family: 'DM Sans', sans-serif;
}

/* Navbar */
.navbar{
    background:linear-gradient(90deg,#06402B,#84eab3);
    padding:18px;
    border-radius:16px;
    text-align:center;
    color:white;
    font-size:28px;
    font-weight:700;
    margin-bottom:25px;
    box-shadow:0px 8px 20px rgba(0,0,0,0.12);
}

/* Hero */
.hero{
    color:black;
    text-align:left;
}
.hero h1{
    font-size:48px;
    font-weight:700;
    margin-bottom:10px;
}
.hero p{
    font-size:18px;
    color:#333;
}

   /* ---- Cards ---- */
[data-testid="stMain"] .stContainer {
    background: rgba(13, 20, 35, 0.85) !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 20px !important;
    padding: 28px 32px !important;
    backdrop-filter: blur(20px) !important;
    box-shadow: 0 1px 0 rgba(255,255,255,0.05) inset,
                0 20px 60px rgba(0,0,0,0.4) !important;
}


section[data-testid="stMain"] h1,
section[data-testid="stMain"] h2,
section[data-testid="stMain"] h3,
section[data-testid="stMain"] h4,
section[data-testid="stMain"] p,
section[data-testid="stMain"] span,
section[data-testid="stMain"] label {
    color: #111 !important;
}

div[data-testid="stMain"] * {
    color: #111 !important;
}

/* Sidebar background */
section[data-testid="stSidebar"]{
    background:linear-gradient(#013220);
}

/* Sidebar labels */
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] .stSelectbox label,
section[data-testid="stSidebar"] .stSlider label {
    color: white !important;
    font-weight: 600;
}

/* Sidebar header */
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h3 {
    color: white !important;
}


/* Buttons */
.stButton > button{
    background:linear-gradient(90deg,#06402B,#84eab3);
    color:white;
    border:none;
    border-radius:10px;
    font-weight:bold;
    height:3em;
    width:100%;
}

/* Images */
            
img{
    border-radius:20px;
}

/* ---- Footer ---- */
footer { 
    visibility: hidden; 
    }
.footer-custom {
    text-align: center;
    font-size: 0.78rem;
    color: #7e8fa6;
    margin-top: 3rem;
    letter-spacing: 0.04em;
}
.footer-dot { color: #FF0000; margin: 0 6px; }


</style>
""", unsafe_allow_html=True)

# ==============================
# NAVBAR
# ==============================

st.markdown("""
<div class="navbar">
🌍 Tourism Guide Assistant
</div>
""", unsafe_allow_html=True)

# ==============================
# SIDEBAR
# ==============================

with st.sidebar:

    st.header("🎯 Plan Your Trip")

    trip_type = st.selectbox(
        "Trip Type",
        ["Nature", "Adventure", "Historical"]
    )

    budget = st.select_slider(
        "Budget (PKR)",
        options=[
            10000,20000,30000,40000,
            50000,60000,70000,80000,
            90000,100000
        ],
        value=50000
    )

    weather = st.selectbox(
        "Weather",
        ["Cold","Hot","Moderate"]
    )

    days = st.slider(
        "Trip Duration",
        1,
        10,
        5
    )

    group_type = st.selectbox(
        "Travel With",
        ["Family","Friends","Couple"]
    )

    st.divider()

    st.markdown("""
<div style="
background:#0D4F3C;
padding:12px;
border-radius:10px;
color:white;
font-weight:500;
text-align:center;
">
✨ AI will suggest perfect destinations
</div>
""", unsafe_allow_html=True)

# ==============================
# HERO SECTION
# ==============================


st.markdown("""
<div class="hero">
<h1>🌍 Travel Explorer AI</h1>
<p>Discover personalized destinations based on your budget, weather, trip duration and travel style.</p>
</div>
""", unsafe_allow_html=True)

st.image(
    "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
    use_container_width=True
)

# ==============================
# QUICK INFO
# ==============================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Budget", f"PKR {budget:,}")

with c2:
    st.metric("Duration", f"{days} Days")

with c3:
    st.metric("Weather", weather)

with c4:
    st.metric("Group", group_type)

st.write("")

# ==============================
# GENERATE BUTTON
# ==============================

if st.button("🔍 Generate Recommendations"):

    results = recommend_places(
        trip_type,
        budget,
        weather,
        days,
        group_type
    )

    st.markdown("## 🏔 Recommended Destinations")

    if results is not None and len(results) > 0:

        for _, row in results.iterrows():

            place = row.get("place", "Unknown")

            image_path = (
                f"images/{place.lower().replace(' ','_')}.jpg"
            )

            with st.container(border=True):

                col1, col2 = st.columns([1, 2])

                # LEFT
                with col1:

                    if os.path.exists(image_path):
                        st.image(
                            image_path,
                            use_container_width=True
                        )
                    else:
                        st.image(
                            "https://picsum.photos/600/400",
                            use_container_width=True
                        )

                # RIGHT
                with col2:

                    st.subheader(f"📍 {place}")

                    score = int(
                        row.get("match_score", 0)
                    )

                    st.progress(score)

                    m1, m2, m3 = st.columns(3)

                    with m1:
                        st.metric(
                            "Match",
                            f"{score}%"
                        )

                    with m2:
                        st.metric(
                            "Budget",
                            f"PKR {row.get('budget','N/A')}"
                        )

                    with m3:
                        st.metric(
                            "Days",
                            row.get("days","N/A")
                        )

                    st.markdown("### 🎯 Activities")

                    st.info(
                        row.get(
                            "generated_activities",
                            "N/A"
                        )
                    )

                    st.markdown("### 🏷 Tags")

                    st.success(
                        row.get(
                            "generated_tags",
                            "N/A"
                        )
                    )

                    st.markdown("### 📝 Description")

                    st.write(
                        row.get(
                            "generated_description",
                            "N/A"
                        )
                    )

            st.write("")

    else:
        st.error("No destinations found.")

# ==============================
# CHATBOT
# ==============================

st.divider()

st.markdown("## 🤖 Travel Assistant")

user_input = st.chat_input(
    "Ask anything about travel..."
)

if user_input:

    st.chat_message("user").write(
        user_input
    )

    response = chatbot_response(
        user_input
    )

    st.chat_message("assistant").write(
        response
    )

# ==============================
# FOOTER
# ==============================

st.divider()

st.markdown("""
<div class="footer-custom">
    TravelExplorer AI
    <span class="footer-dot">•</span>
    Streamlit
    <span class="footer-dot">•</span>
    Tourism Recommendation System
    <span class="footer-dot">•</span>
    For Educational Use Only
</div>
""", unsafe_allow_html=True)