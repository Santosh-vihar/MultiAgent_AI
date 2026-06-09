import os
import pandas as pd
import streamlit as st

from agents import (
    architect_agent,
    risk_agent,
    failure_agent,
    innovation_agent,
)
from pdf_reader import extract_pdf_text

st.set_page_config(page_title="Oracle AI", layout="wide")

st.markdown(
    """
    <style>
        .stApp {
            background: radial-gradient(circle at 15% 20%, #f7f4ef 0%, #f1ede6 35%, #e9ecef 100%);
            color: #1f2937;
        }
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0f3d5e 0%, #0b2f4a 100%);
            border-right: 1px solid rgba(255, 255, 255, 0.12);
        }
        [data-testid="stSidebar"] * {
            color: #f8fafc;
        }
        [data-testid="stSidebar"] div[data-baseweb="select"] > div {
            background-color: rgba(255, 255, 255, 0.12);
            border: 1px solid rgba(255, 255, 255, 0.25);
        }
        h1, h2, h3 {
            color: #0b2f4a;
            letter-spacing: 0.3px;
        }
        .hero-card {
            background: linear-gradient(120deg, rgba(255,255,255,0.94), rgba(245,248,250,0.96));
            border: 1px solid #dbe4ea;
            border-radius: 18px;
            padding: 22px 24px;
            box-shadow: 0 10px 26px rgba(22, 34, 51, 0.08);
            margin-bottom: 1rem;
        }
        .section-title {
            margin-top: 0.6rem;
            margin-bottom: 0.2rem;
            font-size: 1.2rem;
            font-weight: 700;
            color: #0f3d5e;
        }
        .section-sub {
            color: #425466;
            margin-bottom: 0.9rem;
        }
        div[data-testid="stButton"] button {
            background: linear-gradient(135deg, #0f766e, #0f4c75);
            color: #ffffff;
            border: none;
            border-radius: 10px;
            font-weight: 600;
            padding: 0.55rem 1rem;
        }
        div[data-testid="stButton"] button:hover {
            filter: brightness(1.05);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

nav_options = ["Home", "Chatbot", "About"]
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

if "navigation_selectbox" not in st.session_state:
    st.session_state.navigation_selectbox = st.session_state.current_page

def on_page_change():
    st.session_state.current_page = st.session_state.navigation_selectbox

page = st.sidebar.selectbox(
    "Navigate",
    nav_options,
    key="navigation_selectbox",
    on_change=on_page_change,
)
st.session_state.current_page = page

if "analysis" not in st.session_state:
    st.session_state.analysis = {}

if page == "Home":
    st.title("Oracle AI")
    st.subheader("AI that finds what humans forget.")
    st.markdown(
        """
        <div class='hero-card'>
            Many projects <span style='color:#D62839; font-weight:700'>fail because teams overlook hidden requirements, risks, and architectural challenges</span>.<br>
            Current AI tools mostly answer questions. Oracle AI helps teams review ideas before they become expensive mistakes.
        </div>
        """,
        unsafe_allow_html=True,
    )

    img_path = "image.png"
    vid_path = "video.mp4"

    df = pd.DataFrame(
        {
            "Normal AI Chatbot": [
                "Answers Questions",
                "Gives Information",
                "Reactive",
                "Generic Suggestions",
                "No Failure Prediction",
            ],
            "Oracle AI": [
                "Reviews Ideas",
                "Finds Risks",
                "Proactive",
                "Architecture Analysis",
                "Failure Prediction",
            ],
        }
    )

    styled_df = (
        df.style
        .set_properties(**{
            "font-size": "18px",
            "font-weight": "bold",
            "color": "black",
        })
        .set_table_styles([
            {
                "selector": "th",
                "props": [
                    ("font-size", "20px"),
                    ("font-weight", "bold"),
                    ("color", "black"),
                    ("background-color", "#f0f2f6"),
                ],
            }
        ])
    )

    st.markdown("<div class='section-title'>Comparison Snapshot</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-sub'>See how Oracle AI goes beyond a normal chatbot by proactively identifying failure points and architecture risks.</div>",
        unsafe_allow_html=True,
    )
    st.dataframe(styled_df, use_container_width=True, hide_index=True)

    st.markdown("<div class='section-title'>How Oracle AI Thinks</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-sub'>This visual explains Oracle AI's review mindset: it inspects assumptions, highlights blind spots, and maps practical next steps before execution.</div>",
        unsafe_allow_html=True,
    )

    if os.path.exists(img_path):
        st.image(img_path, use_container_width=True)
    else:
        uploaded_img = st.file_uploader("Upload intro image", type=["png", "jpg", "jpeg"], key="img")
        if uploaded_img:
            st.image(uploaded_img, use_container_width=True)

    st.markdown("<div class='section-title'>What This Video Covers</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-sub'>A quick walkthrough of Oracle AI's purpose, how it evaluates ideas, and the kind of risks it can surface early in your planning process.</div>",
        unsafe_allow_html=True,
    )

    if os.path.exists(vid_path):
        st.video(vid_path)
    else:
        uploaded_vid = st.file_uploader("Upload intro video", type=["mp4", "mov", "avi"], key="vid")
        if uploaded_vid:
            st.video(uploaded_vid)

    if st.button("Open Chatbot"):
        st.session_state.current_page = "Chatbot"
        st.session_state.navigation_selectbox = "Chatbot"
        st.rerun()

if page == "Chatbot":
    st.title("Oracle AI - Chatbot")
    st.write("Upload a project document or describe your project idea. Oracle AI will analyze it from multiple expert perspectives.")

    uploaded_pdf = st.file_uploader("Upload project PDF (optional)", type=["pdf"])
    query = st.text_area(
        "Project idea",
        height=180,
        placeholder="Example: I want to create a food waste management system for hostels...",
    )

    if uploaded_pdf is not None:
        pdf_text = extract_pdf_text(uploaded_pdf)
        if pdf_text.strip():
            st.success("PDF processed successfully.")
            with st.expander("View extracted text"):
                st.write(pdf_text)
            query = pdf_text
        else:
            st.warning("No text could be extracted from the PDF.")

    if st.button("Analyze project"):
        if "GROQ_API_KEY" not in st.secrets or not st.secrets["GROQ_API_KEY"].strip():
            st.error("🔑 **GROQ_API_KEY is not configured!** Please configure the API key in your Streamlit Cloud Dashboard under **Settings -> Secrets** or locally in `.streamlit/secrets.toml`.")
        elif query and query.strip():
            with st.spinner("Oracle AI is reviewing your project..."):
                try:
                    st.session_state.analysis = {
                        "architect": architect_agent(query),
                        "risk": risk_agent(query),
                        "failure": failure_agent(query),
                        "innovation": innovation_agent(query),
                    }
                except Exception as e:
                    st.error(f"⚠️ **Error connecting to Groq API:** {e}")
        else:
            st.warning("Please enter a project idea or upload a PDF.")

    if st.session_state.analysis:
        tab1, tab2, tab3, tab4 = st.tabs(["Architect", "Risk", "Failure", "Innovation"])

        with tab1:
            st.markdown("### Architecture Review")
            st.markdown(st.session_state.analysis["architect"])

        with tab2:
            st.markdown("### Risk Analysis")
            st.markdown(st.session_state.analysis["risk"])

        with tab3:
            st.markdown("### Failure Prediction")
            st.markdown(st.session_state.analysis["failure"])

        with tab4:
            st.markdown("### Innovation Review")
            st.markdown(st.session_state.analysis["innovation"])

if page == "About":
    st.title("About Oracle AI")
    
    st.markdown(
        """
        <div class="hero-card">
            <h3>Why Oracle AI is better than standard Chatbots</h3>
            <p>Traditional AI assistants are <b>reactive</b>—they answer questions, write code, or agree with your ideas, which can lead to confirmation bias and critical oversights. 
            Oracle AI is <b>proactive and adversarial</b>. It doesn't just agree with you; it uses a specialized <b>Multi-Agent framework</b> designed to pressure-test your concepts from four different expert angles:</p>
            <ul>
                <li><b>Senior Software Architect:</b> Uncovers hidden dependencies, database designs, and structural gaps.</li>
                <li><b>Risk Assessment Specialist:</b> Thinks like an attacker to identify security, scalability, and operational risks.</li>
                <li><b>Failure Prediction Engine:</b> Analyzes bottleneck constraints and provides an objective statistical success probability.</li>
                <li><b>Innovation Reviewer:</b> Assesses novelty, market practicality, and how to differentiate your idea.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Core Features")
    st.markdown("- **Adversarial Feedback Loops:** Finds the flaws in your plan before they become expensive mistakes.")
    st.markdown("- **PDF Document Parsing:** Upload complex project spec sheets directly to get them reviewed instantly.")
    st.markdown("- **Dynamic Expert Panels:** Simulates a professional corporate design-review board in seconds.")

    st.markdown("---")
    st.markdown("### Contact & Connect")
    st.markdown(
        """
        Feel free to reach out for feedback, collaborations, or questions!
        
        * 📧 **Email:** [santoshvihar06@gmail.com](mailto:santoshvihar06@gmail.com)
        * 💻 **GitHub:** [GitHub Profile](https://github.com/Santosh-vihar)
        * 🔗 **LinkedIn:** [Santosh Vihar](https://www.linkedin.com/in/santosh-vihar-39220a355/)
        """
    )
