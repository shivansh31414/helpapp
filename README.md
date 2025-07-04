# 🧠 Gemini-Pro Chatbot using Streamlit

A simple, browser-based chatbot built with **Streamlit** and powered by **Gemini-Pro** from Google Generative AI. This lightweight app is designed for quick and interactive AI conversations—perfect for prototyping or casual dialogue with a large language model.

---

## 🚀 Features

- ✨ Minimal, clean UI using Streamlit’s `st.chat_*` components
- 🔐 Environment-secured Gemini API key access via `.env`
- 📜 Persistent chat context through session state
- 🤝 Assistant role alignment for better UX
- 🧩 Easily extensible if you want to add NLP pipelines or logging

---

## ⚙️ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/shivansh31414/helpapp.git
cd helpapp
```
### 2. Install Dependencies
bash
pip install streamlit python-dotenv google-
### 3. Set Up Environment Variable
Create a .env file in the root directory:

goggle_Api_key=your_google_gemini_api_key_here
## 4.Run the App

streamlit run main.py
