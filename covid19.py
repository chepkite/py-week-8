import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud




""" Load COVID-19 data from a CSV file """
def load_covid_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

 # display the first 10 rows of the dataframe
    
df = load_covid_data("metadata.csv")
print(df.head())

# shape of the dataframe
print(f"Dataframe shape: {df.shape}")
 
 # data types of each column
print(f"Data types:\n{df.dtypes}")

# mising values in each column
print(f"Missing values:\n{df.isnull().sum()}")

# basic statistics of numerical columns
print(f"Basic statistics:\n{df.describe()}")

# check the % of missing values in each column
missing_percentage = df.isnull().mean() * 100
print(f"Missing values percentage:\n{missing_percentage}")

# drop columns with more than 50% missing values
df_clean = df.drop(columns=missing_percentage[missing_percentage > 50].index)
print(f"Dataframe shape after dropping columns with >50% missing values: {df_clean.shape}")

# drop rows with any missing values
df_clean = df_clean.dropna(subset=['tittle', 'publish time'])
print(f"Dataframe shape after dropping rows with any missing values: {df_clean.shape}") 
print(df_clean.head())

# convert 'publish time' to datetime
df_clean['publish time'] = pd.to_datetime(df_clean['publish time'], errors='coerce')

# extract year, month, day, and weekday from 'publish time'
df_clean['year'] = df_clean['publish time'].dt.year
df_clean['month'] = df_clean['publish time'].dt.month
df_clean['day'] = df_clean['publish time'].dt.day
df_clean['weekday'] = df_clean['publish time'].dt.day_name()

# abstract word count
df_clean['abstract_word_count'] = df_clean['abstract'].apply(lambda x: len(str(x).split()))
print(df_clean[['publish time', 'year', 'month', 'day', 'weekday', 'abstract_word_count']].head())


# years count
year_counts = df_clean['year'].value_counts().sort_index()

# visualize the number of publications per year
plt.figure(figsize=(10, 6))
sns.barplot(x=year_counts.index, y=year_counts.values, palette='viridis')
plt.title('Number of Publications per Year')
plt.xlabel('Year')
plt.ylabel('Number of Publications')
plt.show()

# months count
month_counts = df_clean['month'].value_counts().sort_index()
# visualize the number of publications per month
plt.figure(figsize=(10, 6))
sns.barplot(x=month_counts.index, y=month_counts.values, palette='magma')
plt.title('Number of Publications per Month')
plt.xlabel('Month')
plt.ylabel('Number of Publications')
plt.show()

# weekdays count
weekday_counts = df_clean['weekday'].value_counts().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
# visualize the number of
plt.figure(figsize=(10, 6))
sns.barplot(x=weekday_counts.index, y=weekday_counts.values, palette='coolwarm')
plt.title('Number of Publications per Weekday')
plt.xlabel('Weekday')
plt.ylabel('Number of Publications')
plt.show()














