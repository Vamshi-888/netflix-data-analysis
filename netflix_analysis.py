
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['year_added'] = df['date_added'].dt.year
    df = df.dropna(subset=['country', 'rating'])
    return df

def plot_content_type(df):
    df['type'].value_counts().plot(kind='bar', color='skyblue')
    plt.title('Movies vs TV Shows')
    plt.show()

def plot_year_trend(df):
    df['year_added'].value_counts().sort_index().plot(marker='o', color='green')
    plt.title('Content Added Over Years')
    plt.show()

def plot_top_countries(df):
    df['country'].value_counts().head(10).plot(kind='barh', color='orange')
    plt.title('Top 10 Countries')
    plt.show()

def plot_top_genres(df):
    genres = df['listed_in'].str.split(',').explode().str.strip()
    genres.value_counts().head(10).plot(kind='bar', color='purple')
    plt.title('Top 10 Genres')
    plt.xticks(rotation=45)
    plt.show()

def run_analysis(path):
    df = load_data(path)
    df = clean_data(df)
    plot_content_type(df)
    plot_year_trend(df)
    plot_top_countries(df)
    plot_top_genres(df)

run_analysis('netflix_titles.csv')
