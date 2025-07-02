import streamlit as st
import os
from utils.transcriber import transcribe_video
from utils.summarizer import summarize_text

st.set_page_config(page_title="EchoKit", layout="wide")
st.title("🎧 EchoKit – AI-Powered Transcription & Summarization")

st.markdown("Upload a **video or audio file**, and EchoKit will transcribe and summarize it using AI agents.")

uploaded_file = st.file_uploader("Choose a file", type=["mp4", "mp3", "wav", "mkv"])

if uploaded_file:
    video_path = os.path.join("data", uploaded_file.name)
    
    # Save uploaded file
    with open(video_path, "wb") as f:
        f.write(uploaded_file.read())

    # Display media
    if uploaded_file.type.startswith("video"):
        st.video(video_path)
    else:
        st.audio(video_path)

    st.markdown("---")

    # Transcription
    with st.spinner("🔊 Transcribing... please wait ⏳"):
        transcript, segments = transcribe_video(video_path)
    st.success("✅ Transcription complete!")

    # Summarization
    with st.spinner("🧠 Summarizing... please wait"):
        summary = summarize_text(transcript)
    st.success("✅ Summarization complete!")

    # Show output
    with st.expander("📜 Full Transcript", expanded=True):
        st.text_area("Transcript", transcript, height=300)

        st.download_button(
            label="📥 Download Transcript",
            data=transcript,
            file_name="transcript.txt",
            mime="text/plain"
        )

    with st.expander("🧾 Summary", expanded=True):
        st.text_area("Summary", summary, height=200)

        st.download_button(
            label="📥 Download Summary",
            data=summary,
            file_name="summary.txt",
            mime="text/plain"
        )

    # Save output to files
    with open("output/transcript.txt", "w", encoding="utf-8") as f:
        f.write(transcript)
    with open("output/summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    st.markdown("---")
    st.info("📁 Files saved to `/output` folder.")

# Author Footer
st.markdown(
    """
    <hr style="margin-top:3rem;margin-bottom:1rem">
    <div style="text-align:center; font-size: 0.9em;">
        🔧 Built with 🤍 by <strong>Mufitha Majeed</strong> | 
        Project: <code>EchoKit</code> | 
        <a href="https://github.com/yourusername/echokit" target="_blank">GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)