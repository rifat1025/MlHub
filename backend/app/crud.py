from sqlalchemy.orm import Session
from app.models import PredictionLog


def save_prediction(
    db: Session,
    model_id: int,
    input_data: dict,
    prediction: dict,
    confidence: float = None,
):
    record = PredictionLog(
        model_id=model_id,
        input_data=input_data,
        prediction=prediction,
        confidence=confidence,
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return record