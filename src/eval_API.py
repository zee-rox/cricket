import requests
import pandas as pd
import os

test_csv_path = "../data/test/cricket_dataset_test.csv"
try:
    response = requests.post(
        "http://localhost:8000/predict",
        json={"csv_path": test_csv_path}
    )
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    
    if response.status_code == 200:
        result_path = response.json()["result_path"]
        print("\nPrediction Results:")
        
except requests.exceptions.ConnectionError:
    print("Error: Cannot connect to API. Make sure the server is running.")
finally:
    # Cleanup
    os.remove(test_csv_path)