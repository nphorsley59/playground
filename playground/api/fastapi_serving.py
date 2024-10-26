"""
A basic model-serving API using the FastAPI framework.

Endpoints:
    /predict
        Method: POST

Create and run a FastAPI app with uvicorn <path>.<to>.<module>.:app --reload.
Test POST endpoints with python -m <path>.<to>.<module>.
"""

from unittest.mock import MagicMock

from fastapi import FastAPI
import numpy as np
from pydantic import BaseModel
import requests


# Create the app
app = FastAPI()


# The model would typically be loaded here
model = MagicMock()
model.predict.return_value = np.array([1]) 


class FeatureData(BaseModel):
    feature1: float
    feature2: float
    feature3: float


@app.post("/predict")
async def predict(data: FeatureData):
    """
    POST /predict
    Submits feature data to a model and returns prediction.

    Returns:
        Prediction as a JSON-formatted response.

    Example:
        uvicorn <path>.<to>.<module>.:app --reload
        http://127.0.0.1:8000/predict
    """
    # Reshape input data from the request for prediction
    feature_array = np.array([[data.feature1, data.feature2, data.feature3]])
    # Make a prediction
    prediction = model.predict(feature_array)
    predicted_class = prediction[0]
    # Return the prediction as a JSON response
    return {"prediction": int(predicted_class)}


if __name__ == "__main__":
    url = "http://127.0.0.1:8000/predict"
    data = {
        "feature1": 0.123,
        "feature2": 0.456,
        "feature3": 0.789,
    }
    response = requests.post(url, json=data)
    print(response.json())
