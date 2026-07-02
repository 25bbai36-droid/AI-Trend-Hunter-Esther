import streamlit as st
import time

st.set_page_config(
    page_title="AI Trend Hunter",
    page_icon="📈",
    layout="wide"
)
with st.sidebar:
    st.image("https://img.icons8.com/color/96/artificial-intelligence.png", width=90)
    st.image(
    "https://img.icons8.com/fluency/240/artificial-intelligence.png",
    width=120
)
st.title("📈 AI Trend Hunter")
st.markdown("### Discover trending topics and AI-powered content ideas instantly.")
st.title("AI Trend Hunter")

st.markdown("---")

st.write("🤖 AI Powered")
st.write("📈 Real-time Trend Discovery")
st.write("💡 Content Ideas")
st.write("🏷 Smart Hashtags")

st.markdown("---")

st.success("Project by Esther Pinto")
st.title("📈 AI Trend Hunter")

st.write("Discover trending topics and AI-powered content ideas instantly.")

st.markdown("---")
col1,col2,col3=st.columns(3)

col1.metric("🔥 Trend Score","92%")
col2.metric("💡 Content Ideas","15")
col3.metric("🏷 Hashtags","25")
business=st.text_input("Enter your Business Category")
if st.button("🚀 Find AI Trends"):
    with st.spinner("🤖 AI is analysing trends..."):
        time.sleep(2)
        st.success("Analysis Complete ✅")
        st.progress(92)
        st.subheader("🔥 Trending Topics")

    st.info("AI Automation")
    st.info("Digital Marketing")
    st.info("Personal Branding")
    st.subheader("🏷 Suggested Hashtags")

    st.success("#AI")

    st.success("#Trending")

    st.success("#BusinessGrowth")

    st.success("#Marketing")
    st.subheader("💡 AI Content Ideas")

    st.write("✅ Top 5 AI Tools for Businesses")

    st.write("✅ Latest Marketing Trends")

    st.write("✅ Future of Artificial Intelligence")

    st.write("✅ Best Social Media Strategies")
    st.subheader("📊 Final AI Report")

    st.write("Trend Score : 92/100")

    st.write("Predicted Reach : High")

    st.write("Recommended Platform : Instagram")

    st.write("Best Time to Post : 7 PM")
    st.markdown("---")

st.caption("Developed by Esther Pinto ❤️")
    