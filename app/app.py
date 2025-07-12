from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import joblib

app = FastAPI()

model = joblib.load("xgboost.pkl")

class PredictionInput(BaseModel):
    encoded_smiles: list  # List of floats or integers (Morgan FP)
    encoded_protein: list  # One-hot vector (must be length 3)

@app.post("/predict")
def predict_binding_affinity(input_data: PredictionInput):
    encoded_smiles = np.array(input_data.encoded_smiles)
    encoded_protein = np.array(input_data.encoded_protein)

    if len(encoded_protein) != 3:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid protein encoding length. Expected 3, got {len(encoded_protein)}."
        )

    combined_features = np.hstack((encoded_smiles, encoded_protein))
    prediction = model.predict([combined_features])
    prediction_probs = model.predict_proba([combined_features])
    return {"prediction": float(prediction[0])}
