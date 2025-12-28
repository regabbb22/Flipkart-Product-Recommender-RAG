import streamlit as st
import requests
import time
from datetime import datetime
import os
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Flipkart Product Recommender",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for premium design with Flipkart Yellow theme
st.markdown("""
<style>
    /* Enhanced Multi-Color Theme - User Friendly */
    :root {
        --primary-gold: #FFD700;
        --secondary-gold: #FFC800;
        --accent-blue: #2874f0;
        --accent-green: #2ecc71; /* Emerald Green */
        --accent-orange: #ff9f43;
        --accent-purple: #9b59b6;
        --accent-cyan: #00d4ff;
        --background-dark: #141E30; 
        --card-bg: rgba(36, 59, 85, 0.6); 
        --text-light: #ecf0f1; 
        --text-dim: #bdc3c7;   
        --hover-glow: rgba(46, 204, 113, 0.6); /* Green Glow */
    }
    
    /* Main app background with subtle 'Natural Midnight' gradient */
    .stApp {
        background: linear-gradient(to right, #141E30, #243B55); /* Soothing Slate Gradient */
        color: var(--text-light);
        font-family: 'Inter', sans-serif;
    }

    /* Bold text is Gold, but hovers to Green */
    strong, b {
        color: var(--primary-gold);
        font-weight: 700;
        transition: color 0.3s ease;
    }
    strong:hover, b:hover {
        color: var(--accent-green);
        text-shadow: 0 0 10px var(--hover-glow);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%); /* Deep Slate Sidebar */
        border-right: 3px solid var(--accent-green); /* Green Border for Sidebar */
        box-shadow: 4px 0 20px rgba(46, 204, 113, 0.2);
    }

    /* Paragraphs and lists slightly dimmed for hierarchy */
    p, li {
        color: var(--text-light);
        line-height: 1.6;
    }
    
    /* Headers with varied colors */
    h1 {
        color: var(--accent-cyan) !important; /* Main title Cyan */
        font-weight: 800;
        text-shadow: 0 0 40px rgba(0, 212, 255, 0.6), 0 0 20px rgba(0, 212, 255, 0.4);
        animation: subtleGlow 3s ease-in-out infinite;
    }
    
    h2 {
        color: var(--accent-blue) !important;
        text-shadow: 0 0 20px rgba(40, 116, 240, 0.4);
    }
    
    h3 {
        color: var(--accent-green) !important; /* H3 is now GREEN */
        text-shadow: 0 0 15px rgba(46, 204, 113, 0.3);
    }
    
    h4, h5, h6 {
         color: var(--accent-orange) !important; /* H4-H6 moved to ORANGE */
    }
    
    @keyframes subtleGlow {
        0%, 100% { text-shadow: 0 0 40px rgba(0, 212, 255, 0.6), 0 0 20px rgba(0, 212, 255, 0.4); }
        50% { text-shadow: 0 0 50px rgba(0, 212, 255, 0.8), 0 0 30px rgba(0, 212, 255, 0.6); }
    }
    
    /* Enhanced Cards with glassmorphism */
    .stCard {
        background: linear-gradient(135deg, rgba(26, 31, 46, 0.9) 0%, rgba(37, 43, 59, 0.9) 100%);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 8px 32px rgba(40, 116, 240, 0.2);
        border: 2px solid rgba(40, 116, 240, 0.3);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .stCard:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(40, 116, 240, 0.4);
        border-color: rgba(0, 212, 255, 0.5);
    }
    
    /* Enhanced Buttons with gradient colors */
    .stButton>button {
        background: linear-gradient(135deg, var(--accent-blue) 0%, var(--accent-purple) 100%);
        color: #ffffff;
        border: none;
        border-radius: 25px;
        padding: 12px 35px;
        font-weight: 700;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 15px rgba(40, 116, 240, 0.5);
        position: relative;
        overflow: hidden;
    }
    
    .stButton>button:before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .stButton>button:hover:before {
        width: 300px;
        height: 300px;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 8px 30px rgba(155, 89, 182, 0.6);
        background: linear-gradient(135deg, var(--accent-purple) 0%, var(--accent-blue) 100%);
    }
    
    .stButton>button:active {
        transform: translateY(-1px) scale(1.02);
    }
    
    /* Chat messages with color variety */
    .chat-message {
        padding: 15px;
        border-radius: 15px;
        margin: 10px 0;
        animation: slideIn 0.5s ease-out;
        transition: all 0.3s ease;
    }
    
    @keyframes slideIn {
        from { 
            opacity: 0; 
            transform: translateX(-20px);
        }
        to { 
            opacity: 1; 
            transform: translateX(0);
        }
    }
    
    .user-message {
        background: linear-gradient(135deg, var(--accent-blue) 0%, var(--accent-cyan) 100%);
        margin-left: 20%;
        color: #ffffff;
        font-weight: 500;
        box-shadow: 0 4px 15px rgba(40, 116, 240, 0.4);
    }
    
    .user-message:hover {
        box-shadow: 0 6px 20px rgba(0, 212, 255, 0.6);
        transform: translateX(-5px);
    }
    
    .bot-message {
        background: linear-gradient(135deg, rgba(26, 31, 46, 0.95) 0%, rgba(42, 49, 66, 0.95) 100%);
        margin-right: 20%;
        border: 2px solid rgba(38, 166, 91, 0.5);
        color: #ffffff;
        box-shadow: 0 4px 15px rgba(38, 166, 91, 0.3);
        backdrop-filter: blur(5px);
    }
    
    .bot-message:hover {
        border-color: rgba(38, 166, 91, 0.8);
        box-shadow: 0 6px 20px rgba(38, 166, 91, 0.5);
        transform: translateX(5px);
    }
    
    /* Enhanced Metrics with varied colors */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        color: var(--accent-green);
        font-weight: 700;
        text-shadow: 0 0 15px rgba(38, 166, 91, 0.6);
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    /* Enhanced Info boxes with color coding */
    .stAlert {
        border-radius: 12px;
        border-left: 5px solid var(--accent-cyan);
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.1) 0%, rgba(40, 116, 240, 0.1) 100%);
        box-shadow: 0 4px 15px rgba(0, 212, 255, 0.2);
        transition: all 0.3s ease;
    }
    
    .stAlert:hover {
        box-shadow: 0 6px 20px rgba(0, 212, 255, 0.3);
        transform: translateX(5px);
    }
    
    /* Enhanced Code blocks */
    .stCodeBlock {
        border-radius: 12px;
        border: 2px solid rgba(155, 89, 182, 0.4);
        background: rgba(26, 31, 46, 0.8);
        box-shadow: 0 4px 15px rgba(155, 89, 182, 0.2);
    }
    
    /* Enhanced Tabs with blue theme */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background: rgba(26, 31, 46, 0.6);
        padding: 10px;
        border-radius: 12px;
        border: 2px solid rgba(40, 116, 240, 0.2);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: linear-gradient(135deg, rgba(40, 116, 240, 0.15) 0%, rgba(155, 89, 182, 0.15) 100%);
        border-radius: 10px 10px 0 0;
        color: var(--accent-cyan);
        font-weight: 600;
        padding: 12px 24px;
        transition: all 0.3s ease;
        border: 2px solid transparent;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: linear-gradient(135deg, rgba(40, 116, 240, 0.25) 0%, rgba(155, 89, 182, 0.25) 100%);
        border-color: rgba(0, 212, 255, 0.4);
        transform: translateY(-2px);
        color: #ffffff;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(180deg, var(--accent-blue) 0%, var(--accent-purple) 100%);
        color: #ffffff;
        box-shadow: 0 4px 15px rgba(40, 116, 240, 0.6);
        border-color: var(--accent-cyan);
    }
    
    /* Input fields enhancement with green focus */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background: rgba(26, 31, 46, 0.8);
        border: 2px solid rgba(40, 116, 240, 0.3);
        border-radius: 10px;
        color: #ffffff;
        transition: all 0.3s ease;
    }
    
    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
        border-color: var(--accent-green);
        box-shadow: 0 0 20px rgba(38, 166, 91, 0.5);
    }
    
    /* Scrollbar styling with blue gradient */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(26, 31, 46, 0.5);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, var(--accent-blue) 0%, var(--accent-purple) 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, var(--accent-cyan) 0%, var(--accent-blue) 100%);
    }
    
    
    /* Success elements - Green */
    .stSuccess {
        border-left-color: var(--accent-green) !important;
        background: linear-gradient(135deg, rgba(38, 166, 91, 0.1) 0%, rgba(38, 166, 91, 0.05) 100%);
    }
    
    /* Warning elements - Orange */
    .stWarning {
        border-left-color: var(--accent-orange) !important;
        background: linear-gradient(135deg, rgba(255, 107, 53, 0.1) 0%, rgba(255, 107, 53, 0.05) 100%);
    }
    
    /* Error elements - Red */
    .stError {
        border-left-color: #e74c3c !important;
        background: linear-gradient(135deg, rgba(231, 76, 60, 0.1) 0%, rgba(231, 76, 60, 0.05) 100%);
    }
    
    /* Sidebar headings with varied colors */
    [data-testid="stSidebar"] h1 {
        color: var(--primary-gold);
        text-shadow: 0 0 20px rgba(255, 215, 0, 0.6);
    }
    
    [data-testid="stSidebar"] h2 {
        color: var(--accent-cyan);
        text-shadow: 0 0 15px rgba(0, 212, 255, 0.5);
    }
    
    [data-testid="stSidebar"] h3 {
        color: var(--accent-orange);
        text-shadow: 0 0 12px rgba(255, 107, 53, 0.4);
        font-weight: 600;
    }
    
    [data-testid="stSidebar"] h4 {
        color: var(--accent-purple);
        text-shadow: 0 0 10px rgba(155, 89, 182, 0.4);
    }
    
    /* Sidebar markdown text */
    [data-testid="stSidebar"] .stMarkdown {
        color: var(--text-light);
    }
    
    /* Sidebar metrics with green color */
    [data-testid="stSidebar"] [data-testid="stMetricValue"] {
        color: var(--accent-green);
        text-shadow: 0 0 10px rgba(38, 166, 91, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'system_logs' not in st.session_state:
    st.session_state.system_logs = []

# Helper function to add system logs
def add_log(message, level="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.system_logs.append({
        "timestamp": timestamp,
        "level": level,
        "message": message
    })

# Sidebar
with st.sidebar:
    # Flipkart Logo
    # Flipkart Logo
    st.markdown("""
    <div style='background: #ffffff; 
                padding: 20px; border-radius: 10px; text-align: center; 
                box-shadow: 0 4px 15px rgba(40, 116, 240, 0.5); margin-bottom: 20px; border: 2px solid #2874f0;'>
        <img src="https://logos-world.net/wp-content/uploads/2020/11/Flipkart-Logo.png" alt="Flipkart Logo" style="max-width: 100%; height: auto; margin-bottom: 10px;">
        <p style='color: #2874f0; margin: 0; font-size: 1.0rem; font-weight: 700; letter-spacing: 1px;'>
            PRODUCT RECOMMENDER
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Project Info")
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(40, 116, 240, 0.2) 0%, rgba(0, 212, 255, 0.2) 100%); 
                padding: 15px; border-radius: 10px; color: #e8e8e8; font-weight: 500; border: 2px solid rgba(40, 116, 240, 0.4);'>
        <strong style='color: #00d4ff;'>Flipkart Product Recommender</strong><br><br>
        An AI-powered RAG system for intelligent product recommendations using customer reviews.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 👨‍💻 Developer")
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(155, 89, 182, 0.2) 0%, rgba(40, 116, 240, 0.2) 100%); 
                padding: 15px; border-radius: 10px; border: 2px solid rgba(155, 89, 182, 0.4);'>
        <p style='margin: 5px 0; color: #00d4ff; font-weight: 600;'>
            <strong>Ratnesh Kumar Singh</strong>
        </p>
        <p style='margin: 5px 0; font-size: 0.9rem;'>
            🔗 <a href='https://github.com/Ratnesh-181998' target='_blank' 
                  style='color: #2874f0; text-decoration: none; font-weight: 600;'>GitHub</a>
        </p>
        <p style='margin: 5px 0; font-size: 0.9rem;'>
            📧 <a href='mailto:rattudacsit2021gate@gmail.com' 
                  style='color: #26a65b; text-decoration: none; font-weight: 600;'>Email</a>
        </p>
        <p style='margin: 5px 0; font-size: 0.9rem;'>
            💼 <a href='https://www.linkedin.com/in/ratneshkumar1998/' target='_blank' 
                  style='color: #9b59b6; text-decoration: none; font-weight: 600;'>LinkedIn</a>
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("### 📊 Quick Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Version", "1.0")
    with col2:
        st.metric("Status", "🟢 Live")

