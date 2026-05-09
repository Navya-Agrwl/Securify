from deepface import DeepFace
import os

def verify_face(agent_id, uploaded_image_path):
    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        KNOWN_FACES_DIR = os.path.join(BASE_DIR, "known_faces")

        known_face_files = [
            f for f in os.listdir(KNOWN_FACES_DIR)
            if f.lower().endswith(".jpg")
        ]

        if not known_face_files:
            return {"matched": False, "confidence": 0.0}

        best_confidence = 0.0
        matched = False

        for face_file in known_face_files:
            known_image_path = os.path.join(KNOWN_FACES_DIR, face_file)
            try:
                result = DeepFace.verify(
                    uploaded_image_path,
                    known_image_path,
                    enforce_detection=False
                )
                confidence = (1 - result["distance"]) * 100
                if confidence > best_confidence:
                    best_confidence = confidence
                if result["verified"]:
                    matched = True
            except Exception:
                continue

        return {
            "matched": matched,
            "confidence": round(best_confidence, 2)
        }

    except Exception as e:
        print("Face match error:", e)
        return {"matched": False, "confidence": 0.0}