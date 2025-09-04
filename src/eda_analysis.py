# # eda_analysis.py



import pandas as pd
import matplotlib.pyplot as plt

def run_eda():
    print("📊 Starting EDA Analysis...")

    # Load cleaned dataset
    df = pd.read_csv("data/processed/covid_data_clean.csv")
    print(f"📈 Loaded clean dataset: {df.shape}")

    # Visualization 1: Global Cases Trend
    global_trend = df.groupby("date")["new_cases"].sum()
    plt.figure(figsize=(10, 6))
    global_trend.plot(title="Global Daily New Cases")
    plt.xlabel("Date")
    plt.ylabel("New Cases")
    plt.savefig("visualizations/global_cases_trend.png")
    plt.close()
    print("✅ Saved: global_cases_trend.png")

    # Visualization 2: Top Affected Countries
    top_countries = df.groupby("location")["total_cases"].max().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    top_countries.plot(kind="bar", title="Top Affected Countries (Total Cases)")
    plt.ylabel("Total Cases")
    plt.savefig("visualizations/top_affected_countries.png")
    plt.close()
    print("✅ Saved: top_affected_countries.png")

    # Visualization 3: Deaths vs Cases Correlation
    plt.figure(figsize=(8, 6))
    df.plot(x="total_cases", y="total_deaths", kind="scatter", alpha=0.3)
    plt.title("Deaths vs Cases Correlation")
    plt.savefig("visualizations/deaths_vs_cases_analysis.png")
    plt.close()
    print("✅ Saved: deaths_vs_cases_analysis.png")


    # Visualization 4: Vaccination vs Deaths
    if "total_vaccinations" in df.columns:
        vacc_death_df = df[["total_vaccinations", "total_deaths"]].dropna()

        plt.figure(figsize=(8, 6))
        plt.scatter(vacc_death_df["total_vaccinations"],
                    vacc_death_df["total_deaths"],
                    alpha=0.3)
        plt.title("Vaccinations vs Deaths")
        plt.xlabel("Total Vaccinations")
        plt.ylabel("Total Deaths")
        plt.savefig("visualizations/vaccination_vs_deaths.png")
        plt.close()
        print("✅ Saved: vaccination_vs_deaths.png")
    else:
        print("⚠️ 'total_vaccinations' column not found in dataset, skipping plot.")


    # Key Statistics
    total_cases = df["total_cases"].max()
    total_deaths = df["total_deaths"].max()
    fatality_rate = (total_deaths / total_cases) * 100
    peak_day = df.loc[df["new_cases"].idxmax()]

    print("\n📋 Key Statistics Summary:")
    print("=" * 50)
    print(f"🌍 Global Statistics:")
    print(f"• Total Cases: {total_cases:,}")
    print(f"• Total Deaths: {total_deaths:,}")
    print(f"• Global Fatality Rate: {fatality_rate:.2f}%")
    print("\n📈 Peak Daily Cases:")
    print(f"• Date: {peak_day['date']}")
    print(f"• Cases: {int(peak_day['new_cases']):,}")
    print("\n✅ EDA Analysis Complete! Check the 'visualizations' folder.")

    return df  # optional, in case you want to use it elsewhere

if __name__ == "__main__":
    run_eda()



# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
# from datetime import datetime
# import os

# # Set style for better-looking plots
# plt.style.use('seaborn-v0_8')
# sns.set_palette("husl")

# def create_visualizations():
#     """Create 3 key visualizations for COVID-19 data analysis"""
    
#     print("📊 Starting EDA Analysis...")
    
#     # Load cleaned data
#     df = pd.read_csv('data/processed/covid_data_clean.csv')
#     df['date'] = pd.to_datetime(df['date'])
#     print(f"📈 Loaded clean dataset: {df.shape}")
    
#     # Create visualizations directory
#     os.makedirs('visualizations', exist_ok=True)
    
#     # VISUALIZATION 1: Global Cases Trend Over Time
#     print("\n📈 Creating Visualization 1: Global Cases Trend...")
    
#     # Aggregate global data by date
#     global_daily = df.groupby('date').agg({
#         'new_cases': 'sum',
#         'total_cases': 'sum',
#         'new_deaths': 'sum'
#     }).reset_index()
    
