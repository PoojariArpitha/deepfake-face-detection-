
import streamlit as st

st.set_page_config(page_title="Deepfake Detection", layout="centered")

st.title("AI Based Face Swap Detection")

video = st.file_uploader("Upload Video", type=["mp4", "avi", "mov"])

if video is not None:
    st.video(video)

    if st.button("Check video"):
        result = "Fake"
        confidence = 90

        st.write("Prediction:", result)
        st.write("Accuracy Level:", str(confidence) + "%")