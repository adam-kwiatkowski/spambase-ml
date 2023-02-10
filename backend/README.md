# Backend
This is the backend for the project using FastAPI. It is simple API containing a single endpoint that returns a classification for a given email.


## Project Setup

### Install dependencies

```sh
pip install -r requirements.txt
```

### Run the server

```sh
uvicorn app.main:app --reload
```

### Train the model
In order to train the model, you need to download the dataset from [here](https://archive.ics.uci.edu/ml/datasets/Spambase) and create a folder called `spambase` in the root directory of the repository. Then, place the `spambase.data` and `spambase.names` files in the `spambase` directory.

Then, run the following command:
```sh
python ./app/models/ml/train.py
```

## API
### Predict Spam
| Method | Endpoint      | Description    |
|--------|---------------|----------------|
| POST   | /spam/predict | Get Prediction |

#### Parameters
No parameters
#### Request Body
| Name | Type   | Description                |
|------|--------|----------------------------|
| text | string | The email text to classify |
#### Response
| Name  | Type   | Description                                      |
|-------|--------|--------------------------------------------------|
| label | string | The predicted label, either `spam` or `not spam` |