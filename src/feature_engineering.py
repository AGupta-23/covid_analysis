# Simple Feature Engineering

import pandas as pd

def create_features(input_file, output_file):
    df = pd.read_csv(input_file)

    # Fatality rate
    df["fatality_rate"] = df["total_deaths"] / df["total_cases"]

    # Daily new cases/deaths
    df["daily_cases"] = df.groupby("location")["total_cases"].diff().fillna(0)
    df["daily_deaths"] = df.groupby("location")["total_deaths"].diff().fillna(0)

    df.to_csv(output_file, index=False)
    print(f"Feature data saved to {output_file}")
