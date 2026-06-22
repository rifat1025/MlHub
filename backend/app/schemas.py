from pydantic import BaseModel
from typing import Dict, Any, List, Optional
from datetime import datetime

class ModelBase(BaseModel):
    name: str
    description: Optional[str] = None
    model_type: str
    version: str
    accuracy: Optional[float] = None
    features: Optional[List[str]] = None
    parameters: Optional[Dict[str, Any]] = None

class ModelCreate(ModelBase):
    pass

class ModelResponse(ModelBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class PredictionRequest(BaseModel):
    dependents: int
    tenure: int
    online_security: int
    online_backup: int
    device_protection: int
    tech_support: int
    contract: int
    paperless_billing: int
    monthly_charges: float
    total_charges: float


class PredictionResponse(BaseModel):
    prediction: int