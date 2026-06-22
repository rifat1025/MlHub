import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    BASE_DIR
    / "models_pkl"
    / "churn_prediction"
    / "model.pkl"
)

model = joblib.load(MODEL_PATH)



def predict_churn(features: list) -> int:
    prediction = model.predict([features])[0]
    return int(prediction)