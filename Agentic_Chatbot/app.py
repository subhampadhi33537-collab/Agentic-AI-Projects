# AI GENERATED UI — PREMIUM EDITION

import time
from datetime import datetime

import streamlit as st
from backend import chatbot
from langchain_core.messages import HumanMessage


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AURA — AI Assistant",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --------------------------------------------------
# CUSTOM CSS — premium glassmorphism theme
# --------------------------------------------------

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=Inter:wght@400;500;600&display=swap');

    :root {
        --accent-1: #7c3aed;
        --accent-2: #06b6d4;
        --bg-0: #05060a;
        --bg-1: #0b0e16;
        --bg-2: #10141f;
        --border: rgba(255,255,255,0.08);
        --text-dim: #8b93a7;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Main background — subtle radial glow */
    .stApp {
        background:
            radial-gradient(circle at 15% 0%, rgba(124,58,237,0.16), transparent 45%),
            radial-gradient(circle at 85% 15%, rgba(6,182,212,0.12), transparent 40%),
            var(--bg-0);
    }

    /* Hide Streamlit default chrome */
    #MainMenu, footer, header { visibility: hidden; }

    /* ---------------- SIDEBAR ---------------- */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--bg-1) 0%, var(--bg-0) 100%);
        border-right: 1px solid var(--border);
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 1.5rem;
    }

    .aura-logo {
        text-align: center;
        padding: 6px 0 22px 0;
    }

    .aura-icon-wrap {
        width: 64px;
        height: 64px;
        margin: 0 auto 14px auto;
        border-radius: 18px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 30px;
        background: linear-gradient(135deg, var(--accent-1), var(--accent-2));
        box-shadow: 0 8px 24px rgba(124,58,237,0.35);
    }

    .aura-title {
        font-family: 'Sora', sans-serif;
        font-size: 26px;
        font-weight: 800;
        letter-spacing: 4px;
        background: linear-gradient(90deg, #fff, #b9c2d6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .aura-subtitle {
        color: var(--text-dim);
        font-size: 12px;
        margin-top: 6px;
        letter-spacing: 0.3px;
    }

    .side-section-label {
        font-family: 'Sora', sans-serif;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: var(--text-dim);
        margin: 18px 0 10px 2px;
    }

    .info-card {
        background: linear-gradient(180deg, var(--bg-2), var(--bg-1));
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 16px;
        margin-top: 10px;
    }

    .info-card-title {
        font-family: 'Sora', sans-serif;
        font-weight: 700;
        font-size: 13.5px;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    .info-card-text {
        color: var(--text-dim);
        font-size: 12.5px;
        line-height: 1.6;
    }

    .badge-row {
        display: flex;
        gap: 6px;
        flex-wrap: wrap;
        margin-top: 12px;
    }

    .badge-pill {
        font-size: 11px;
        padding: 4px 10px;
        border-radius: 999px;
        background: rgba(124,58,237,0.14);
        border: 1px solid rgba(124,58,237,0.35);
        color: #c9b8fb;
        font-weight: 600;
    }

    /* ---------------- MAIN HEADER ---------------- */
    .chat-header {
        text-align: center;
        padding: 8px 0 18px 0;
        border-bottom: 1px solid var(--border);
        margin-bottom: 22px;
    }

    .chat-header h1 {
        font-family: 'Sora', sans-serif;
        font-size: 34px;
        font-weight: 800;
        margin-bottom: 4px;
        background: linear-gradient(90deg, #ffffff 20%, #a9b4cc 60%, #7c3aed 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 1px;
    }

    .chat-header p {
        color: var(--text-dim);
        font-size: 14px;
    }

    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 7px;
        margin: 12px auto 0 auto;
        padding: 5px 14px;
        border-radius: 999px;
        background: rgba(34,197,94,0.10);
        border: 1px solid rgba(34,197,94,0.35);
        color: #4ade80;
        font-size: 12.5px;
        font-weight: 600;
        width: fit-content;
    }

    .status-dot {
        width: 7px;
        height: 7px;
        border-radius: 50%;
        background: #22c55e;
        box-shadow: 0 0 8px #22c55e;
        animation: pulse 1.8s infinite;
    }

    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.35; }
        100% { opacity: 1; }
    }

    .status-center { display: flex; justify-content: center; }

    /* ---------------- CHAT MESSAGES ---------------- */
    div[data-testid="stChatMessage"] {
        border-radius: 18px;
        padding: 4px 6px;
        margin-bottom: 10px;
        border: 1px solid var(--border);
        background: rgba(255,255,255,0.02);
        backdrop-filter: blur(6px);
        animation: fadeIn 0.35s ease-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(6px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .msg-timestamp {
        font-size: 10.5px;
        color: var(--text-dim);
        margin: -4px 0 6px 46px;
    }

    /* Chat input */
    div[data-testid="stChatInput"] {
        border-radius: 16px;
        border: 1px solid var(--border);
        background: var(--bg-2);
    }

    div[data-testid="stChatInput"] textarea {
        font-size: 14.5px;
    }

    /* Buttons */
    .stButton button {
        width: 100%;
        border-radius: 12px;
        font-weight: 600;
        border: 1px solid var(--border);
        background: linear-gradient(180deg, #171c29, #10141f);
        color: #e6e9f2;
        transition: all 0.2s ease;
    }

    .stButton button:hover {
        border-color: var(--accent-1);
        box-shadow: 0 0 0 1px rgba(124,58,237,0.4);
        color: #fff;
    }

    /* Suggestion chips */
    .chip-row { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 4px; }

    /* Scrollbar */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-thumb {
        background: rgba(124,58,237,0.4);
        border-radius: 8px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = 1

config = {"configurable": {"thread_id": str(st.session_state["thread_id"])}}


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown(
        """
        <div class="aura-logo">
            <div class="aura-icon-wrap">✨</div>
            <div class="aura-title">AURA</div>
            <div class="aura-subtitle">AI Universal Response Assistant</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="side-section-label">Conversation</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ Clear", use_container_width=True):
            st.session_state["message_history"] = []
            st.session_state["thread_id"] += 1
            st.rerun()
    with col2:
        msg_count = len(st.session_state["message_history"])
        st.button(f"💬 {msg_count} msgs", disabled=True, use_container_width=True)

    st.markdown('<div class="side-section-label">About</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="info-card">
            <div class="info-card-title">✨ About AURA</div>
            <div class="info-card-text">
                AURA is an intelligent AI assistant powered by LangGraph and
                Groq, with live web search built in. Ask questions, explore
                ideas, learn concepts, and have a real conversation — AURA
                remembers context within this session.
            </div>
            <div class="badge-row">
                <span class="badge-pill">🧠 LangGraph</span>
                <span class="badge-pill">⚡ Groq</span>
                <span class="badge-pill">🔎 Live Search</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("")
    st.caption("🧠 Powered by LangGraph + Groq · Session memory active")


# --------------------------------------------------
# MAIN HEADER
# --------------------------------------------------

st.markdown(
    """
    <div class="chat-header">
        <h1>✨ AURA</h1>
        <p>Your intelligent AI conversation partner</p>
        <div class="status-center">
            <div class="status-pill">
                <span class="status-dot"></span> AURA is online
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# EMPTY STATE — suggestion chips
# --------------------------------------------------

if not st.session_state["message_history"]:
    st.markdown(
        "<p style='text-align:center;color:var(--text-dim);font-size:13.5px;"
        "margin-bottom:14px;'>Try asking something to get started</p>",
        unsafe_allow_html=True,
    )
    suggestions = [
        "What's happening in AI this week?",
        "Explain LangGraph in simple terms",
        "Give me 3 productivity tips",
        "Compare Macine Learning with Deep Learning",
    ]
    cols = st.columns(len(suggestions))
    for col, s in zip(cols, suggestions):
        with col:
            if st.button(s, use_container_width=True, key=f"chip_{s}"):
                st.session_state["_pending_input"] = s


# --------------------------------------------------
# DISPLAY CHAT HISTORY
# --------------------------------------------------

for message in st.session_state["message_history"]:
    with st.chat_message(
        message["role"], avatar="🧑" if message["role"] == "user" else "✨"
    ):
        st.markdown(message["content"])
    st.markdown(
        f'<div class="msg-timestamp">{message.get("time", "")}</div>',
        unsafe_allow_html=True,
    )


# --------------------------------------------------
# CHAT INPUT
# --------------------------------------------------

user_input = st.chat_input("Message AURA...")

# Allow a clicked suggestion chip to act as input
if not user_input and st.session_state.get("_pending_input"):
    user_input = st.session_state.pop("_pending_input")


# --------------------------------------------------
# PROCESS USER INPUT
# --------------------------------------------------

if user_input:

    now = datetime.now().strftime("%I:%M %p")

    st.session_state["message_history"].append(
        {"role": "user", "content": user_input, "time": now}
    )

    with st.chat_message("user", avatar="🧑"):
        st.markdown(user_input)
    st.markdown(f'<div class="msg-timestamp">{now}</div>', unsafe_allow_html=True)

    with st.chat_message("assistant", avatar="✨"):
        placeholder = st.empty()
        with st.spinner("AURA is thinking..."):
            response = chatbot.invoke(
                {"messages": [HumanMessage(content=user_input)]},
                config=config,
            )
            ai_message = response["messages"][-1].content

        # light "typing" reveal for a premium feel
        typed = ""
        for chunk in ai_message.split(" "):
            typed += chunk + " "
            placeholder.markdown(typed + "▌")
            time.sleep(0.01)
        placeholder.markdown(ai_message)

    reply_time = datetime.now().strftime("%I:%M %p")
    st.markdown(f'<div class="msg-timestamp">{reply_time}</div>', unsafe_allow_html=True)

    st.session_state["message_history"].append(
        {"role": "assistant", "content": ai_message, "time": reply_time}
    )