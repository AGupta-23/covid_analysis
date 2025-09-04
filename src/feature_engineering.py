import pandas as pd

def add_features():
    print("⚙️ Starting Feature Engineering...")

    # Load cleaned data
    df = pd.read_csv("data/processed/covid_data_clean.csv")
    print(f"📊 Loaded dataset: {df.shape}")

    # 1. Case Fatality Rate (CFR) = deaths / cases * 100
    df["case_fatality_rate"] = (df["total_deaths"] / df["total_cases"]) * 100

    # 2. Daily Growth Rate = new_cases / total_cases * 100
    df["daily_growth_rate"] = (df["new_cases"] / df["total_cases"]) * 100

    # 3. Mortality per 100k (already added in cleaning, just ensure it exists)
    if "deaths_per_100k" not in df.columns:
        df["deaths_per_100k"] = (df["total_deaths"] / df["population"]) * 100000

    # 4. Rolling 7-day avg of cases (growth speed indicator)
    df["rolling_cases_7d"] = df.groupby("location")["new_cases"].transform(lambda x: x.rolling(7).mean())

    # 5. Vaccination Effect Proxy (if vaccination column exists)
    if "total_vaccinations" in df.columns:
        df["cases_after_vax"] = (df["total_cases"] / df["total_vaccinations"]).replace([float("inf")], 0)

    # Save engineered dataset
    df.to_csv("data/processed/covid_data_features.csv", index=False)
    print("✅ Feature engineering complete! Saved to data/processed/covid_data_features.csv")

    # Show sample
    print("\n🔍 Sample with new features:")
    print(df.head(10))

    return df

if __name__ == "__main__":
    engineered_data = add_features()