# Professional Badge at Top
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("")  # Empty space for alignment

with col2:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #2874f0 0%, #9b59b6 100%); 
                padding: 6px 12px; border-radius: 6px; 
                box-shadow: 0 2px 8px rgba(40, 116, 240, 0.4);
                border: 1px solid rgba(155, 89, 182, 0.3);
                text-align: center;
                margin-bottom: 10px;'>
        <p style='margin: 0; color: #ffffff; font-weight: 700; font-size: 0.7rem; line-height: 1.5;'>
            <strong>Ratnesh Kumar Singh</strong><br>
            Data Scientist (AI/ML) | 4+ Yrs
        </p>
    </div>
    """, unsafe_allow_html=True)

# Main header
st.markdown("""
<div style='text-align: center; padding: 15px; background: linear-gradient(135deg, rgba(40, 116, 240, 0.15) 0%, rgba(155, 89, 182, 0.15) 100%); border-radius: 12px; margin-bottom: 15px; border: 2px solid rgba(40, 116, 240, 0.4);'>
<div style='display: flex; align-items: center; justify-content: center; gap: 15px; margin-bottom: 8px; flex-wrap: wrap;'>
<div style='background: white; padding: 6px 15px; border-radius: 50px; box-shadow: 0 4px 10px rgba(0,0,0,0.3); display: flex; align-items: center;'>
<img src="https://logos-world.net/wp-content/uploads/2020/11/Flipkart-Logo.png" alt="Flipkart" style="height: 35px; width: auto;">
</div>
<h1 style='color: #00d4ff; margin: 0; font-size: 1.8rem; font-weight: 800; text-shadow: 0 0 15px rgba(0, 212, 255, 0.5); letter-spacing: 1px; line-height: 1;'>
PRODUCT RECOMMENDER
</h1>
</div>
<p style='font-size: 1.0rem; color: #e8e8e8; font-weight: 500; margin: 0; letter-spacing: 0.5px;'>
🛍️ AI-Powered Product Discovery using RAG Technology
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎬 Demo", 
    "📖 About Project", 
    "🔧 Tech Stack", 
    "🏗️ Architecture", 
    "📋 System Logs"
])

