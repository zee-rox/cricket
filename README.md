# Cricket Match Prediction API

This repository contains a machine learning model that predicts cricket match outcomes based on various in-game statistics.

## Project Structure

```
cricket/
├── data/
│   ├── train/
│   │   └── cricket_dataset.csv
│   ├── test/
│   │   └── cricket_dataset_test.csv
│   └── results/
│       └── prediction_results_{timestamp}.csv
├── src/
│   ├── app.py
│   └── eval_api.py
    ├── model/
│       └── cricket_prediction_model.pkl
    ├── notebooks/
│       └── cricket_prediction.ipynb
└── README.md
```

## Dataset Features

The model uses the following features to make predictions:
- `total_runs`: Total runs scored
- `wickets`: Number of wickets fallen
- `target`: Target score
- `balls_left`: Number of balls remaining
- `won`: Target variable (1 for win, 0 for loss)

## Model Selection

Random Forest Classifier was chosen for this task because:
1. It handles non-linear relationships effectively
2. Provides good protection against overfitting
3. Can capture complex interactions between features
4. Works well with both numerical and categorical data

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/zee-rox/cricket.git
cd cricket
```

2. Install required dependencies:
```bash
pip install requirements.txt
```

## Running the Server

1. Start the FastAPI server:
```bash
cd src
uvicorn app:app --reload
```

The server will start at `http://localhost:8000`

## API Endpoints

### POST /predict
Makes predictions on cricket match outcomes using a CSV file.

Request body:
```json
{
    "csv_path": "path/to/input.csv"
}
```

Response:
```json
{
    "result_path": "path/to/results/prediction_results_{timestamp}.csv"
}
```

## Evaluating the API

1. Run the evaluation script:
```bash
python src/eval_api.py
```

This will:
- Send a test CSV to the API
- Print the API response
- Display prediction results
- Clean up test files

## Model Performance

The Random Forest model achieves:
- High accuracy in predicting match outcomes
- Good balance between precision and recall
- Robust performance across different match scenarios

## Error Handling

The API includes comprehensive error handling for:
- Missing CSV files
- Invalid data formats
- Empty datasets
- Server errors

## Results

Predictions are saved in the `data/results` directory with timestamps for easy tracking and analysis.

## Notes

- The model filters matches where:
  - Less than 60 balls are remaining
  - Target score is greater than 120
- Predictions are binary (win/loss)
- Results include all original features plus predictions
