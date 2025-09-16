# ==============================================================================
# Assignment: Data Loading, Analysis, and Visualization with Pandas
# ==============================================================================

# --- Import necessary libraries ---
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris # To get a sample dataset

# --- Main function to orchestrate the analysis ---
def main():
    """
    Main function to run the entire data analysis pipeline.
    """
    print("🚀 Starting Data Analysis Workflow...")

    # Task 1: Load and Explore the Dataset
    print("\n--- Task 1: Loading and Exploring the Dataset ---")
    
    try:
        # Load the Iris dataset from scikit-learn
        iris_bunch = load_iris()
        # Create a pandas DataFrame from the loaded data
        # We combine the feature data and the target (species) column
        iris_df = pd.DataFrame(data=iris_bunch.data, columns=iris_bunch.feature_names)
        iris_df['species'] = pd.Categorical.from_codes(iris_bunch.target, iris_bunch.target_names)
        
        print("✅ Dataset loaded successfully.")
        
        # Display the first few rows to inspect the data
        print("\nFirst 5 rows of the dataset:")
        print(iris_df.head())

        # Explore the structure: data types and missing values
        print("\nDataset structure and info:")
        # .info() checks data types and non-null counts
        iris_df.info()

        # Clean the dataset 
        iris_df.fillna(value, inplace=True) # To fill missing values
        iris_df.dropna(inplace=True)        # To drop rows with missing values
        print("\nDataset is clean. No missing values to handle.")

    except Exception as e:
        # Error handling for any potential issues during loading
        print(f"❌ An error occurred during data loading: {e}")
        return # Stop the script if data can't be loaded

    # Task 2: Basic Data Analysis
    print("\n--- Task 2: Performing Basic Data Analysis ---")

    # Compute basic statistics of numerical columns
    print("\nBasic statistical summary:")
    # .describe() provides mean, median (50%), std, min, max, etc.
    print(iris_df.describe())

    # Perform groupings on a categorical column ('species') and compute the mean
    print("\nAverage measurements per species:")
    species_mean = iris_df.groupby('species').mean()
    print(species_mean)
    
    # Identify patterns or interesting findings
    print("\nFindings from Analysis:")
    print("- The 'setosa' species is distinctly smaller than the other two species in terms of petal length/width and sepal length.")
    print("- 'Virginica' is generally the largest species, especially in petal measurements.")
    print("- 'Sepal width' is less distinct between species compared to other features.")

    # Task 3: Data Visualization
    print("\n--- Task 3: Creating Data Visualizations ---")
    
    # Set a nice style for the plots using seaborn
    sns.set_theme(style="whitegrid")

    # --- 1. Line Chart ---
    # Iris doesn't have a time-series, so we'll plot sepal length for the first 50 samples as an example trend.
    plt.figure(figsize=(10, 6))
    plt.plot(iris_df.index[:50], iris_df['sepal length (cm)'][:50], marker='o', linestyle='--')
    plt.title('Sepal Length Trend for First 50 Samples (Example Line Chart)')
    plt.xlabel('Sample Index')
    plt.ylabel('Sepal Length (cm)')
    plt.grid(True)
    plt.show()

    # --- 2. Bar Chart ---
    # We can visualize the average measurements per species from our analysis in Task 2.
    species_mean.plot(kind='bar', figsize=(12, 7))
    plt.title('Average Measurements by Iris Species')
    plt.xlabel('Species')
    plt.ylabel('Average Measurement (cm)')
    plt.xticks(rotation=0) # Keep the species names horizontal
    plt.legend(title='Measurement Type')
    plt.tight_layout()
    plt.show()
    
    # --- 3. Histogram ---
    # Understand the distribution of a single numerical column.
    plt.figure(figsize=(10, 6))
    sns.histplot(iris_df['petal length (cm)'], kde=True, bins=20)
    plt.title('Distribution of Petal Length')
    plt.xlabel('Petal Length (cm)')
    plt.ylabel('Frequency')
    plt.show()

    # --- 4. Scatter Plot ---
    # Visualize the relationship between two numerical columns.
    # We use 'hue' to color the points by species, which is highly insightful.
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=iris_df, x='sepal length (cm)', y='petal length (cm)', hue='species', s=80)
    plt.title('Sepal Length vs. Petal Length by Species')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend(title='Species')
    plt.show()
    
    print("\n✅ Visualizations created successfully.")
    print("🎉 Data Analysis Workflow Complete!")


# --- Run the main function when the script is executed ---
if __name__ == "__main__":
    main()