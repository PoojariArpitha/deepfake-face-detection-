import streamlit as st

st.title("Deepfake Face Detection")

video = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

if video is not None:
    st.video(video)

    if st.button("Analyze"):
        result = "Fake"
        confidence = 90

        st.write(f"Result: {result}")
        st.write(f"Confidence: {confidence}%")
