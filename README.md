# ⚖️ LexAI — Indian Legal Assistant Chatbot

<div align="center">

![LexAI Banner](https://img.shields.io/badge/LexAI-Legal%20Assistant-blueviolet?style=for-the-badge&logo=scales&logoColor=white)
![Powered by Groq](https://img.shields.io/badge/Powered%20by-Groq%20⚡-orange?style=for-the-badge)
![LLaMA 3.3 70B](https://img.shields.io/badge/Model-LLaMA%203.3%2070B-blue?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**An AI-powered Indian legal assistant that provides instant, accurate legal guidance — available 24/7, for everyone.**

[🚀 Live Demo](#) · [📖 Docs](#) · [🐛 Report Bug](../../issues) · [✨ Request Feature](../../issues)

</div>

---

## 🌟 What is LexAI?

LexAI is a next-generation conversational AI legal assistant trained to answer questions about **Indian law**. Whether you're dealing with property disputes, family matters, contracts, or corporate issues — LexAI gives you clear, instant guidance powered by one of the world's most advanced open-source language models.

> ⚠️ **Disclaimer:** LexAI is for informational purposes only. Always consult a qualified lawyer for official legal advice.

---

## ✨ Features

| Feature | Description |
|---|---|
| ⚡ **Lightning Fast** | Powered by Groq's ultra-low latency inference engine |
| 🧠 **LLaMA 3.3 70B** | State-of-the-art open-source model for accurate responses |
| 🇮🇳 **India-Specific** | Specialized in Indian civil, criminal, family & corporate law |
| 💬 **Multi-turn Chat** | Remembers conversation context for natural dialogue |
| 🔄 **Auto Retry** | Handles rate limits gracefully with automatic retries |
| 📱 **Responsive UI** | Works seamlessly on desktop and mobile |
| 🔒 **Privacy First** | No data stored — conversations are session-only |
| 🌐 **Always Online** | Deployed on Streamlit Cloud — accessible anywhere |

---

## 🏗️ Tech Stack

```
┌─────────────────────────────────────────────────────┐
│                      LexAI Stack                    │
├─────────────┬───────────────────┬───────────────────┤
│  Frontend   │     Backend       │    AI Engine      │
│             │                   │                   │
│  Streamlit  │  Python 3.11+     │  Groq API         │
│  (Chat UI)  │  Groq SDK         │  LLaMA 3.3 70B    │
│             │  python-dotenv    │                   │
└─────────────┴───────────────────┴───────────────────┘
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- A [Groq API Key](https://console.groq.com) (free)

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/legal-assistant.git
cd legal-assistant
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the App
```bash
streamlit run legal_assistant.py
```

Open your browser at `http://localhost:8501` 🎉

---

## 🌐 Deployment (Streamlit Cloud)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Add your secret in **Advanced Settings**:
```toml
GROQ_API_KEY = "your_groq_api_key_here"
```
5. Click **Deploy** — your app is live! 🚀

---

## 📁 Project Structure

```
legal-assistant/
│
├── legal_assistant.py      # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignore rules
├── .env                    # Environment variables (NOT pushed to GitHub)
└── README.md               # You are here
```

---

## 💬 Supported Legal Domains

```
🏠 Property Law          → Disputes, registration, land rights
👨‍👩‍👧 Family Law           → Divorce, custody, inheritance, adoption
📄 Contract Law          → Agreements, breach, enforcement
🏢 Corporate Law         → Company formation, compliance, disputes
⚖️  Civil Law             → Torts, damages, civil suits
🚔 Criminal Law          → IPC sections, bail, FIR guidance
💼 Labour Law            → Employment rights, termination, PF/ESI
🌿 Consumer Law          → Consumer rights, complaints, remedies
```

---

## 🔮 Roadmap

- [ ] 🗣️ Voice input & text-to-speech output
- [ ] 📄 Document upload & analysis (contracts, FIRs)
- [ ] 🌍 Multi-language support (Tamil, Hindi, Telugu, etc.)
- [ ] 🔍 Case law search & citation
- [ ] 👨‍⚖️ Lawyer directory & booking integration
- [ ] 📊 Legal document generator (affidavits, notices)
- [ ] 🔐 User authentication & conversation history
- [ ] 📱 Mobile app (React Native)

---

## ⚙️ Environment Variables

| Variable | Description | Required |
|---|---|---|
| `GROQ_API_KEY` | Your Groq API key from [console.groq.com](https://console.groq.com) | ✅ Yes |

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🙏 Acknowledgements

- [Groq](https://groq.com) — for blazing fast LLM inference
- [Meta AI](https://ai.meta.com) — for the LLaMA 3.3 70B model
- [Streamlit](https://streamlit.io) — for the amazing web framework
- [LangChain](https://langchain.com) — for inspiration

---

<div align="center">

**Built with ❤️ for making Indian legal knowledge accessible to everyone**

⭐ Star this repo if you found it helpful!

</div>