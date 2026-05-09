import os
import random

def verify_face(agent_id, uploaded_image_path):
    """
    Mock face verification for cloud deployment.
    In production, replace with actual face recognition logic.
    """
    try:
        # Simulate processing time
        known_faces_dir = os.path.join(os.path.dirname(__file__), "known_faces")
        known_files = [f for f in os.listdir(known_faces_dir) if f.lower().endswith(".jpg")]
        
        if not known_files:
            return {"matched": False, "confidence": 0.0}

        # Mock: randomly verify with high confidence for demo
        confidence = round(random.uniform(75, 95), 2)
        matched = confidence > 80

        return {
            "matched": matched,
            "confidence": confidence
        }

    except Exception as e:
        print("Face match error:", e)
        return {"matched": False, "confidence": 0.0}