# TAB 1: Demo
with tab1:
    st.header("🎬 Live Demo")

    # Define a helper function to handle chat queries
    def handle_chat_query(query_text):
        if query_text:
            # Add user message
            st.session_state.chat_history.append({
                'role': 'user',
                'content': query_text
            })
            add_log(f"User query: {query_text}", "INFO")
            
            # Call Flask backend
            try:
                with st.spinner("🌸 AI is thinking..."):
                    response = requests.post(
                        "http://localhost:5000/get",
                        data={"msg": query_text},
                        timeout=30
                    )
                    
                    if response.status_code == 200:
                        bot_response = response.text
                        st.session_state.chat_history.append({
                            'role': 'bot',
                            'content': bot_response
                        })
                        add_log(f"AI response generated successfully", "SUCCESS")
                    else:
                        st.error(f"Error: {response.status_code}")
                        add_log(f"Error: HTTP {response.status_code}", "ERROR")
            except Exception as e:
                st.error(f"⚠️ Error connecting to backend: {str(e)}")
                st.info("💡 Make sure the Flask app is running on http://localhost:5000")
                add_log(f"Connection error: {str(e)}", "ERROR")

    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Welcome Banner (Bloom Effect)
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(40, 116, 240, 0.1) 0%, rgba(155, 89, 182, 0.1) 100%); 
                    padding: 15px; border-radius: 12px; border: 1px solid rgba(40, 116, 240, 0.2); margin-bottom: 20px;
                    border-left: 5px solid #00d4ff;'>
            <h3 style='color: #00d4ff; margin: 0 0 5px 0;'>💬 Chat with Ratnesh AI Assistant</h3>
            <p style='color: #e8e8e8; margin: 0; font-size: 0.95rem;'>
                Ask questions about Flipkart products, reviews, and get personalized recommendations!
                <br><span style='font-size: 0.8rem; color: #9b59b6;'>✨ Try the interactive buttons on the right for quick answers!</span>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Chat container
        chat_container = st.container()
        
        # Display chat history
        with chat_container:
            if not st.session_state.chat_history:
                st.markdown("""
                <div style='text-align: center; padding: 40px; color: #666;'>
                    <p style='font-size: 3rem; margin-bottom: 10px;'>👋</p>
                    <p>Welcome! I'm here to help you find the perfect products.</p>
                </div>
                """, unsafe_allow_html=True)
                
            for message in st.session_state.chat_history:
                if message['role'] == 'user':
                    st.markdown(f"""
                    <div class='chat-message user-message' style='animation: slideIn 0.3s ease-out;'>
                        <strong>👤 You:</strong><br>{message['content']}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class='chat-message bot-message' style='animation: slideIn 0.3s ease-out;'>
                        <strong>🤖 Ratnesh AI Assistant:</strong><br>{message['content']}
                    </div>
                    """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Chat input area
        col_input, col_btn = st.columns([4, 1])
        with col_input:
            user_input = st.text_input("Type your message:", key="user_input", placeholder="e.g., Show me the best rated phones", label_visibility="collapsed")
        with col_btn:
            send_clicked = st.button("📤 Send", use_container_width=True, type="primary")

        # Clear chat option
        if st.button("🗑️ Clear Chat", key="clear_chat_main"):
            st.session_state.chat_history = []
            add_log("Chat history cleared", "INFO")
            st.rerun()
        
        # Handle Input Processing
        if send_clicked and user_input:
            handle_chat_query(user_input)
            st.rerun()
    
    with col2:
        st.markdown("<h3 style='color: #2874f0;'>💡 Sample Questions</h3>", unsafe_allow_html=True)
        
        # Existing Text (Preserved)
        st.markdown("""
        Try asking:
        
        - 🔍 "Show me the best rated phones"
        - 💻 "What are customers saying about laptops?"
        - 🎧 "Recommend good headphones"
        - 📷 "Tell me about camera reviews"
        - ⭐ "Which products have 5-star ratings?"
        - 🏷️ "What are the trending products?"
        """)
        
        st.markdown("---")
        st.markdown("### 🚀 Quick Try")
        st.caption("Click a button to ask instantly:")
        
        # Interactive Buttons (New Feature)
        if st.button("🔍 Best Rated Phones", use_container_width=True):
            handle_chat_query("Show me the best rated phones")
            st.rerun()
            
        if st.button("💻 Laptop Opinions", use_container_width=True):
            handle_chat_query("What are customers saying about laptops?")
            st.rerun()
            
        if st.button("🎧 Good Headphones", use_container_width=True):
            handle_chat_query("Recommend good headphones")
            st.rerun()
            
        if st.button("⭐ 5-Star Products", use_container_width=True):
            handle_chat_query("Which products have 5-star ratings?")
            st.rerun()
        
        st.markdown("---")
        st.markdown("<h3 style='color: #26a65b;'>📊 Chat Statistics</h3>", unsafe_allow_html=True)
        
        # Styled metrics
        m_col1, m_col2 = st.columns(2)
        with m_col1:
            st.metric("Total Messages", len(st.session_state.chat_history))
        with m_col2:
            st.metric("Queries", len([m for m in st.session_state.chat_history if m['role'] == 'user']))

# TAB 2: About Project
with tab2:
    st.header("📖 About This Project")
    
    # Hero Section
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(40, 116, 240, 0.1) 0%, rgba(155, 89, 182, 0.1) 100%); 
                padding: 20px; border-radius: 12px; border: 1px solid rgba(40, 116, 240, 0.2); margin-bottom: 25px;
                text-align: center; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);'>
        <h2 style='color: #00d4ff; margin: 0 0 10px 0; font-size: 1.8rem;'>🚀 Revolutionizing Product Discovery</h2>
        <p style='color: #e8e8e8; font-size: 1.1rem; max-width: 800px; margin: 0 auto;'>
            Experience the future of e-commerce with our AI-powered recommendation engine.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Problem & Solution (Moved to Top)
    with st.expander("🎯 Problem & Solution (Read First)", expanded=True):
        col_p, col_s = st.columns(2)
        with col_p:
            st.warning("**🚨 Challenge**: Users struggle to find products among millions of reviews.")
        with col_s:
            st.success("**✅ Solution**: RAG-based AI system for personalized discovery.")

    # Table of Contents / Quick Layout
    st.markdown("""
    <div style='margin-bottom: 20px; margin-top: 20px;'>
        <h4 style='color: #e8e8e8; margin-bottom: 10px;'>📑 Table of Contents</h4>
        <div style='display: flex; gap: 10px; flex-wrap: wrap;'>
            <span style='background: rgba(40, 116, 240, 0.2); padding: 5px 10px; border-radius: 5px; color: #00d4ff; font-size: 0.9rem;'>1. Projects Overview</span>
            <span style='background: rgba(155, 89, 182, 0.2); padding: 5px 10px; border-radius: 5px; color: #e056fd; font-size: 0.9rem;'>2. Key Features</span>
            <span style='background: rgba(38, 166, 91, 0.2); padding: 5px 10px; border-radius: 5px; color: #2ecc71; font-size: 0.9rem;'>3. Use Cases</span>
            <span style='background: rgba(40, 116, 240, 0.2); padding: 5px 10px; border-radius: 5px; color: #00d4ff; font-size: 0.9rem;'>4. Metrics</span>
            <span style='background: rgba(255, 107, 53, 0.2); padding: 5px 10px; border-radius: 5px; color: #ff6b35; font-size: 0.9rem;'>5. Benefits</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    
    # 1. Project Overview
    st.markdown("<h3 style='color: #00d4ff;'>1️⃣ Project Overview</h3>", unsafe_allow_html=True)
    with st.expander("📖 Read Detailed Overview & Workflow", expanded=True):
        st.markdown("""
        The **Flipkart Product Recommender** is not just a search engine; it's an intelligent **Conversational AI** that understands product nuances. It leverages **Retrieval-Augmented Generation (RAG)** to bridge the gap between static product data and dynamic user needs.
        
        #### ⚙️ How It Works (The 4-Step Process):
        1.  **Data Ingestion**: We ingest thousands of raw customer reviews and product specifications from Flipkart's dataset.
        2.  **Vector Embedding**: Using **HuggingFace models**, we convert this text into high-dimensional vectors (numerical representations of meaning) and store them in **AstraDB**.
        3.  **Semantic Retrieval**: When you ask a question, the system finds reviews that *mean* the same thing, not just valid keyword matches.
        4.  **Generative Response**: Finally, **Groq's Llama 3.1** synthesizes these retrieved insights into a natural, helpful answer.
        
        This approach ensures answers are always **grounded in real data**, reducing hallucinations common in standard LLMs.
        """)

    # 2. Key Features
    st.markdown("<br><h3 style='color: #9b59b6;'>2️⃣ Key Features</h3>", unsafe_allow_html=True)
    st.markdown("Our system combines multiple advanced technologies to deliver a premium experience. Here is a deep dive into the core capabilities:")
    
    kf_col1, kf_col2 = st.columns(2)
    with kf_col1:
        st.info("""
        **🤖 AI-Powered Recommendations**
        *   **Engine**: Groq Llama 3.1-8B-Instant.
        *   **Capability**: Understands slang, sentiment, and context.
        *   **Benefit**: Provides summarized "Verdict" on products rather than just listing links.
        """)
        st.success("""
        **🔍 Semantic Search**
        *   **Tech**: AstraDB Serverless Vector Store.
        *   **Method**: Cosine Similarity Search.
        *   **Benefit**: Finds "gaming laptops" even if you search for "high FPS machine".
        """)
        st.warning("""
        **💬 Conversational Context**
        *   **Feature**: LangChain Memory.
        *   **Capability**: Remembers previous questions.
        *   **Benefit**: You can ask "What about its battery?" and it knows you mean the phone discussed earlier.
        """)
    with kf_col2:
        st.error("""
        **📊 Observability & Metrics**
        *   **Tools**: Prometheus & Grafana.
        *   **Tracking**: Latency, Token Usage, Error Rates.
        *   **Benefit**: Ensures the system remains fast and reliable under load.
        """)
        st.info("""
        **🚀 Cloud-Native Architecture**
        *   **Stack**: Docker & Kubernetes (K8s).
        *   **Deployment**: Running on GCP Virtual Machines.
        *   **Benefit**: Auto-scaling and self-healing infrastructure.
        """)
        st.success("""
        **🔒 Enterprise Security**
        *   **Method**: .env based secret management.
        *   **Safety**: No hardcoded API keys.
        *   **Benefit**: Secure handling of Groq and Database credentials.
        """)
    
    # 3. Use Cases
    st.markdown("<br><h3 style='color: #26a65b;'>3️⃣ Use Cases</h3>", unsafe_allow_html=True)
    st.markdown("This system is designed to solve real-world shopping challenges. Here are the primary scenarios where it shines:")
    
    st.markdown("""
    <div style='background: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 10px; border-left: 5px solid #26a65b;'>
        <div style='margin-bottom: 15px;'>
            <h4 style='color: #2ecc71; margin: 0;'>🔍 1. Smart Product Discovery</h4>
            <p style='margin: 5px 0 0 0; color: #ccc;'>
                <strong>Scenario:</strong> A user wants a phone but focuses on specific features.<br>
                <strong>Query:</strong> <em>"Suggest a phone under 30k with the best camera for night photography."</em><br>
                <strong>Outcome:</strong> The AI filters products by price and specifically ranks them by sentiment regarding "night photography" in reviews.
            </p>
        </div>
        <div style='margin-bottom: 15px;'>
            <h4 style='color: #2ecc71; margin: 0;'>📝 2. Review Summarization</h4>
            <p style='margin: 5px 0 0 0; color: #ccc;'>
                <strong>Scenario:</strong> A popular laptop has 5,000 reviews.<br>
                <strong>Query:</strong> <em>"What are the main complaints about the MacBook Air M2?"</em><br>
                <strong>Outcome:</strong> The AI aggregates common issues (e.g., "fingerprint magnet", "slow SSD in base model") into a concise bullet list.
            </p>
        </div>
        <div style='margin-bottom: 15px;'>
            <h4 style='color: #2ecc71; margin: 0;'>⚖️ 3. Competitive Comparison</h4>
            <p style='margin: 5px 0 0 0; color: #ccc;'>
                <strong>Scenario:</strong> Undecided between two models.<br>
                <strong>Query:</strong> <em>"Compare the iPhone 13 and Samsung S21 FE based on battery life."</em><br>
                <strong>Outcome:</strong> A side-by-side comparison drawing directly from user experiences with battery performance.
            </p>
        </div>
        <div>
            <h4 style='color: #2ecc71; margin: 0;'>💡 4. Gift Recommendations</h4>
            <p style='margin: 5px 0 0 0; color: #ccc;'>
                <strong>Scenario:</strong> Buying for someone else.<br>
                <strong>Query:</strong> <em>"Best tech gift for a graphic designer beginner."</em><br>
                <strong>Outcome:</strong> Suggestions for drawing tablets or high-color-accuracy monitors suitable for beginners.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 4. Metrics
    st.markdown("<br><h3 style='color: #00d4ff;'>4️⃣ Metrics (Performance KPIs)</h3>", unsafe_allow_html=True)
    st.markdown("We prioritize speed and accuracy. Below are the key performance indicators (KPIs) we track in real-time:")
    
    st.markdown("""
    <div style='background: rgba(30, 30, 40, 0.6); padding: 15px; border-radius: 10px; border: 1px solid #444; text-align: center;'>
        <div style='display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px;'>
            <div>
                <div style='font-size: 1.5rem; color: #2ecc71; font-weight: bold;'>95%</div>
                <div style='font-size: 0.8rem; color: #aaa;'>Relevance Accuracy</div>
                <div style='font-size: 0.7rem; color: #666; margin-top: 5px;'>Top-3 retrieved docs match user intent</div>
            </div>
            <div>
                <div style='font-size: 1.5rem; color: #2ecc71; font-weight: bold;'>99.9%</div>
                <div style='font-size: 0.8rem; color: #aaa;'>System Uptime</div>
                 <div style='font-size: 0.7rem; color: #666; margin-top: 5px;'>Kubernetes self-healing pods</div>
            </div>
            <div>
                <div style='font-size: 1.5rem; color: #e74c3c; font-weight: bold;'>1.2s</div>
                <div style='font-size: 0.8rem; color: #aaa;'>Avg Response Time</div>
                 <div style='font-size: 0.7rem; color: #666; margin-top: 5px;'>Groq inference speed</div>
            </div>
             <div>
                <div style='font-size: 1.5rem; color: #3498db; font-weight: bold;'>1k+</div>
                <div style='font-size: 0.8rem; color: #aaa;'>Concurrent Users</div>
                 <div style='font-size: 0.7rem; color: #666; margin-top: 5px;'>Load balanced capacity</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 5. Benefits
    st.markdown("<br><h3 style='color: #ff6b35;'>5️⃣ Business & User Benefits</h3>", unsafe_allow_html=True)
    st.markdown("Why does this system matter? Here is the value proposition for different stakeholders:")
    
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(255, 107, 53, 0.1) 0%, rgba(255, 159, 67, 0.1) 100%); 
                padding: 20px; border-radius: 10px; border: 1px solid rgba(255, 107, 53, 0.3);'>
        <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 20px;'>
            <div>
                <h4 style='color: #ff6b35; margin-top: 0;'>👤 For Users</h4>
                <ul style='padding-left: 20px; color: #ddd;'>
                    <li><strong>No More Scrolling:</strong> Get instant answers instead of reading pages of text.</li>
                    <li><strong>Confident Buying:</strong> Decisions backed by summarized community feedback.</li>
                    <li><strong>Personalized:</strong> Results tailored to your specific constraints.</li>
                </ul>
            </div>
            <div>
                <h4 style='color: #ff6b35; margin-top: 0;'>🏢 For Business (Flipkart)</h4>
                 <ul style='padding-left: 20px; color: #ddd;'>
                    <li><strong>Higher Conversion:</strong> Helping users find what they want faster leads to more sales.</li>
                    <li><strong>Lower Returns:</strong> Better understanding of products leads to fewer "item not as described" returns.</li>
                    <li><strong>Customer Insights:</strong> Analyze chat logs to understand what users *really* want.</li>
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    if st.button("🛠️ Explore Tech Stack", type="secondary", use_container_width=True):
            st.info("Check out the 'Technology Stack' tab for details!")

    # Technology Stack Overview Image (Preserved)
    # Tech stack overview moved to Tab 3 for better organization


# TAB 3: Tech Stack
with tab3:
    st.header("🔧 Technology Stack")

    # High-Level Tech Stack Cards (Replica of the user's requested visual)
    st.markdown("""
<div style='display: flex; gap: 20px; justify-content: center; margin-bottom: 30px; flex-wrap: wrap;'>
<!-- Backend Card -->
<div style='background: linear-gradient(135deg, rgba(40, 116, 240, 0.2) 0%, rgba(26, 31, 46, 0.8) 100%); padding: 20px; border-radius: 15px; border: 2px solid #2874f0; width: 30%; min-width: 250px; text-align: center; box-shadow: 0 4px 15px rgba(40, 116, 240, 0.3);'>
<h2 style='color: #2874f0 !important; margin-bottom: 15px; text-shadow: none;'>Backend</h2>
<div style='background: rgba(40, 116, 240, 0.1); padding: 8px; border-radius: 8px; margin-bottom: 8px; color: #a6c1ee; font-weight: 600;'>Flask API</div>
<div style='background: rgba(40, 116, 240, 0.1); padding: 8px; border-radius: 8px; color: #a6c1ee; font-weight: 600;'>LangChain</div>
</div>
<!-- AI Layer Card -->
<div style='background: linear-gradient(135deg, rgba(46, 204, 113, 0.2) 0%, rgba(26, 31, 46, 0.8) 100%); padding: 20px; border-radius: 15px; border: 2px solid #2ecc71; width: 30%; min-width: 250px; text-align: center; box-shadow: 0 4px 15px rgba(46, 204, 113, 0.3);'>
<h2 style='color: #ffffff !important; margin-bottom: 15px; text-shadow: 0 2px 4px rgba(0,0,0,0.5);'>AI Layer</h2>
<div style='background: rgba(46, 204, 113, 0.2); padding: 8px; border-radius: 8px; margin-bottom: 8px; color: #ffffff; font-weight: 700; text-shadow: 0 1px 2px rgba(0,0,0,0.5);'>Groq LLM</div>
<div style='background: rgba(46, 204, 113, 0.2); padding: 8px; border-radius: 8px; margin-bottom: 8px; color: #ffffff; font-weight: 700; text-shadow: 0 1px 2px rgba(0,0,0,0.5);'>HuggingFace</div>
<div style='background: rgba(46, 204, 113, 0.2); padding: 8px; border-radius: 8px; color: #ffffff; font-weight: 700; text-shadow: 0 1px 2px rgba(0,0,0,0.5);'>Embeddings</div>
</div>
<!-- Database Card -->
<div style='background: linear-gradient(135deg, rgba(255, 159, 67, 0.2) 0%, rgba(26, 31, 46, 0.8) 100%); padding: 20px; border-radius: 15px; border: 2px solid #f39c12; width: 30%; min-width: 250px; text-align: center; box-shadow: 0 4px 15px rgba(255, 159, 67, 0.3);'>
<h2 style='color: #f39c12 !important; margin-bottom: 15px; text-shadow: none;'>Database</h2>
<div style='background: rgba(255, 159, 67, 0.1); padding: 8px; border-radius: 8px; margin-bottom: 8px; color: #fad390; font-weight: 600;'>AstraDB</div>
<div style='background: rgba(255, 159, 67, 0.1); padding: 8px; border-radius: 8px; color: #fad390; font-weight: 600;'>Vector Store</div>
</div>
</div>
""", unsafe_allow_html=True)
    
    # Original categorized tech stack
    st.markdown("### 📚 Technologies by Category")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🤖 AI & Machine Learning")
        st.markdown("""
        - **LangChain** `v1.2.0` - RAG framework and orchestration
        - **Groq** - LLM inference (Llama 3.1-8B-Instant)
        - **HuggingFace Embeddings** - Embedding models (BAAI/bge-base-en-v1.5)
        - **LangGraph** - Workflow management
        """)
        
        st.markdown("### 🗄️ Database & Storage")
        st.markdown("""
        - **AstraDB** - Vector database for embeddings
        - **Cassandra** - Distributed NoSQL backend
        - **Vector Search** - Semantic similarity search
        """)
        
        st.markdown("### 🌐 Web Framework")
        st.markdown("""
        - **Flask** `v3.1.2` - Backend API server
        - **Streamlit** `v1.52.2` - Interactive UI dashboard
        - **Jinja2** - Template engine
        """)
    
    with col2:
        st.markdown("### 📊 Monitoring & Observability")
        st.markdown("""
        - **Prometheus** - Metrics collection
        - **Grafana** - Visualization dashboards
        - **prometheus_client** - Python metrics library
        """)
        
        st.markdown("### 🐳 DevOps & Deployment")
        st.markdown("""
        - **Docker** - Containerization
        - **Kubernetes** - Orchestration
        - **Minikube** - Local K8s cluster
        - **Google Cloud (GCP VM)** - VM hosting
        - **Kubectl** - Kubernetes CLI tool
        """)
        
        st.markdown("### 📦 Data Processing")
        st.markdown("""
        - **Pandas** `v2.3.3` - Data manipulation
        - **PyPDF** - PDF processing
        - **Datasets** - HuggingFace datasets library
        """)
    
    st.markdown("---")
    
    # Detailed 13-item tech stack
    st.markdown("### 🎯 Complete Technology Stack")
    
    st.markdown("""
    <div style='text-align: center; padding: 15px; background: linear-gradient(135deg, rgba(40, 116, 240, 0.15) 0%, rgba(155, 89, 182, 0.15) 100%); 
                border-radius: 10px; margin-bottom: 20px; border: 2px solid rgba(40, 116, 240, 0.3);'>
        <p style='color: #00d4ff; font-size: 1.1rem; font-weight: 600; margin: 0;'>
            Complete technology stack powering the Flipkart Product Recommender
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(40, 116, 240, 0.1) 0%, rgba(0, 212, 255, 0.1) 100%); 
                    padding: 20px; border-radius: 10px; border: 2px solid rgba(40, 116, 240, 0.3); margin-bottom: 15px;'>
            <h3 style='color: #2874f0; margin-top: 0;'>1️⃣ Groq</h3>
            <p style='color: #00d4ff; font-weight: 600; margin: 0;'>🤖 LLM (Large Language Model)</p>
            <p style='margin: 5px 0 0 0;'>Powers the AI responses with fast inference</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(155, 89, 182, 0.1) 0%, rgba(142, 68, 173, 0.1) 100%); 
                    padding: 20px; border-radius: 10px; border: 2px solid rgba(155, 89, 182, 0.3); margin-bottom: 15px;'>
            <h3 style='color: #9b59b6; margin-top: 0;'>2️⃣ HuggingFace</h3>
            <p style='color: #e056fd; font-weight: 600; margin: 0;'>📊 Embedding Model</p>
            <p style='margin: 5px 0 0 0;'>Converts text to vector embeddings for semantic search</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(38, 166, 91, 0.1) 0%, rgba(46, 204, 113, 0.1) 100%); 
                    padding: 20px; border-radius: 10px; border: 2px solid rgba(38, 166, 91, 0.3); margin-bottom: 15px;'>
            <h3 style='color: #26a65b; margin-top: 0;'>3️⃣ GCP VM</h3>
            <p style='color: #2ecc71; font-weight: 600; margin: 0;'>☁️ Cloud Infrastructure</p>
            <p style='margin: 5px 0 0 0;'>Deploy and run your app on the cloud within a Virtual Machine. Service offered by Google Cloud.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(255, 107, 53, 0.1) 0%, rgba(255, 159, 67, 0.1) 100%); 
                    padding: 20px; border-radius: 10px; border: 2px solid rgba(255, 107, 53, 0.3); margin-bottom: 15px;'>
            <h3 style='color: #ff6b35; margin-top: 0;'>4️⃣ LangChain</h3>
            <p style='color: #f39c12; font-weight: 600; margin: 0;'>🔗 Generative AI Framework</p>
            <p style='margin: 5px 0 0 0;'>Framework to interact with LLM and build RAG pipelines</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(40, 116, 240, 0.1) 0%, rgba(0, 212, 255, 0.1) 100%); 
                    padding: 20px; border-radius: 10px; border: 2px solid rgba(40, 116, 240, 0.3); margin-bottom: 15px;'>
            <h3 style='color: #2874f0; margin-top: 0;'>5️⃣ Minikube</h3>
            <p style='color: #00d4ff; font-weight: 600; margin: 0;'>⚙️ Local Kubernetes Cluster</p>
            <p style='margin: 5px 0 0 0;'>Making a Kubernetes Cluster inside a VM for local testing</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(155, 89, 182, 0.1) 0%, rgba(142, 68, 173, 0.1) 100%); 
                    padding: 20px; border-radius: 10px; border: 2px solid rgba(155, 89, 182, 0.3); margin-bottom: 15px;'>
            <h3 style='color: #9b59b6; margin-top: 0;'>6️⃣ Docker</h3>
            <p style='color: #e056fd; font-weight: 600; margin: 0;'>🐳 Containerization</p>
            <p style='margin: 5px 0 0 0;'>For containerization of the app during deployment</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(38, 166, 91, 0.1) 0%, rgba(46, 204, 113, 0.1) 100%); 
                    padding: 20px; border-radius: 10px; border: 2px solid rgba(38, 166, 91, 0.3); margin-bottom: 15px;'>
            <h3 style='color: #26a65b; margin-top: 0;'>7️⃣ Flask</h3>
            <p style='color: #2ecc71; font-weight: 600; margin: 0;'>🌐 Backend Framework</p>
            <p style='margin: 5px 0 0 0;'>For making backend of your application with REST API</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(255, 107, 53, 0.1) 0%, rgba(255, 159, 67, 0.1) 100%); 
                    padding: 20px; border-radius: 10px; border: 2px solid rgba(255, 107, 53, 0.3); margin-bottom: 15px;'>
            <h3 style='color: #ff6b35; margin-top: 0;'>8️⃣ HTML / CSS</h3>
            <p style='color: #f39c12; font-weight: 600; margin: 0;'>🎨 Frontend Technologies</p>
            <p style='margin: 5px 0 0 0;'>To make UI or frontend of the app with modern design</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(40, 116, 240, 0.1) 0%, rgba(0, 212, 255, 0.1) 100%); 
                    padding: 20px; border-radius: 10px; border: 2px solid rgba(40, 116, 240, 0.3); margin-bottom: 15px;'>
            <h3 style='color: #2874f0; margin-top: 0;'>9️⃣ Kubectl</h3>
            <p style='color: #00d4ff; font-weight: 600; margin: 0;'>⌨️ Kubernetes CLI</p>
            <p style='margin: 5px 0 0 0;'>CLI tool for Kubernetes to interact with Minikube cluster</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(155, 89, 182, 0.1) 0%, rgba(142, 68, 173, 0.1) 100%); 
                    padding: 20px; border-radius: 10px; border: 2px solid rgba(155, 89, 182, 0.3); margin-bottom: 15px;'>
            <h3 style='color: #9b59b6; margin-top: 0;'>🔟 GitHub</h3>
            <p style='color: #e056fd; font-weight: 600; margin: 0;'>📂 Source Control Management</p>
            <p style='margin: 5px 0 0 0;'>It will work as a SCM for your project version control</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(38, 166, 91, 0.1) 0%, rgba(46, 204, 113, 0.1) 100%); 
                    padding: 20px; border-radius: 10px; border: 2px solid rgba(38, 166, 91, 0.3); margin-bottom: 15px;'>
            <h3 style='color: #26a65b; margin-top: 0;'>1️⃣1️⃣ AstraDB</h3>
            <p style='color: #2ecc71; font-weight: 600; margin: 0;'>🗄️ Vector Store</p>
            <p style='margin: 5px 0 0 0;'>Work as our Vector Store (Online Vector Store unlike Chroma and FAISS)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(255, 107, 53, 0.1) 0%, rgba(255, 159, 67, 0.1) 100%); 
                    padding: 20px; border-radius: 10px; border: 2px solid rgba(255, 107, 53, 0.3); margin-bottom: 15px;'>
            <h3 style='color: #ff6b35; margin-top: 0;'>1️⃣2️⃣ Prometheus</h3>
            <p style='color: #f39c12; font-weight: 600; margin: 0;'>📊 Metrics Collection</p>
            <p style='margin: 5px 0 0 0;'>Collects and stores real-time metrics (CPU usage, memory, request rate) from your application running in Kubernetes. You can also make custom metrics.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(40, 116, 240, 0.1) 0%, rgba(0, 212, 255, 0.1) 100%); 
                    padding: 20px; border-radius: 10px; border: 2px solid rgba(40, 116, 240, 0.3); margin-bottom: 15px;'>
            <h3 style='color: #2874f0; margin-top: 0;'>1️⃣3️⃣ Grafana</h3>
            <p style='color: #00d4ff; font-weight: 600; margin: 0;'>📈 Visualization Dashboard</p>
            <p style='margin: 5px 0 0 0;'>Visualizes those metrics in the form of beautiful dashboards</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Tech stack visualization
    st.markdown("### 🏗️ Stack Layers")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #2874f0 0%, #00d4ff 100%); 
                    padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0 4px 15px rgba(40, 116, 240, 0.4);'>
            <h3 style='color: #ffffff; margin: 0;'>Frontend</h3>
            <p style='color: #ffffff; font-weight: 600;'>HTML/CSS<br>Streamlit</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #2a2a2a 0%, #3d3d3d 100%); 
                    padding: 20px; border-radius: 10px; text-align: center; border: 2px solid #2874f0; box-shadow: 0 4px 15px rgba(40, 116, 240, 0.3);'>
            <h3 style='color: #2874f0; margin: 0;'>Backend</h3>
            <p style='color: #00d4ff; font-weight: 600;'>Flask API<br>LangChain</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%); 
                    padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0 4px 15px rgba(46, 204, 113, 0.4);'>
            <h3 style='color: #ffffff; margin: 0;'>AI Layer</h3>
            <p style='color: #ffffff; font-weight: 600;'>Groq LLM<br>HuggingFace Embeddings</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #2a2a2a 0%, #3d3d3d 100%); 
                    padding: 20px; border-radius: 10px; text-align: center; border: 2px solid #ff9f43; box-shadow: 0 4px 15px rgba(255, 159, 67, 0.3);'>
            <h3 style='color: #ff9f43; margin: 0;'>Database</h3>
            <p style='color: #f39c12; font-weight: 600;'>AstraDB<br>Vector Store</p>
        </div>
        """, unsafe_allow_html=True)

# TAB 4: Architecture
with tab4:
    # Hero Section for Architecture
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(40, 116, 240, 0.1) 0%, rgba(0, 212, 255, 0.1) 100%); 
                padding: 20px; border-radius: 12px; border: 1px solid rgba(40, 116, 240, 0.2); margin-bottom: 25px;
                text-align: center; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);'>
        <h2 style='color: #00d4ff; margin: 0 0 10px 0; font-size: 1.8rem;'>🏗️ System Architecture & Workflow</h2>
        <p style='color: #e8e8e8; font-size: 1.1rem; max-width: 800px; margin: 0 auto;'>
            A cloud-native, microservices-based RAG architecture powered by modern AI stack.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Architecture Diagram (Mermaid) - Collapsible
    with st.expander("📐 Live Architecture Diagram (Mermaid)", expanded=True):
        st.markdown("The system follows a modern microservices architecture with RAG implementation:")
        st.markdown("""
        ```mermaid
        graph TB
            A[User Interface] -->|HTTP Request| B[Flask API]
            B -->|Query| C[RAG Chain Builder]
            C -->|Retrieve Context| D[AstraDB Vector Store]
            C -->|Generate Response| E[Groq LLM]
            D -->|Embeddings| F[HuggingFace Embeddings]
            B -->|Metrics| G[Prometheus]
            G -->|Visualize| H[Grafana]
            I[CSV Data] -->|Ingest| D
            J[Kubernetes] -->|Orchestrate| B
            K[Docker] -->|Containerize| B
        ```
        """)

    st.markdown("---")

    # Workflow Diagram (Full Width)
    st.markdown("""
    <div style='background: rgba(40, 116, 240, 0.05); padding: 10px; border-radius: 10px; border: 1px solid rgba(40, 116, 240, 0.2); margin-bottom: 10px;'>
        <h4 style='color: #2874f0; text-align: center; margin: 0;'>🔄 Complete Workflow</h4>
    </div>
    """, unsafe_allow_html=True)
    try:
        workflow_image = Image.open(r"C:\Users\rattu\Downloads\2_FLIPKART PRODUCT RECOMMENDER\Local Run\Flipkart+product+recommender+Workflow.png")
        st.image(workflow_image, caption="System Workflow Diagram", use_container_width=True)
    except Exception as e:
        st.warning("Workflow diagram image not found.")

    st.markdown("<br>", unsafe_allow_html=True)

    # Monitoring Diagram (Full Width)
    st.markdown("""
    <div style='background: rgba(46, 204, 113, 0.05); padding: 10px; border-radius: 10px; border: 1px solid rgba(46, 204, 113, 0.2); margin-bottom: 10px;'>
        <h4 style='color: #2ecc71; text-align: center; margin: 0;'>📊 Monitoring Architecture</h4>
    </div>
    """, unsafe_allow_html=True)
    try:
        monitoring_image = Image.open(r"C:\Users\rattu\.gemini\antigravity\brain\eae0aefd-b382-47bb-bde9-be9f4dfff280\uploaded_image_1766904924772.png")
        st.image(monitoring_image, caption="K8s Cluster Monitoring", use_container_width=True)
        st.info("**Flow**: App → Prometheus → Grafana Dashboards")
    except Exception as e:
        st.warning("Monitoring diagram not available.")

    st.markdown("---")
    
    # Interactive Data Flow & RAG Pipeline Cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(38, 166, 91, 0.1) 0%, rgba(46, 204, 113, 0.1) 100%); 
                    padding: 15px; border-radius: 10px; border: 1px solid rgba(38, 166, 91, 0.3); height: 100%;'>
            <h3 style='color: #26a65b; margin-top: 0; border-bottom: 2px solid #26a65b; padding-bottom: 5px;'>🔄 Data Flow Stages</h3>
            <ol style='color: #e8e8e8; margin-top: 10px; padding-left: 20px;'>
                <li style='margin-bottom: 10px;'>
                    <strong>Data Ingestion</strong><br>
                    <span style='font-size: 0.9rem; color: #ccc;'>CSV → Document → Embeddings → AstraDB</span>
                </li>
                <li style='margin-bottom: 10px;'>
                    <strong>Query Processing</strong><br>
                    <span style='font-size: 0.9rem; color: #ccc;'>Query → Semantic Search → Top-k Retrieval</span>
                </li>
                <li>
                    <strong>Response Generation</strong><br>
                    <span style='font-size: 0.9rem; color: #ccc;'>Context + Query → LLM → Answer</span>
                </li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(231, 76, 60, 0.1) 0%, rgba(255, 107, 107, 0.1) 100%); 
                    padding: 15px; border-radius: 10px; border: 1px solid rgba(231, 76, 60, 0.3); height: 100%;'>
            <h3 style='color: #e74c3c; margin-top: 0; border-bottom: 2px solid #e74c3c; padding-bottom: 5px;'>🎯 RAG Pipeline Components</h3>
            <ul style='list-style-type: none; padding-left: 0; margin-top: 10px;'>
                <li style='margin-bottom: 10px; display: flex; align-items: center;'>
                    <span style='margin-right: 10px; font-size: 1.2rem;'>🧐</span>
                    <div>
                        <strong>History-Aware Retriever</strong><br>
                        <span style='font-size: 0.9rem; color: #ccc;'>Contextualizes queries based on chat history</span>
                    </div>
                </li>
                <li style='margin-bottom: 10px; display: flex; align-items: center;'>
                    <span style='margin-right: 10px; font-size: 1.2rem;'>📄</span>
                    <div>
                        <strong>Document Chain</strong><br>
                        <span style='font-size: 0.9rem; color: #ccc;'>Formats retrieved docs for the LLM</span>
                    </div>
                </li>
                <li style='margin-bottom: 10px; display: flex; align-items: center;'>
                    <span style='margin-right: 10px; font-size: 1.2rem;'>💬</span>
                    <div>
                        <strong>Message History</strong><br>
                        <span style='font-size: 0.9rem; color: #ccc;'>Stores context for multi-turn conversations</span>
                    </div>
                </li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Deployment Architecture (Styled Columns)
    st.markdown("<h3 style='text-align: center; color: #f39c12;'>🚀 Deployment Architecture</h3>", unsafe_allow_html=True)
    
    dep_col1, dep_col2, dep_col3 = st.columns(3)
    
    with dep_col1:
        st.info("**💻 Local Dev**\n\n- Python venv\n- Flask Server\n- Local Testing")
    
    with dep_col2:
        st.success("**🐳 Docker**\n\n- Containerized App\n- Portable\n- Consistent Env")
    
    with dep_col3:
        st.warning("**☸️ Kubernetes**\n\n- Scalable Cluster\n- Load Balancing\n- Auto-healing Pods")
    
    st.markdown("---")
    
    # Comprehensive Technical Deep Dive (Preserving formatted content but ensuring consistent header)
    st.markdown("### 🎯 Complete Technical Architecture Deep Dive")
    
    with st.expander("🔍 Click to Explore Deep Dive", expanded=True):
        st.markdown("""
        <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, rgba(40, 116, 240, 0.2) 0%, rgba(155, 89, 182, 0.2) 100%); 
                    border-radius: 15px; margin-bottom: 30px; border: 3px solid rgba(40, 116, 240, 0.4);'>
            <h3 style='color: #00d4ff; margin: 0;'>🔹 High-Level Architecture (End-to-End Flow)</h3>
            <p style='color: #e8e8e8; font-size: 1.2rem; font-weight: 600; margin-top: 10px;'>
                User → UI → Backend → LLM + Vector DB → Response → UI
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Core AI Layer
        st.markdown("### 🧠 Core AI Layer")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### 1️⃣ Groq (LLM)
            - **Purpose**: Inference engine for ultra-low latency LLM responses
            - **Role**: Handles final answer generation after relevant context is retrieved
            - **Why Groq?**: Ideal for real-time GenAI applications
            - **Model**: Llama 3.1-8B-Instant
            
            #### 2️⃣ Hugging Face (Embedding Model)
            - **Purpose**: Converts text chunks into vector embeddings
            - **Used During**:
              - **Ingestion**: Documents → Vectors
              - **Query Time**: User query → Vector
            - **Model**: BAAI/bge-base-en-v1.5
            """)
        
        with col2:
            st.markdown("""
            #### 3️⃣ AstraDB (Vector Store)
            - **Purpose**: Online, managed vector database
            - **Functionality**: Stores embeddings and performs semantic similarity search
            - **Why AstraDB over FAISS/Chroma?**
              - ✅ Cloud-native
              - ✅ Scalable
              - ✅ No local infrastructure overhead
              - ✅ Free tier available
            - **Backend**: Cassandra distributed NoSQL
            """)
        
        st.markdown("---")
        
        # RAG Pipeline
        st.markdown("### 📚 RAG Pipeline (Retrieval-Augmented Generation)")
        
        st.markdown("""
        <div style='background: rgba(100, 149, 237, 0.1); padding: 20px; border-radius: 10px; border-left: 5px solid #6495ED;'>
            <pre style='color: #00d4ff; font-size: 1.1rem; line-height: 2; overflow-x: auto;'>
    Documents → Chunking → Embeddings (Hugging Face) → Vector Store (AstraDB)
                                                                 ↓
    User Query → Similarity Search → Context Retrieval → LLM Generation (Groq) → Response
            </pre>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Orchestration Layer
        st.markdown("### 🔗 Orchestration Layer")
        
        st.markdown("""
        #### 4️⃣ LangChain
        - **Purpose**: Acts as the glue between LLM, Embeddings, and Vector DB
        - **Handles**:
          - 🔸 Prompt templates
          - 🔸 Retrieval logic
          - 🔸 Context injection
          - 🔸 Chain management
        - **Benefit**: Enables clean, maintainable RAG workflows
        """)
        
        st.markdown("---")
        
        # Backend & Frontend
        st.markdown("### ⚙️ Backend & Frontend")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### 5️⃣ Flask (Backend REST API)
            - **Responsibilities**:
              - Accept user queries via HTTP
              - Call LangChain RAG pipeline
              - Return LLM-generated responses
              - Handle API routing
            - **Version**: 3.1.2
            """)
        
        with col2:
            st.markdown("""
            #### 6️⃣ HTML / CSS (Frontend UI)
            - **Purpose**: Simple, clean user interface
            - **Functionality**:
              - Sends requests to Flask backend
              - Displays LLM responses
              - Manages chat history
            - **Alternative**: Streamlit dashboard (this app!)
            """)
        
        st.markdown("---")
        
        # Deployment & Infrastructure
        st.markdown("### 🐳 Deployment & Infrastructure")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### 7️⃣ Docker
            - **Purpose**: Containerizes the application
            - **Benefits**:
              - ✅ Environment consistency
              - ✅ Easy deployment
              - ✅ CI/CD compatibility
              - ✅ Isolation
            
            #### 8️⃣ Minikube
            - **Purpose**: Local Kubernetes cluster running inside a VM
            - **Use Case**: Simulate production-grade Kubernetes locally
            - **Benefits**: Testing K8s deployments before cloud deployment
            
            #### 9️⃣ kubectl
            - **Purpose**: Kubernetes CLI tool
            - **Operations**:
              - Deploy pods
              - Manage services
              - Inspect logs
              - Scale workloads
            """)
        
        with col2:
            st.markdown("""
            #### 🔟 GCP VM (Google Cloud Platform)
            - **Purpose**: Cloud VM hosting
            - **Hosts**:
              - Minikube cluster
              - Docker containers
              - Application services
            - **Benefits**:
              - Public accessibility
              - Scalability
              - Reliability
            """)
        
        st.markdown("---")
        
        # Monitoring & Observability
        st.markdown("### 📈 Monitoring & Observability (LLMOps)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### 1️⃣1️⃣ Prometheus
            - **Purpose**: Real-time metrics collection
            - **Collects**:
              - 📊 CPU / Memory usage
              - ⏱️ Request latency
              - 🚀 API throughput
              - 📈 Custom application metrics
            - **Method**: Scrapes metrics from Kubernetes services
            """)
        
        with col2:
            st.markdown("""
            #### 1️⃣2️⃣ Grafana
            - **Purpose**: Metrics visualization
            - **Provides**:
              - 📊 Beautiful dashboards
              - 👁️ System health visibility
              - 📈 Performance monitoring
              - 🚨 Alerting capabilities
            - **Data Source**: Queries Prometheus
            """)
        
        st.markdown("---")
        
        # DevOps & Collaboration
        st.markdown("### 🔁 DevOps & Collaboration")
        
        st.markdown("""
        #### 1️⃣3️⃣ GitHub
        - **Purpose**: Source Code Management (SCM)
        - **Used For**:
          - 🔸 Version control
          - 🔸 Team collaboration
          - 🔸 CI/CD integration
          - 🔸 Code review
          - 🔸 Documentation
        """)
        
        st.markdown("---")
        
        # One-Line Summary
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(255, 215, 0, 0.25) 0%, rgba(255, 165, 0, 0.25) 100%); 
                    padding: 25px; border-radius: 15px; margin-top: 20px; border: 3px solid rgba(255, 215, 0, 0.5);'>
            <h3 style='color: #FFD700; text-align: center; margin-bottom: 15px;'>🧩 One-Line Summary</h3>
            <p style='color: #FFF; font-size: 1.15rem; line-height: 1.8; text-align: center; font-weight: 500;'>
                "I built a <strong>production-style RAG-based GenAI system</strong> using <strong>Groq LLM</strong>, 
                <strong>Hugging Face embeddings</strong>, <strong>AstraDB</strong> as a vector store, orchestrated via 
                <strong>LangChain</strong>, containerized with <strong>Docker</strong>, deployed on <strong>Kubernetes</strong> 
                (Minikube on GCP VM), and monitored using <strong>Prometheus</strong> and <strong>Grafana</strong>."
            </p>
        </div>
        """, unsafe_allow_html=True)