#     # Create 7-day rolling average for smoother trends
#     global_daily['new_cases_7day'] = global_daily['new_cases'].rolling(window=7).mean()
#     global_daily['new_deaths_7day'] = global_daily['new_deaths'].rolling(window=7).mean()
    
#     # Plot
#     fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
    
#     # Daily new cases
#     ax1.plot(global_daily['date'], global_daily['new_cases_7day'], 
#              color='#e74c3c', linewidth=2, label='7-day average')
#     ax1.fill_between(global_daily['date'], 0, global_daily['new_cases_7day'], 
#                      color='#e74c3c', alpha=0.3)
#     ax1.set_title('Global Daily New COVID-19 Cases (2020-2023)', fontsize=16, fontweight='bold')
#     ax1.set_ylabel('New Cases per Day', fontsize=12)
#     ax1.legend()
#     ax1.grid(True, alpha=0.3)
    
#     # Cumulative cases
#     ax2.plot(global_daily['date'], global_daily['total_cases'], 
#              color='#3498db', linewidth=2)
#     ax2.fill_between(global_daily['date'], 0, global_daily['total_cases'], 
#                      color='#3498db', alpha=0.3)
#     ax2.set_title('Global Cumulative COVID-19 Cases', fontsize=16, fontweight='bold')
#     ax2.set_xlabel('Date', fontsize=12)
#     ax2.set_ylabel('Total Cases', fontsize=12)
#     ax2.grid(True, alpha=0.3)
    
#     # Format y-axis
#     ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1e6:.1f}M'))
#     ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1e9:.1f}B'))
    
#     plt.tight_layout()
#     plt.savefig('visualizations/global_cases_trend.png', dpi=300, bbox_inches='tight')
#     plt.close()
#     print("✅ Saved: global_cases_trend.png")
    
#     #  VISUALIZATION 2: Top 15 Most Affected Countries 
#     print("\n🌍 Creating Visualization 2: Top Affected Countries...")
    
#     # Get latest data for each country
#     latest_data = df.loc[df.groupby('location')['date'].idxmax()]
    
#     # Sort by total cases and get top 15
#     top_countries = latest_data.nlargest(15, 'total_cases')
    
#     # Create subplot for cases and deaths
#     fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
#     # Total cases bar chart
#     bars1 = ax1.barh(top_countries['location'], top_countries['total_cases'], 
#                      color='#e74c3c')
#     ax1.set_title('Top 15 Countries by Total COVID-19 Cases', fontsize=14, fontweight='bold')
#     ax1.set_xlabel('Total Cases', fontsize=12)
#     ax1.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1e6:.0f}M'))
    
#     # Add value labels on bars
#     for i, bar in enumerate(bars1):
#         width = bar.get_width()
#         ax1.text(width + width*0.01, bar.get_y() + bar.get_height()/2, 
#                 f'{width/1e6:.1f}M', ha='left', va='center', fontweight='bold')
    
#     # Cases per 100k population
#     top_per_capita = latest_data.nlargest(15, 'cases_per_100k')
#     bars2 = ax2.barh(top_per_capita['location'], top_per_capita['cases_per_100k'], 
#                      color='#f39c12')
#     ax2.set_title('Top 15 Countries by Cases per 100k Population', fontsize=14, fontweight='bold')
#     ax2.set_xlabel('Cases per 100k Population', fontsize=12)
    
#     # Add value labels on bars
#     for i, bar in enumerate(bars2):
#         width = bar.get_width()
#         ax2.text(width + width*0.01, bar.get_y() + bar.get_height()/2, 
#                 f'{width:,.0f}', ha='left', va='center', fontweight='bold')
    
#     plt.tight_layout()
#     plt.savefig('visualizations/top_affected_countries.png', dpi=300, bbox_inches='tight')
#     plt.close()
#     print("✅ Saved: top_affected_countries.png")
    
#     #  VISUALIZATION 3: Deaths vs Cases Correlation Analysis 
#     print("\n💀 Creating Visualization 3: Deaths vs Cases Correlation...")
    
