# data_downloader.py
import pandas as pd
import urllib.request
import os

def download_covid_data():
    """Download COVID-19 data and save to data/raw folder"""
    
    # Create directories if they don't exist
    os.makedirs('data/raw', exist_ok=True)
    os.makedirs('data/processed', exist_ok=True)
    
    try:
        # URL of the COVID-19 dataset
        url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
        
        print("Downloading COVID-19 data...")
        
        # Download using pandas (easier than urllib)
        df = pd.read_csv(url)
        
        # Save to raw data folder
        df.to_csv('data/raw/covid_data_raw.csv', index=False)
        
        print(f"✅ Dataset downloaded successfully!")
        print(f"📊 Shape: {df.shape}")
        print(f"📅 Date range: {df['date'].min()} to {df['date'].max()}")
        print(f"🌍 Countries: {df['location'].nunique()}")
        
        # Show first few rows
        print("\n🔍 First 5 rows:")
        print(df.head())
        
    except Exception as e:
        print(f"❌ Error downloading data: {e}")
        print("\n🔄 Alternative: Use built-in dataset instead")
        
        # Fallback: create a small sample dataset
        create_sample_data()

def create_sample_data():
    """Create a sample COVID dataset if download fails"""
    import numpy as np
    from datetime import datetime, timedelta
    
    # Create sample data
    countries = ['USA', 'India', 'Brazil', 'UK', 'France', 'Germany', 'Italy', 'Spain']
    dates = pd.date_range('2020-01-01', '2023-12-31', freq='D')
    
    data = []
    for country in countries:
        for i, date in enumerate(dates[:500]):  # Limit to 500 days per country
            # Simulate realistic COVID data
            cases = max(0, int(np.random.normal(1000, 500) * (1 + 0.1 * np.sin(i/30))))
            deaths = max(0, int(cases * np.random.uniform(0.01, 0.03)))
            
            data.append({
                'location': country,
                'date': date,
                'new_cases': cases,
                'total_cases': cases * (i + 1),
                'new_deaths': deaths,
                'total_deaths': deaths * (i + 1),
                'population': np.random.randint(50000000, 350000000)
            })
    
    df = pd.DataFrame(data)
    df.to_csv('data/raw/covid_data_raw.csv', index=False)
    print("✅ Sample dataset created!")
    print(f"📊 Shape: {df.shape}")

if __name__ == "__main__":
    download_covid_data()