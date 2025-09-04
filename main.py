# Main pipeline runner (simple and readable)

from src.data_cleaning import clean_data
from src.eda_analysis import run_eda
from src.feature_engineering import create_features
from src.insights_generator import generate_insights

# File paths
raw_data = "data/raw/covid_data_raw.csv"
clean_data_file = "data/processed/covid_data_clean.csv"
features_file = "data/processed/covid_data_features.csv"
results_file = "results/actionable_insights.txt"
viz_folder = "visualizations"

# Step 1: Clean data
clean_data(raw_data, clean_data_file)

# Step 2: Run EDA
run_eda(clean_data_file, viz_folder)

# Step 3: Feature Engineering
create_features(clean_data_file, features_file)

# Step 4: Generate Insights
generate_insights(features_file, results_file)

print("\n✅ Project pipeline complete!")
