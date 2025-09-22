CORD-19 Research Dataset: An Exploratory Analysis

Objective:
The goal of this project was to load, clean, and analyze the CORD-19 research paper metadata. The analysis focused on identifying trends in publication volume, top contributing journals, and key research topics. The final outcome is an interactive Streamlit application to explore these findings.

Data Preparation:
The initial dataset contained over 1 million records with numerous columns. The following data cleaning and preparation steps were performed:
Handling Missing Data: Rows with missing essential information (title, abstract, journal, publication time) were removed to ensure the quality of the analysis.
Date Conversion: The publish_time column was converted from a text format to a proper datetime format.
Feature Engineering: A year column was extracted from the publication date to facilitate time-based analysis.

Key Findings:
Explosion in Research: The visualization of publications over time clearly shows a massive surge in COVID-19 related research papers in 2020. This reflects the global scientific community's rapid response to the pandemic. The number of publications remained high in subsequent years.
Top Publishing Journals: A small number of journals were responsible for a large volume of publications. The analysis identified the top 10 most prolific journals, with journals like PLoS One and Scientific Reports leading the way.
Dominant Data Sources: The papers in the dataset were primarily sourced from a few major repositories. The analysis showed that sources like PMC and Medline were the most significant contributors.
(Optional: Word Cloud Insight): The word cloud of paper titles highlighted common themes in the research, with terms like "patient," "viral," "clinical," "cells," and "infection" being highly prominent, indicating a strong focus on the clinical and biological aspects of the virus.

Conclusion:
This project successfully demonstrated a complete data analysis workflow, from raw data to an interactive web application. The analysis revealed clear patterns in the scientific response to the COVID-19 pandemic. The resulting Streamlit app provides an accessible way for users to explore these trends for themselves.

3. Reflect on Challenges and Learning

Potential Challenges You Might Have Faced:
Data Size: "The metadata.csv file was very large, which made initial loading slow. Using low_memory=False helped, but I learned that for even bigger datasets, I might need tools like Dask or to load the data in chunks."
Data Messiness: "The publish_time column contained various formats and some non-date strings. Using errors='coerce' in pd.to_datetime was essential for handling this without crashing the script."
Streamlit Layout: "Getting the plots to appear side-by-side required learning about st.columns. It took some experimentation to get the layout right."
Visualization Choices: "Initially, I used a vertical bar chart for the top journals, but the labels overlapped. I learned that a horizontal bar chart (orient='h' or swapping x/y in Seaborn) is much better for long category labels."

Key Learnings:
The Data Science Workflow: "I now have a practical understanding of the end-to-end process: loading data, cleaning it (which took a surprising amount of effort), analyzing it to find patterns, and finally, presenting the results in an interactive way."
Pandas Power: "I became much more comfortable with key pandas functions like .dropna(), .to_datetime(), the .dt accessor, and .value_counts()."
The Value of Visualization: "A table of numbers (like the top journals) is hard to interpret, but a bar chart makes the key insights immediately obvious."
Rapid Prototyping with Streamlit: "I was amazed at how quickly I could turn a data analysis script into a functional web app without needing to know any HTML, CSS, or JavaScript."
