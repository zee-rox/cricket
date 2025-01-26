from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import pickle
import os
from datetime import datetime

app = FastAPI()

class CSVInput(BaseModel):
    csv_path: str

def load_model():
    with open('./model/cricket_prediction_model.pkl', 'rb') as file:
        return pickle.load(file)

@app.post("/predict")
async def predict_from_csv(input_data: CSVInput):
    # Validate input path
    if not os.path.exists(input_data.csv_path):
        raise HTTPException(status_code=404, detail="CSV file not found")
    
    try:
        # Load and filter data
        df = pd.read_csv(input_data.csv_path)
        filtered_df = df[
            (df['balls_left'] < 60) & 
            (df['target'] > 120)
        ]
        
        if filtered_df.empty:
            raise HTTPException(status_code=400, detail="No rows match criteria")
        
        # Load model and make predictions
        model = load_model()
        X = filtered_df[['total_runs', 'wickets', 'target', 'balls_left']]
        predictions = model.predict(X)
        
        # Add predictions to dataframe
        filtered_df['predicted_won'] = predictions
        
        # Create results filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        result_path = f"../data/results/prediction_results_{timestamp}.csv"
        
        # Ensure results directory exists
        os.makedirs('results', exist_ok=True)
        
        # Save results
        filtered_df.to_csv(result_path, index=False)
        
        return {"result_path": result_path}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))