#     # Prepare data for correlation analysis
#     country_summary = latest_data[latest_data['total_cases'] > 10000].copy()  # Focus on significantly affected countries
    
#     # Calculate case fatality rate
#     country_summary['fatality_rate'] = (country_summary['total_deaths'] / country_summary['total_cases']) * 100
#     country_summary = country_summary[country_summary['fatality_rate'] < 10]  # Remove outliers
    
#     # Create subplot
#     fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    
#     # Scatter plot: Total Cases vs Total Deaths
#     scatter1 = ax1.scatter(country_summary['total_cases'], country_summary['total_deaths'], 
#                           c=country_summary['fatality_rate'], s=60, alpha=0.7, 
#                           cmap='Reds', edgecolors='black', linewidth=0.5)
    
#     # Add trend line
#     z = np.polyfit(country_summary['total_cases'], country_summary['total_deaths'], 1)
#     p = np.poly1d(z)
#     ax1.plot(country_summary['total_cases'], p(country_summary['total_cases']), 
#              "r--", alpha=0.8, linewidth=2)
    
#     ax1.set_title('COVID-19: Total Cases vs Total Deaths by Country', fontsize=14, fontweight='bold')
#     ax1.set_xlabel('Total Cases', fontsize=12)
#     ax1.set_ylabel('Total Deaths', fontsize=12)
#     ax1.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1e6:.0f}M'))
#     ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1e3:.0f}K'))
    
#     # Add colorbar
#     cbar1 = plt.colorbar(scatter1, ax=ax1)
#     cbar1.set_label('Case Fatality Rate (%)', fontsize=10)
    
#     # Case Fatality Rate distribution
#     ax2.hist(country_summary['fatality_rate'], bins=20, color='#e74c3c', 
#              alpha=0.7, edgecolor='black')
#     ax2.axvline(country_summary['fatality_rate'].mean(), color='blue', 
#                 linestyle='--', linewidth=2, label=f'Mean: {country_summary["fatality_rate"].mean():.1f}%')
#     ax2.axvline(country_summary['fatality_rate'].median(), color='green', 
#                 linestyle='--', linewidth=2, label=f'Median: {country_summary["fatality_rate"].median():.1f}%')
    
#     ax2.set_title('Distribution of Case Fatality Rates by Country', fontsize=14, fontweight='bold')
#     ax2.set_xlabel('Case Fatality Rate (%)', fontsize=12)
#     ax2.set_ylabel('Number of Countries', fontsize=12)
#     ax2.legend()
#     ax2.grid(True, alpha=0.3)
    
#     plt.tight_layout()
#     plt.savefig('visualizations/deaths_vs_cases_analysis.png', dpi=300, bbox_inches='tight')
#     plt.close()
#     print("✅ Saved: deaths_vs_cases_analysis.png")
    
#     # ========== SUMMARY STATISTICS ==========
#     print("\n📋 Key Statistics Summary:")
#     print("=" * 50)
    
#     # Global totals
#     total_cases = latest_data['total_cases'].sum()
#     total_deaths = latest_data['total_deaths'].sum()
#     global_fatality_rate = (total_deaths / total_cases) * 100
    
#     print(f"🌍 Global Statistics:")
#     print(f"   • Total Cases: {total_cases:,.0f}")
#     print(f"   • Total Deaths: {total_deaths:,.0f}")
#     print(f"   • Global Fatality Rate: {global_fatality_rate:.2f}%")
    
#     # Peak information
#     peak_day = global_daily.loc[global_daily['new_cases'].idxmax()]
#     print(f"\n📈 Peak Daily Cases:")
#     print(f"   • Date: {peak_day['date'].strftime('%Y-%m-%d')}")
#     print(f"   • Cases: {peak_day['new_cases']:,.0f}")
    
#     # Most affected countries
#     print(f"\n🔝 Most Affected Countries (Total Cases):")
#     for i, (idx, country) in enumerate(top_countries[['location', 'total_cases']].iterrows()):
#         if i < 5:  # Show top 5
#             print(f"   {i+1}. {country['location']}: {country['total_cases']:,.0f}")
    
#     print("\n✅ EDA Analysis Complete! Check the 'visualizations' folder.")

# if __name__ == "__main__":
#     create_visualizations()