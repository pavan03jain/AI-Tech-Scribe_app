# 🔒 Secure-Scribe AI: Privacy-First Executive Intelligence

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://YOUR-APP-LINK.streamlit.app)

**Secure-Scribe AI** is a high-performance, privacy-centric pipeline designed to transform long-form audio/video into structured executive briefings. By leveraging local-edge transcription and high-speed LPU inference, the system ensures that sensitive data remains sovereign while providing sub-second intelligence.

## 🚀 Key Features
- **Data Sovereignty:** Uses Faster-Whisper for local-edge speech-to-text processing.
- **Sub-Second Summarization:** Integrated with Llama 3.3 via Groq’s LPU (Language Processing Unit) for near-instant inference.
- **Executive Output:** Automated generation of branded PDF reports featuring 3-sentence briefings and actionable items.
- **Stateless Architecture:** No PII (Personally Identifiable Information) is stored; files are processed in-memory and discarded.

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **STT Engine:** Faster-Whisper (Large-v3/Base)
- **LLM:** Llama 3.3 (70B)
- **Infrastructure:** Groq API & CTranslate2
- **PDF Engine:** FPDF2

## 🧬 System Architecture
1. **Ingestion:** User uploads multimedia via a Streamlit-buffered interface.
2. **Local Transcription:** Audio is processed using `Faster-Whisper` with `int8` quantization to optimize for containerized memory limits.
3. **Contextual Intelligence:** The transcript is passed to the Llama 3.3 model with a specialized "Chief of Staff" system prompt.
4. **Document Synthesis:** The result is parsed into a stylized PDF available for immediate download.

## 📦 Installation & Setup
To run this project locally:
1. Install system dependencies: `sudo apt install ffmpeg`
2. Install Python requirements: `pip install -r requirements.txt`
3. Configure your `.env` file with your `GROQ_API_KEY`.
4. Run: `streamlit run app.py`

---
*Developed by PAVAN JAIN - 2026 Machine Learning Project*