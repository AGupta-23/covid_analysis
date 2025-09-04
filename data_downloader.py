# Simple Data Downloader

import pandas as pd

def download_data(output_file):
    # Source: Our World in Data - COVID dataset
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

    print("📥 Downloading dataset...")
    df = pd.read_csv(url)

    # Save raw data
    df.to_csv(output_file, index=False)
    print(f"✅ Raw data saved to {output_file}")

if __name__ == "__main__":
    download_data("data/raw/covid_data_raw.csv")
