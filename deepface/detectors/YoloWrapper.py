from cv2 import Mat
from typing import List

def build_model():
    from yoloface import face_analysis

    detector = face_analysis()
    return detector

def detect_face(detector: face_analysis, img) -> List[Mat, list, list]:
    img = cv2.imread(img)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    frame, bbox, confidence = detector.face_detection(frame_arr=rgb)
    return frame, bbox, confidence

    # note for serengil
    # i unable to find how to extract landmarks, can you do it .

