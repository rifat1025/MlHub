from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
import logging
from . import models, schemas
from .models import ModelMetadata, PredictionLog   
from .database import engine, Base, get_db
from .ml_utils import predict_churn
from .crud import save_prediction


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="MLHub API",
    description="API for managing and serving machine learning models",
    version="1.0.0",
)
Base.metadata.create_all(bind=engine)
@app.get("/")
def root():
    return {
        "message": "MLHub API",
        "version": "1.0.0",
        "status": "running",
        "models_loaded": len(model_manager.models),
        "database": "MySQL (XAMPP)"
    }

@app.post("/predict")
def predict(
    request : schemas.PredictionRequest,
    db : Session = Depends (get_db)
):
    features = [
    request.dependents,
    request.tenure,
    request.online_security,
    request.online_backup,
    request.device_protection,
    request.tech_support,
    request.contract,
    request.paperless_billing,
    request.monthly_charges,
    request.total_charges,
]

    prediction = predict_churn(features)
    
    # Save the prediction to the database
    save_prediction(
        db=db,
        model_id=1,  # Assuming a single model for now, can be extended to support multiple models
        input_data=request.model_dump(),
        prediction={"churn": prediction},
    )

    return {
        "prediction": prediction
    }
    