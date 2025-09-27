from datetime import date
from fastapi import APIRouter

from routers.services.diabetes_service import diabetes_prediction
from schemas.diabetes_schemas import PatientData

router = APIRouter()

@router.post("/predict")
async def patient_predict(data: PatientData):
    print("patient data ", data.identification_number)

    prediction = diabetes_prediction(data)
    return {"prediction": prediction}
