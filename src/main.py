from fastapi import FastAPI
from src.model import RFModel
from pydantic import BaseModel, Field

class DataIn(BaseModel):
    area: float = Field(gt=0)
    lat: float = Field(ge=19.194, le=23635)
    lon: float = Field(ge=-102.553, le=-90.488)

class DataOut(BaseModel):
    success:bool
    prediction:float | None = None
    message:str

app = FastAPI()

model=RFModel("models/rf_model.pkl")


@app.post("/predict", status_code=200, response_model=DataOut)
def predict(request:DataIn):
    response=request.model_dump()
    
    try:
        
        prediction = model.make_prediction(
            area=request.area,
            lat = request.lat,
            lon =request.lon
        )
        # return {
        #     "success":True,
        #     "prediction": prediction,
        #     "message": "prediction done"
        # }
        
        response["success"] = True
        response["prediction"] = prediction
        response["message"] = "Prediction done"
    
    except Exception as e:
        # return {
        #     "success": False,
        #     "prediction": None,
        #     "message": str(e)
        # }
        response["success"] = False
        response["prediction"]=None
        response["message"] = str(e)   
    return response     
    