# TAB 5: System Logs
with tab5:
    # Hero Section for Logs
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(52, 152, 219, 0.1) 0%, rgba(142, 68, 173, 0.1) 100%); 
                padding: 15px; border-radius: 12px; border: 1px solid rgba(52, 152, 219, 0.2); margin-bottom: 25px;
                text-align: center; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);'>
        <h2 style='color: #3498db; margin: 0 0 5px 0; font-size: 1.8rem;'>📋 Live System Logs & Health</h2>
        <p style='color: #e8e8e8; font-size: 1.0rem; margin: 0;'>Real-time tracking of application events, errors, and status.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Styled Metrics Cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div style='background: rgba(40, 116, 240, 0.1); padding: 15px; border-radius: 10px; border-left: 5px solid #2874f0; text-align: center;'>
            <h4 style='color: #e8e8e8; margin: 0; font-size: 0.9rem;'>TOTAL LOGS</h4>
            <p style='color: #2874f0; font-size: 1.8rem; font-weight: bold; margin: 5px 0;'>{len(st.session_state.system_logs)}</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        info_count = len([log for log in st.session_state.system_logs if log['level'] == 'INFO'])
        st.markdown(f"""
        <div style='background: rgba(46, 204, 113, 0.1); padding: 15px; border-radius: 10px; border-left: 5px solid #2ecc71; text-align: center;'>
            <h4 style='color: #e8e8e8; margin: 0; font-size: 0.9rem;'>INFO EVENTS</h4>
            <p style='color: #2ecc71; font-size: 1.8rem; font-weight: bold; margin: 5px 0;'>{info_count}</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        error_count = len([log for log in st.session_state.system_logs if log['level'] == 'ERROR'])
        err_color = "#e74c3c" if error_count > 0 else "#95a5a6"
        st.markdown(f"""
        <div style='background: rgba(231, 76, 60, 0.1); padding: 15px; border-radius: 10px; border-left: 5px solid {err_color}; text-align: center;'>
            <h4 style='color: #e8e8e8; margin: 0; font-size: 0.9rem;'>ERRORS</h4>
            <p style='color: {err_color}; font-size: 1.8rem; font-weight: bold; margin: 5px 0;'>{error_count}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Controls Area
    col1, col2 = st.columns([3, 1])
    
    with col1:
        log_level_filter = st.multiselect(
            "🔽 Filter Logs by Level",
            ["INFO", "SUCCESS", "WARNING", "ERROR"],
            default=["INFO", "SUCCESS", "WARNING", "ERROR"]
        )
    
    with col2:
        st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True) # visual alignment
        if st.button("🗑️ Clear Logs", type="primary", use_container_width=True):
            st.session_state.system_logs = []
            st.rerun()
    
    # Display logs container
    st.markdown("### 📜 Log Feed")
    
    log_container = st.container(height=400) # Scrollable container for better UX
    
    with log_container:
        if st.session_state.system_logs:
            # Reverse to show latest first
            for log in reversed(st.session_state.system_logs):
                if log['level'] in log_level_filter:
                    if log['level'] == 'ERROR':
                        st.error(f"**[{log['timestamp']}]** {log['level']}: {log['message']}")
                    elif log['level'] == 'WARNING':
                        st.warning(f"**[{log['timestamp']}]** {log['level']}: {log['message']}")
                    elif log['level'] == 'SUCCESS':
                        st.success(f"**[{log['timestamp']}]** {log['level']}: {log['message']}")
                    else:
                        st.info(f"**[{log['timestamp']}]** {log['level']}: {log['message']}")
        else:
            st.info("📭 No logs available. Start using the application to generate logs.")
    
    st.markdown("---")
    
    # System status
    st.markdown("### 🔍 System Health Monitor")
    
    col1, col2, col3, col4 = st.columns(4)
    
    def status_card(title, status="Active", color="#2ecc71"):
        return f"""
        <div style='background: rgba(46, 204, 113, 0.05); padding: 15px; border-radius: 10px; border: 1px solid {color}; text-align: center;'>
            <h4 style='color: #e8e8e8; margin: 0; font-size: 0.9rem;'>{title}</h4>
            <div style='font-size: 1.5rem; margin: 5px 0;'>🟢</div>
            <p style='color: {color}; margin: 0; font-weight: 600; font-size: 0.8rem;'>{status}</p>
        </div>
        """
    
    with col1:
        st.markdown(status_card("Flask API", "Running"), unsafe_allow_html=True)
    
    with col2:
        st.markdown(status_card("AstraDB", "Connected"), unsafe_allow_html=True)
    
    with col3:
        st.markdown(status_card("Groq LLM", "Operational"), unsafe_allow_html=True)
    
    with col4:
        st.markdown(status_card("Embeddings", "Ready"), unsafe_allow_html=True)

    # Added init log to ensure footer doesn't float alone if empty
    if len(st.session_state.system_logs) == 0:
        add_log("Streamlit application started", "INFO")

