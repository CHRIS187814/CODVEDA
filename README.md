# Data Cleaning and Exploratory Data Analysis (EDA) with Pandas and Seaborn

## Overview
This project focuses on data cleaning and exploratory data analysis (EDA) using Pandas and Seaborn. The script handles missing values, removes duplicates, standardizes data formats, calculates summary statistics, and visualizes data distributions and relationships.

## Features
- Load and preprocess dataset (CSV file)
- Handle missing values with appropriate imputation techniques
- Remove duplicate records
- Standardize inconsistent data formats (dates, categorical values)
- Compute summary statistics (mean, median, mode, standard deviation)
- Analyze numerical feature correlations
- Generate various visualizations:
  - Histograms
  - Boxplots
  - Scatter plots
  - Bar plots
  - Line charts
  - Correlation heatmaps
- Export cleaned data and visualizations

## Installation
Ensure you have Python and the required libraries installed:
```bash
pip install pandas matplotlib seaborn
```

## Usage
Run the script with:
```bash
python data_cleaning_eda.py
```

## Output
The script generates:
- A cleaned dataset (`cleaned_data.csv`)
- Various visualization images (e.g., `age_distribution.png`, `correlation_heatmap.png`)
- Summary statistics and insights printed in the terminal

## Visualizations
- **Histogram:** Distribution of numerical features
- **Boxplot:** Outliers and spread of numerical data
- **Scatter Plot:** Relationship between two numerical variables
- **Bar Plot:** Frequency of categorical variables
- **Line Chart:** Trends over time
- **Heatmap:** Correlation matrix visualization

## Author
Chris

## License
This project is licensed under the MIT License.

