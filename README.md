![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) ![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D) ![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
# Spambase ML
I've created this project to learn more about the deployment of machine learning models. The project is a simple API that takes in an email and returns a prediction of whether it is spam or not spam. The model is trained using the Spambase dataset available [here](https://archive.ics.uci.edu/ml/datasets/Spambase).


This repository is divided into two parts, the frontend and the backend. The frontend is a simple Vue 3 app that allows you to enter an email and get a prediction. The backend is a FastAPI app that contains the model and the endpoint to make predictions.

Informations about the API and training the model can be found in the [backend README](backend/README.md).

![Screenshot](https://user-images.githubusercontent.com/22380943/218220229-b7529f64-238d-4cd6-bb77-ed88efd40938.png)

## Running the web app
```console
docker compose up -d
```
