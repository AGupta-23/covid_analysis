# Actionable Insights

import pandas as pd

def generate_insights(input_file, output_file):
    df = pd.read_csv(input_file)

    insights = []
    insights.append(f"1. Average fatality rate: {df['fatality_rate'].mean()*100:.2f}%")
    insights.append(f"2. Peak daily cases: {df['daily_cases'].max():.0f}")
    insights.append(f"3. Peak daily deaths: {df['daily_deaths'].max():.0f}")

    with open(output_file, "w") as f:
        for line in insights:
            f.write(line + "\n")

    print("Insights written to", output_file)
