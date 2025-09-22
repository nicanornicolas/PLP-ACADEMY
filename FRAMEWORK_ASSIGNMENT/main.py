# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Page Configuration ---
st.set_page_config(
    page_title="CORD-19 Data Explorer",
    layout="wide"
)

# --- Title and Description ---
st.title("CORD-19 Research Paper Explorer")
st.write("This application provides a simple analysis of the CORD-19 dataset, focusing on publication trends, top journals, and key topics.")


# --- Caching the Data Loading ---
@st.cache_data # This decorator caches the data so it doesn't reload on every interaction
def load_and_clean_data(file_path):
    """
    Loads and cleans the CORD-19 metadata.
    """
    df = pd.read_csv(file_path, low_memory=False)
    
    # Select and clean essential columns
    essential_columns = ['title', 'abstract', 'journal', 'publish_time', 'source_x']
    df_cleaned = df.dropna(subset=essential_columns)
    
    # Convert publish_time to datetime and extract year
    df_cleaned['publish_time'] = pd.to_datetime(df_cleaned['publish_time'], errors='coerce')
    df_cleaned.dropna(subset=['publish_time'], inplace=True)
    df_cleaned['year'] = df_cleaned['publish_time'].dt.year
    
    # Filter for a reasonable year range (e.g., post-2000)
    df_cleaned = df_cleaned[df_cleaned['year'] > 2000].copy()
    df_cleaned['year'] = df_cleaned['year'].astype(int)

    return df_cleaned

# Load the data using the function
df = load_and_clean_data('metadata.csv')


# --- Sidebar for Filters ---
st.sidebar.header("Filters")

# Get min and max year from the data for the slider
min_year = int(df['year'].min())
max_year = int(df['year'].max())

# Create a year range slider
selected_year_range = st.sidebar.slider(
    "Select a year range",
    min_value=min_year,
    max_value=max_year,
    value=(2020, max_year) # Default range
)

# Filter the dataframe based on the selected year range
start_year, end_year = selected_year_range
filtered_df = df[(df['year'] >= start_year) & (df['year'] <= end_year)]

st.header(f"Displaying Data from {start_year} to {end_year}")


# --- Main Page Layout ---
# Create two columns for visualizations
col1, col2 = st.columns(2)


with col1:
    st.subheader("Publications Over Time")
    # Analysis
    year_counts = filtered_df['year'].value_counts().sort_index()
    # Visualization
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.lineplot(x=year_counts.index, y=year_counts.values, ax=ax1, marker='o')
    ax1.set_title('Number of Publications by Year')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Number of Papers')
    st.pyplot(fig1)

with col2:
    st.subheader("Top 10 Publishing Journals")
    # Analysis
    top_journals = filtered_df['journal'].value_counts().head(10)
    # Visualization
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax2, palette='mako')
    ax2.set_title('Top 10 Journals by Number of Publications')
    ax2.set_xlabel('Number of Papers')
    ax2.set_ylabel('Journal')
    st.pyplot(fig2)

# --- Show a sample of the data ---
st.subheader("Raw Data Sample")
st.write("A sample of the filtered data.")
st.dataframe(filtered_df[['title', 'journal', 'year', 'source_x']].head(10))