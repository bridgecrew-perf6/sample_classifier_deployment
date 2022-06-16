import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pickle as plk
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import sys
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler


class DataReq(BaseModel):
    order_id: List[int] = []
    store_id: List[int] = []
    to_user_distance: List[float] = []
    to_user_elevation: List[float] = []
    total_earning: List[float] = []
    created_at: List[str] = []

engine = create_engine('postgresql+psycopg2://postgres:admin@localhost:5432/postgres')

app = FastAPI()

print(sys.version)
with open('Predict.plk', 'rb') as f:
    model = plk.load(f)


@app.post('/predict')
def predict(data: DataReq):
    data = data.dict()
    df = pd.DataFrame.from_dict(data)
    response = model.predict(df[['to_user_distance', 'to_user_elevation', 'total_earning']])
    df['taken'] = response
    df['created_at'] = pd.to_datetime(df['created_at'])
    df.to_sql('predictions.history', con=engine, if_exists='append')
    return {'response': response.tolist()}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
