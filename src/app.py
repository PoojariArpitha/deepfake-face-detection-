import streamlit as st
from main import detect_deepfake  

st.set_page_config(page_title="Deepfake Detection", layout="centered")

st.title("AI Based Face Swap Detection")

video = st.file_uploader("Upload Video", type=["mp4", "avi", "mov"])

if video is not None:
    st.video(video)

    if st.button("Check video"):

        video_bytes = video.read()

        with open("temp.mp4", "wb") as f:
            f.write(video_bytes)

        result, confidence = detect_deepfake("temp.mp4")

        st.success(f"Result: {result}")
        st.info(f"Confidence: {confidence}%")