import pandas as pd

def generate_insights():
    print("🧠 Generating actionable insights...")

    # Load engineered dataset
    df = pd.read_csv("data/processed/covid_data_features.csv")
    insights = []

    # 1. Global fatality rate
    total_cases = df["total_cases"].max()
    total_deaths = df["total_deaths"].max()
    fatality_rate = (total_deaths / total_cases) * 100
    insights.append(f"🌍 Global fatality rate during COVID-19 was {fatality_rate:.2f}%.")

    # 2. Vaccination effect (if vaccination data available)
    if "total_vaccinations" in df.columns:
        latest = df.dropna(subset=["total_vaccinations"])
        vaccinated_countries = latest.groupby("location").last()
        high_vax = vaccinated_countries[vaccinated_countries["total_vaccinations"] > 1_000_000]
        low_vax = vaccinated_countries[vaccinated_countries["total_vaccinations"] <= 1_000_000]

        if not high_vax.empty and not low_vax.empty:
            avg_deaths_high = high_vax["deaths_per_100k"].mean()
            avg_deaths_low = low_vax["deaths_per_100k"].mean()
            reduction = ((avg_deaths_low - avg_deaths_high) / avg_deaths_low) * 100
            insights.append(f"💉 Countries with higher vaccination rates had about {reduction:.1f}% fewer deaths per 100k population.")

    # 3. Peak cases insight
    peak_day = df.loc[df["new_cases"].idxmax()]
    insights.append(
        f"📈 Peak daily cases were {int(peak_day['new_cases']):,} "
        f"on {peak_day['date']} in {peak_day['location']}."
    )

    # Save insights
    with open("results/actionable_insights.txt", "w", encoding="utf-8") as f:
        f.write("=== COVID-19 Actionable Insights ===\n\n")
        for i, ins in enumerate(insights, 1):
            f.write(f"{i}. {ins}\n")

    print("✅ Insights generated and saved to results/actionable_insights.txt")

    # Show them
    print("\n🔍 Insights Preview:")
    for ins in insights:
        print("-", ins)


if __name__ == "__main__":
    generate_insights()
