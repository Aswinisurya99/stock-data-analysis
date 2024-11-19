import pandas as pd
import random
import numpy as np
import csv
import os

def process_file(file_path):
    # Load CSV file
    df = pd.read_csv(file_path)
    if len(df) < 30:
        raise ValueError("Not enough data points for analysis.")
    
    # Randomly select a starting point for 30 consecutive data points
    start_idx = random.randint(0, len(df) - 30)
    subset = df.iloc[start_idx:start_idx + 30]
    return subset.to_dict('records')

def detect_outliers(data):
    prices = [item['stock_price'] for item in data]
    mean_price = np.mean(prices)
    std_dev = np.std(prices)
    threshold = 2 * std_dev
    
    outliers = []
    for item in data:
        deviation = abs(item['stock_price'] - mean_price)
        if deviation > threshold:
            item['deviation'] = deviation
            item['threshold'] = threshold
            outliers.append(item)
    
    return outliers

def save_outliers_to_csv(outliers, output_file):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=outliers[0].keys())
        writer.writeheader()
        writer.writerows(outliers)
