# plant_monitoring.py

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Use Seaborn theme for nicer visuals
sns.set_theme(style="whitegrid")

JSON_URL = "https://get.data.gov.lt/datasets/gov/lzukt/Ivertis"

# ------------------------
# 1. Fetch Data
# ------------------------
def fetch_data():
    try:
        response = requests.get(JSON_URL)
        response.raise_for_status()
        json_data = response.json()
        data = json_data.get("_data", json_data)
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()

# ------------------------
# 2. Clean Data
# ------------------------
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns={
        "_id": "vda_id",
        "stebejimo_data": "observation_date",
        "augalo_pavadinimas": "plant_name",
        "ligos_kenkejo_pavadinimas": "disease_pest_name",
        "ligos_kenkejo_pavadinimas_lot": "disease_pest_name_lot",
        "zalingumo_ivertis": "harm_value",
        "pazeidimo_lygis": "violation_level",
        "savivaldybe": "municipality"
    })

    # Parse date (dayfirst=True for European dates)
    df['observation_date'] = pd.to_datetime(df['observation_date'], errors='coerce', dayfirst=True)

    # Convert harm_value to numeric
    df['harm_value'] = pd.to_numeric(df['harm_value'], errors='coerce')

    # Drop rows missing essential values
    df = df.dropna(subset=['plant_name', 'harm_value'])

    # Keep only rows with valid dates
    df = df[df['observation_date'].notna()]
    return df

# ------------------------
# 3. Get Raw Records
# ------------------------
def get_raw(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    return df.head(n)

# ------------------------
# 4. Top 5 Plants
# ------------------------
def get_top_plants(df: pd.DataFrame, top_n: int = 5) -> pd.DataFrame:
    return (df.groupby('plant_name')['harm_value']
              .sum()
              .sort_values(ascending=False)
              .head(top_n)
              .reset_index(name='total_harm'))

# ------------------------
# 5. Yearly Trend
# ------------------------
def get_yearly_trend(df: pd.DataFrame) -> pd.DataFrame:
    df['year'] = df['observation_date'].dt.year
    trend = df.groupby('year')['harm_value'].sum().reset_index(name='total_harm')
    return trend

# ------------------------
# 6. Visualizations
# ------------------------
def plot_top_plants(df: pd.DataFrame):
    plt.figure(figsize=(10,6))
    bar = sns.barplot(x='total_harm', y='plant_name', data=df, color="mediumseagreen")
    plt.title("Top Plants by Harm Value", fontsize=16)
    plt.xlabel("Total Harm Value", fontsize=12)
    plt.ylabel("Plant Name", fontsize=12)

    # Add value labels
    for i, v in enumerate(df['total_harm']):
        bar.text(v + 20, i, str(round(v,1)), color='black', va='center')

    plt.tight_layout()
    plt.show()

def plot_yearly_trend(df: pd.DataFrame):
    plt.figure(figsize=(10,6))
    sns.lineplot(x='year', y='total_harm', data=df, marker='o', linewidth=2.5, color="coral")
    plt.fill_between(df['year'], df['total_harm'], alpha=0.2, color="coral")
    plt.title("Yearly Harm Trend", fontsize=16)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Total Harm Value", fontsize=12)
    plt.xticks(df['year'].unique())
    plt.tight_layout()
    plt.show()

# ------------------------
# 7. Main Execution
# ------------------------
if __name__ == "__main__":
    df_raw = fetch_data()
    print("Columns from API:", df_raw.columns.tolist())

    df_clean = clean_data(df_raw)

    print("First 10 Records:")
    print(get_raw(df_clean))

    print("\nTop 5 Plants:")
    top_plants = get_top_plants(df_clean)
    print(top_plants)
    plot_top_plants(top_plants)

    print("\nYearly Trend:")
    yearly_trend = get_yearly_trend(df_clean)
    print(yearly_trend)
    plot_yearly_trend(yearly_trend)
