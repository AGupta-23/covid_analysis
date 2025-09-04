📘 COVID-19 Data Analysis Project:

This project is about analyzing the COVID-19 dataset using Python.
The steps include cleaning the data, exploring it with graphs, creating new features, and finally writing down insights that can help decision-makers.

📂 Project Structure:

data/
 ├── raw/                # Original dataset (downloaded)
 ├── processed/          # Cleaned + feature engineered datasets
results/                 # Actionable insights (text file)
src/                     # Python scripts (cleaning, EDA, etc.)
visualizations/          # Graphs generated from analysis

⚙️ How to Run:

First, download the data:
python src/data_downloader.py


Clean the data:
python src/data_cleaning.py


Do EDA and generate visualizations:
python src/eda_analysis.py


Create features:
python src/feature_engineering.py


Generate insights:
python src/insights_generator.py

🛠 Tools Used:
Python
Pandas, NumPy
Matplotlib, Seaborn

📌 Note:
Since direct downloading from the internet sometimes didn’t work, I wrote a simple script data_downloader.py to fetch the dataset and save it locally.
