# 🎭 AI-Based Face Swap Detection

##  Overview

This project is a simple AI-based system designed to detect whether a video is **Real or Deepfake**.
It provides a user-friendly interface where users can upload a video and receive a prediction along with a confidence score. It is effective with all the necessary requirements.



##  Features

* Upload video through a web interface
* Analyze video using backend logic
* Display prediction (Real / Fake)
* Show confidence percentage
* Clean and interactive UI using Streamlit



##  Tech Stack

* Python
* Streamlit
* OpenCV (planned)
* NumPy (planned)



##  Project Structure

```
deepfake-face-detection/
│
├── src/
│   ├── app.py          # UI (Streamlit)
│   ├── main.py         # Backend logic
│   ├── model.py        # Detection logic
│
├── data/               # Sample videos
├── screenshots/        # Output images
├── model_folder/       # Pretrained model (model.h5)
│
└── README.md
```



##  How to Run

```bash
pip install streamlit
python -m streamlit run src/app.py
```



##  Output

* Upload a video
* Click "Check video"
* Get result: **Real / Fake**
* View confidence score



##  Note

This project demonstrates the workflow of a deepfake detection system.
Due to time constraints, a lightweight simulation is used instead of a fully trained deep learning model.



##  Future Improvements

* Integrate CNN-based deep learning model
* Use real datasets for training
* Improve accuracy and performance



##  Team

* Person 1 – Model Development
* Person 2 – Backend Integration
* Person 3 – UI Development



##  Conclusion

This project successfully demonstrates a working pipeline for deepfake detection, combining frontend, backend, and AI logic into a single system.
