from src.data_cleaning import clean_covid_data
from src.feature_engineering import add_features
from src.eda_analysis import run_eda
from src.insights_generator import generate_insights

def main():
    print("\n🚀 Starting COVID-19 Analysis Pipeline...\n")

    # Step 1: Data Cleaning
    cleaned_df = clean_covid_data()

    # Step 2: Feature Engineering
    features_df = add_features()

    # Step 3: Exploratory Data Analysis (Visualizations)
    run_eda()

    # Step 4: Generate Actionable Insights
    generate_insights()

    print("\n🎉 Pipeline complete! Check 'data/processed/', 'visualizations/', and 'results/' folders.\n")

if __name__ == "__main__":
    main()
