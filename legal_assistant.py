from dotenv import load_dotenv
import os
import streamlit as st
from groq import Groq
import random
import time

# ── Must be first Streamlit command ──────────────────────────────────────────
st.set_page_config(
    page_title="LexAI — Indian Legal Assistant",
    page_icon="⚖️",
    layout="centered",
    menu_items={
        'About': "**LexAI** — AI-powered Indian Legal Assistant built with Groq & LLaMA 3.3 70B"
    }
)

# ── Load environment variables ────────────────────────────────────────────────
load_dotenv()

# ── Groq client ───────────────────────────────────────────────────────────────
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "llama-3.3-70b-versatile"

SYSTEM_PROMPT = (
    "You are an expert Indian legal assistant. Answer questions clearly and "
    "accurately about Indian law, including civil, criminal, family, property, "
    "contract, and corporate law. Always remind users to consult a qualified "
    "lawyer for official legal advice."
)

INITIAL_PROMPTS = [
    "What legal assistance do you need today?",
    "Do you have any questions about Indian civil law?",
    "Feel free to ask me about family law, property disputes, or contract law.",
    "How can I help you with corporate or business law issues?",
    "I'm here to assist you with any legal questions. What would you like to know?",
]

# ── Groq response with retry ──────────────────────────────────────────────────
def get_groq_response(messages: list, max_retries: int = 3):
    for attempt in range(max_retries):
        try:
            return client.chat.completions.create(
                model=MODEL,
                messages=messages,
                temperature=0.4,
                max_tokens=1024,
                stream=True,
            )
        except Exception as e:
            if "429" in str(e) and attempt < max_retries - 1:
                wait = 15 * (attempt + 1)
                st.warning(f"⏳ Rate limit hit. Retrying in {wait}s...")
                time.sleep(wait)
            else:
                raise e

# ── UI ────────────────────────────────────────────────────────────────────────
st.markdown("""
    <h1 style='text-align: center; background: linear-gradient(90deg, #7B2FBE, #4A90D9);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    font-size: 3rem; font-weight: 800;'>
    ⚖️ LexAI
    </h1>
    <p style='text-align: center; color: gray; font-size: 0.9rem;'>
    🇮🇳 Indian Legal Assistant · Powered by Groq ⚡ · LLaMA 3.3 70B · For informational purposes only
    </p>
    <hr>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
    st.session_state.display_history = []
    opening = random.choice(INITIAL_PROMPTS)
    st.session_state.display_history.append(("assistant", opening))

# ── Render chat history ───────────────────────────────────────────────────────
for role, text in st.session_state.display_history:
    with st.chat_message(role):
        st.markdown(text)

# ── Chat input ────────────────────────────────────────────────────────────────
user_input = st.chat_input("Ask your legal question here…")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.display_history.append(("user", user_input))

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            stream = get_groq_response(st.session_state.messages)
            reply = ""
            placeholder = st.empty()
            for chunk in stream:
                delta = chunk.choices[0].delta.content
                if delta:
                    reply += delta
                    placeholder.markdown(reply + "▌")
            placeholder.markdown(reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })
    st.session_state.display_history.append(("assistant", reply))