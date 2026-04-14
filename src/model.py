import cv2
import numpy as np

def extract_frames(video_path):
    cap = cv2.VideoCapture(video_path)

    print("Opened:", cap.isOpened())  # ✅ ADD THIS

    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    print("Frames:", len(frames))  # ✅ ADD THIS

    return frames


def detect_deepfake(video_path):
    frames = extract_frames(video_path)

    if len(frames) == 0:
        return "Error", 0

    brightness_values = []

    for frame in frames[:20]:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        brightness = np.mean(gray)
        brightness_values.append(brightness)

    avg_brightness = np.mean(brightness_values)

    if avg_brightness > 100:
        return "Real", int(avg_brightness % 100)
    else:
        return "Fake", int((100 - avg_brightness) % 100)


# Test
if __name__ == "__main__":
    video = "test.mp4"
    result, confidence = detect_deepfake(video)
    print(f"Result: {result}, Confidence: {confidence}%")
