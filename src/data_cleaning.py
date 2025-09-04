# Simple Data Cleaning

import pandas as pd

def clean_data(input_file, output_file):
    # Load dataset
    df = pd.read_csv(input_file)

    # Drop rows where total cases or deaths are missing
    df = df.dropna(subset=["total_cases", "total_deaths"])

    # Replace other missing values with 0
    df = df.fillna(0)

    # Save cleaned data
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")
