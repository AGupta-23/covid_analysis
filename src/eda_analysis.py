# Exploratory Data Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda(input_file, output_folder):
    df = pd.read_csv(input_file)

    # 1. Global trend
    df.groupby("date")["total_cases"].sum().plot(figsize=(10,5))
    plt.title("Global COVID-19 Cases Trend")
    plt.xlabel("Date")
    plt.ylabel("Cases")
    plt.savefig(f"{output_folder}/global_cases_trend.png")
    plt.close()

    # 2. Top 10 countries
    top_countries = df.groupby("location")["total_cases"].max().sort_values(ascending=False).head(10)
    sns.barplot(x=top_countries.values, y=top_countries.index)
    plt.title("Top 10 Countries by Cases")
    plt.savefig(f"{output_folder}/top_affected_countries.png")
    plt.close()

    # 3. Deaths vs Cases
    plt.scatter(df["total_cases"], df["total_deaths"], alpha=0.3)
    plt.title("Deaths vs Cases")
    plt.xlabel("Cases")
    plt.ylabel("Deaths")
    plt.savefig(f"{output_folder}/deaths_vs_cases_analysis.png")
    plt.close()

    print("EDA visualizations saved.")
