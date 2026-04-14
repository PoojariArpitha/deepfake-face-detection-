import cv2
import random

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

def extract_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()
    return frames

def detect_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces

def predict_face(face_img):
    # Simulated model (hackathon friendly)
    label = random.choice(["Fake", "Real"])
    confidence = random.uniform(70, 99)
    return label, confidence

# ⭐ THIS IS YOUR FINAL OUTPUT FUNCTION
def real_model(video_path):
    frames = extract_frames(video_path)

    fake_count = 0
    real_count = 0
    confidences = []

    for frame in frames[:20]:  # limit for speed
        faces = detect_faces(frame)

        for (x, y, w, h) in faces:
            face_img = frame[y:y+h, x:x+w]

            label, confidence = predict_face(face_img)
            confidences.append(confidence)

            if label == "Fake":
                fake_count += 1
            else:
                real_count += 1

    if fake_count > real_count:
        final_label = "Fake"
    else:
        final_label = "Real"

    avg_confidence = round(sum(confidences)/len(confidences), 2) if confidences else 0

    return final_label, avg_confidence
