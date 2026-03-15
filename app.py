import streamlit as st
import os
from fpdf import FPDF
from groq import Groq
from faster_whisper import WhisperModel

# --- CONFIGURATION ---
st.set_page_config(page_title="Secure-Scribe AI", page_icon="🔒", layout="centered")

# Access your Groq Key from Streamlit Secrets
# (Setup this in Streamlit Cloud Settings > Secrets)
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=GROQ_API_KEY)

st.title("🔒 Secure-Scribe AI")
st.info("Professional Executive Briefings. 100% Private Processing.")

# --- 1. FILE UPLOAD ---
uploaded_file = st.file_uploader("Upload Audio or Video", type=["mp3", "wav", "m4a", "mp4"])

if uploaded_file:
    # Save the file temporarily
    with open("input_file", "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("Generate Executive Briefing"):
        with st.spinner("Step 1: Local Transcription (Faster-Whisper)..."):
            # We use 'tiny' or 'base' for free web hosting to save memory
            model = WhisperModel("base", device="cpu", compute_type="int8")
            segments, _ = model.transcribe("input_file", beam_size=5)
            full_text = " ".join([segment.text for segment in segments])
        
        with st.spinner("Step 2: AI Summarization (Llama 3.3 via Groq)..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a Chief of Staff. Summarize the following transcript into a professional 3-sentence executive summary followed by a bulleted list of action items."},
                    {"role": "user", "content": full_text}
                ]
            )
            summary_result = response.choices[0].message.content

        # --- 3. GENERATE PDF ---
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("helvetica", "B", 16)
        pdf.cell(0, 10, "EXECUTIVE BRIEFING REPORT", ln=True, align='C')
        pdf.ln(10)
        pdf.set_font("helvetica", size=11)
        pdf.multi_cell(0, 10, summary_result)
        
        pdf_output = "Briefing_Report.pdf"
        pdf.output(pdf_output)

        # --- 4. DOWNLOAD ---
        st.success("Briefing Ready!")
        with open(pdf_output, "rb") as f:
            st.download_button(
                label="📥 Download Executive PDF",
                data=f,
                file_name="Executive_Briefing.pdf",
                mime="application/pdf"
            )