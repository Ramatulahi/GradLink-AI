from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load your trained career recommender model
career_model = joblib.load("model.pkl")

app = FastAPI()

# ===== Career Recommender =====
class CareerInput(BaseModel):
    cgpa: float
    interests: str

@app.post("/recommend-career")
def recommend_career(data: CareerInput):
    df = pd.DataFrame([data.dict()])
    prediction = career_model.predict(df)[0]
    proba = career_model.predict_proba(df)[0]
    return {
        "predicted_career": prediction,
        "confidence_scores": dict(zip(career_model.classes_, map(float, proba)))
    }

# ===== Resource Finder =====
class ResourceInput(BaseModel):
    course_code: str

# Hardcoded resources dictionary (minimal MVP)
resources_db = {
    "MAT201": {
        "YouTube": [
            "https://www.youtube.com/watch?v=kjBOesZCoqc",  # Linear Algebra - 3Blue1Brown
            "https://www.youtube.com/watch?v=HECwFNgqN1Y"   # Eigenvalues - Essence of Linear Algebra
        ],
        "PDFs": [
            "https://example.com/MAT201_notes.pdf",
            "https://example.com/MAT201_past_questions.pdf"
        ]
    },
    "EEE203": {
        "YouTube": [
            "https://www.youtube.com/watch?v=1cadfbhz5vI",  # Circuit Theory basics
            "https://www.youtube.com/watch?v=KYfTVB4ZHhI"
        ],
        "PDFs": [
            "https://example.com/EEE203_circuits.pdf"
        ]
    }
    # add more courses/resources as needed
}

@app.post("/find-resources")
def find_resources(data: ResourceInput):
    course = data.course_code.upper()
    resources = resources_db.get(course)
    if resources:
        return {"course_code": course, "resources": resources}
    else:
        return {"course_code": course, "resources": [], "message": "No resources found for this course"}

