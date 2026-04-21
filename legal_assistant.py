from dotenv import load_dotenv
import os
import streamlit as st
from groq import Groq
import spacy
import random
import time

# ── Must be first Streamlit command ──────────────────────────────────────────
st.set_page_config(page_title="Legal Assistant Chatbot", page_icon="⚖️")

# ── Load environment variables ────────────────────────────────────────────────
load_dotenv()

# ── Groq client ───────────────────────────────────────────────────────────────
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "llama-3.3-70b-versatile"  # Free, fast, and powerful on Groq

SYSTEM_PROMPT = (
    "You are an expert Indian legal assistant. Answer questions clearly and "
    "accurately about Indian law, including civil, criminal, family, property, "
    "contract, and corporate law. Always remind users to consult a qualified "
    "lawyer for official legal advice."
)

# ── Random conversation starters ──────────────────────────────────────────────
INITIAL_PROMPTS = [
    "What legal assistance do you need today?",
    "Do you have any questions about Indian civil law?",
    "Feel free to ask me about family law, property disputes, or contract law.",
    "How can I help you with corporate or business law issues?",
    "I'm here to assist you with any legal questions. What would you like to know?",
]

# ── Load spaCy once ───────────────────────────────────────────────────────────
@st.cache_resource
def load_nlp():
    return spacy.load("en_core_web_sm")

nlp = load_nlp()

# ── NLP helper ────────────────────────────────────────────────────────────────
def process_input(user_input: str):
    doc = nlp(user_input)
    tokens = [token.text for token in doc]
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return tokens, entities

# ── Groq response with retry ──────────────────────────────────────────────────
def get_groq_response(messages: list, max_retries: int = 3) -> str:
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                temperature=0.4,
                max_tokens=1024,
                stream=True,
            )
            return response  # return stream
        except Exception as e:
            if "429" in str(e) and attempt < max_retries - 1:
                wait = 15 * (attempt + 1)
                st.warning(f"⏳ Rate limit hit. Retrying in {wait}s...")
                time.sleep(wait)
            else:
                raise e

# ── UI ────────────────────────────────────────────────────────────────────────
st.title("⚖️ Legal Assistant Chatbot")
st.caption("Powered by Groq · LLaMA 3.3 70B · For informational purposes only")

# ── Session state ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    # messages = Groq API format (includes system prompt)
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
    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.display_history.append(("user", user_input))

    # Optional NLP entity display
    _, entities = process_input(user_input)
    if entities:
        with st.expander("🔍 Detected entities (NLP)", expanded=False):
            for text, label in entities:
                st.write(f"**{text}** → `{label}`")

    # Add user message to Groq history
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Get and stream Groq response
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

    # Save assistant reply to history
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })
    st.session_state.display_history.append(("assistant", reply))