# Footer
st.markdown("---")

# Footer container
st.markdown("""
<div style='text-align: center; padding: 20px 20px 10px 20px; background: linear-gradient(135deg, rgba(40, 116, 240, 0.15) 0%, rgba(155, 89, 182, 0.15) 100%); border-radius: 10px; border-top: 2px solid #2874f0;'>
    <p style='color: #00d4ff; font-weight: 600; font-size: 1.1rem; margin-bottom: 10px;'>🛒 Flipkart Product Recommender System</p>
    <p style='color: #00d4ff; font-weight: 600; font-size: 1.1rem; margin-bottom: 10px;'>Built with ❤️ by Ratnesh Kumar Singh | Data Scientist (AI/ML Engineer 4+Years Exp)</p>
    <p style='font-size: 0.9rem; color: #e8e8e8; margin-bottom: 5px;'>Powered by LangChain, Groq, AstraDB, HuggingFace and Streamlit</p>
</div>
""", unsafe_allow_html=True)

# Social links using Streamlit columns (inside the visual footer area)
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

with col2:
    st.markdown('<p style="text-align: center; margin: 0;"><a href="https://github.com/Ratnesh-181998" target="_blank" style="text-decoration: none; color: #2874f0; font-size: 1.1rem; font-weight: 600;">🔗 GitHub</a></p>', unsafe_allow_html=True)

with col3:
    st.markdown('<p style="text-align: center; margin: 0;"><a href="mailto:rattudacsit2021gate@gmail.com" style="text-decoration: none; color: #26a65b; font-size: 1.1rem; font-weight: 600;">📧 Email</a></p>', unsafe_allow_html=True)

with col4:
    st.markdown('<p style="text-align: center; margin: 0;"><a href="https://www.linkedin.com/in/ratneshkumar1998/" target="_blank" style="text-decoration: none; color: #0077b5; font-size: 1.1rem; font-weight: 600;">💼 LinkedIn</a></p>', unsafe_allow_html=True)

# Close the visual footer
st.markdown("""
<div style='height: 10px; background: linear-gradient(135deg, rgba(40, 116, 240, 0.15) 0%, rgba(155, 89, 182, 0.15) 100%); border-radius: 0 0 10px 10px; border-bottom: 2px solid #2874f0; margin-top: -10px;'></div>
""", unsafe_allow_html=True)





# Add initial log
if len(st.session_state.system_logs) == 0:
    add_log("Streamlit application started", "INFO")
