# data_cleaning.py
import pandas as pd
import numpy as np
from datetime import datetime

def clean_covid_data():
    """Clean and preprocess the COVID-19 dataset"""
    
    print("🧹 Starting data cleaning...")
    
    # Load raw data
    df = pd.read_csv('data/raw/covid_data_raw.csv')
    print(f"📊 Original dataset shape: {df.shape}")
    
    # 1. Convert date column to datetime
    df['date'] = pd.to_datetime(df['date'])
    print("✅ Converted date column to datetime")
    
    # 2. Remove unnecessary columns (keep only essential ones for analysis)
    essential_cols = [
        'location', 'date', 'total_cases', 'new_cases', 'total_deaths', 
        'new_deaths', 'population', 'total_cases_per_million', 
        'new_cases_per_million', 'total_deaths_per_million'
    ]
    
    # Keep only columns that exist in the dataset
    available_cols = [col for col in essential_cols if col in df.columns]
    df = df[available_cols]
    print(f"✅ Kept {len(available_cols)} essential columns")
    
    # 3. Remove rows where location is not a country (remove continents, income groups)
    exclude_locations = [
        'World', 'Europe', 'Asia', 'North America', 'South America', 'Africa', 'Oceania',
        'High income', 'Upper middle income', 'Lower middle income', 'Low income',
        'European Union'
    ]
    df = df[~df['location'].isin(exclude_locations)]
    print(f"✅ Removed non-country locations. New shape: {df.shape}")
    
    # 4. Handle missing values
    # For numeric columns, fill NaN with 0 (assuming no data means no cases/deaths)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].fillna(0)
    print("✅ Filled missing numeric values with 0")
    
    # 5. Remove rows with negative values (data errors)
    for col in ['total_cases', 'new_cases', 'total_deaths', 'new_deaths']:
        if col in df.columns:
            df = df[df[col] >= 0]
    print("✅ Removed rows with negative values")
    
    # 6. Filter data to focus on main pandemic period (2020-2023)
    df = df[(df['date'] >= '2020-01-01') & (df['date'] <= '2023-12-31')]
    print(f"✅ Filtered to 2020-2023 period. Shape: {df.shape}")
    
    # 7. Remove countries with insufficient data (less than 100 days of data)
    country_counts = df['location'].value_counts()
    valid_countries = country_counts[country_counts >= 100].index
    df = df[df['location'].isin(valid_countries)]
    print(f"✅ Kept {len(valid_countries)} countries with sufficient data")
    
    # 8. Create additional useful columns
    if 'population' in df.columns and df['population'].sum() > 0:
        # Calculate cases per 100k population
        df['cases_per_100k'] = (df['total_cases'] / df['population']) * 100000
        df['deaths_per_100k'] = (df['total_deaths'] / df['population']) * 100000
    
    # Add year and month columns for time-based analysis
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['month_year'] = df['date'].dt.to_period('M')
    
    print("✅ Added derived columns: cases_per_100k, deaths_per_100k, year, month")
    
    # 9. Sort by location and date
    df = df.sort_values(['location', 'date']).reset_index(drop=True)
    
    # 10. Data quality check
    print("\n📋 Data Quality Summary:")
    print(f"   • Final shape: {df.shape}")
    print(f"   • Countries: {df['location'].nunique()}")
    print(f"   • Date range: {df['date'].min()} to {df['date'].max()}")
    print(f"   • Total cases (latest): {df.groupby('location')['total_cases'].last().sum():,.0f}")
    print(f"   • Missing values: {df.isnull().sum().sum()}")
    
    # Save cleaned data
    df.to_csv('data/processed/covid_data_clean.csv', index=False)
    print("\n✅ Cleaned data saved to 'data/processed/covid_data_clean.csv'")
    
    # Show sample of cleaned data
    print("\n🔍 Sample of cleaned data:")
    print(df.head(10))
    
    return df

if __name__ == "__main__":
    cleaned_data = clean_covid_data()