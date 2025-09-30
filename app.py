import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


st.title("COVID-19 Data Analysis")
st.write("This app analyzes COVID-19 data and provides visualizations.")
st.write("Developed by Sharon Chepkite")

# load and display an image
image = Image.open("covid.png")
st.image(image, caption='COVID-19', use_container_width=True)
st.write("Image from WHO ")

# Load COVID-19 data
df = pd.read_csv("metadata.csv")
# Clean up column names
df.columns = df.columns.str.strip().str.lower()

#st.write("Columns in DataFrame:", df.columns.tolist())

# Convert publish_time to datetime and extract year
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year


# Sidebar for year selection
min_year, max_year = int(df['year'].min()), int(df['year'].max())
year_range = st.slider("Select year range", min_year, max_year, (min_year, max_year))

# Filter data
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Display basic info
st.write(f"Data from {year_range[0]} to {year_range[1]}")
st.dataframe(filtered_df)
st.write(f"Dataframe shape: {filtered_df.shape}")
st.write("Missing values percentage:")
st.write(filtered_df.isnull().mean() * 100)
st.write("Basic statistics:")
st.write(filtered_df.describe())
st.write(filtered_df.head())

# Plot: Publications per year
pubs_per_year = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(pubs_per_year.index, pubs_per_year.values)
ax.set_xlabel('Year')
ax.set_ylabel('Number of Publications')
ax.set_title('Number of Publications per Year')
st.pyplot(fig)


# Show raw data (optional checkbox)
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.dataframe(filtered_df.head(10))



