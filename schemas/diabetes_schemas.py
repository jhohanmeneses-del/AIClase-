from pydantic import BaseModel

class PatientData(BaseModel):
    firs_name: str 
    last_name: str
    identification_number:str
    pregnancies:int
    glucose:int
    bloodPressure:int
    skinThickness:int
    insulin:int	
    bmi: float
    diabetesPedigreeFunction:float
    age:int