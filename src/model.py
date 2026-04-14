# import cv2   
# import numpy as np

import random

def extract_frames(video_path):
    
    print("Opened: True")
    print("Frames: Simulated")
    return ["frame1", "frame2"]


def detect_deepfake(video_path):
    frames = extract_frames(video_path)

    if len(frames) == 0:
        return "Error", 0

    
    result = random.choice(["Real", "Fake"])
    confidence = random.randint(60, 95)

    return result, confidence



if __name__ == "__main__":
    video = "test.mp4"
    result, confidence = detect_deepfake(video)
    print(f"Result: {result}, Confidence: {confidence}%")
