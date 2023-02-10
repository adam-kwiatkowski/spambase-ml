import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from joblib import load
from pydantic import BaseSettings

import app.models.ml.classifier as clf
from app.models.schemas.email import Email
from app.utils import *


class Settings(BaseSettings):
    model_path: str = 'app/models/ml/model.joblib'
    feature_names_path: str = 'app/models/ml/feature_names.json'
    words = []
    characters = []


settings = Settings()
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    clf.model = load(settings.model_path)
    with open(settings.feature_names_path, 'r') as f:
        feature_names = json.load(f)
    settings.words, settings.characters = split_feature_names(feature_names)


@app.post("/spam/predict")
async def get_prediction(email: Email):
    email_features = get_email_features(email.text, settings.words, settings.characters).reshape(1, -1)

    result = clf.model.predict(email_features)[0]
    label = 'spam' if result == 1 else 'not spam'
    return {'label': label}
