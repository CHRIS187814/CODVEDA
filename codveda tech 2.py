import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#TASK 1: WORK WITH A RAW DATASET

# Create a sample dataset
data = {
    'id': [1, 2, 2, 3, 4, 5, 6, None, 8, 9],
    'name': ['Alice', 'Bob', 'Bob', 'Charlie', 'David', 'Eve', None, 'Grace', 'Heidi', 'Ivan'],
    'age': [25, None, 30, 35, 40, 29, 50, 22, None, 27],
    'date': ['2023-01-01', '2023/02/15', '15-03-2023', None, '2023-05-10', '2023-06-25', 'July 7, 2023', '2023-08-15', '2023-09-01', '2023-10-10'],
    'category': [' A', 'b', 'B', 'C', 'd', 'D', None, 'A ', ' b ', 'C']
}

df = pd.DataFrame(data)

# Save sample dataset
df.to_csv('sample_data.csv', index=False)

# Load dataset
df = pd.read_csv('sample_data.csv')

# Display initial dataset info
print("Initial Dataset Info:")
df.info()

# Handling missing values
df = df.copy()  # Avoid SettingWithCopyWarning
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].fillna(df[col].mode()[0])  # Fill categorical with mode
    else:
        df[col] = df[col].fillna(df[col].median())  # Fill numerical with median

# Remove duplicate rows
df = df.drop_duplicates()

# Standardize date format
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Standardize categorical values
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    df[col] = df[col].str.lower().str.strip()

# Display cleaned dataset info
print("\nCleaned Dataset Info:")
df.info()

# Save cleaned dataset
df.to_csv('cleaned_data.csv', index=False)
print("\nData cleaning complete. Cleaned dataset saved as 'cleaned_data.csv'.")



#PERFORMING EDA AND BASIC DATA VISUALIZATIONS

# Exploratory Data Analysis (EDA)
print("\nBasic Statistics:")
print(df.describe())

# Summary Statistics
print("\nSummary Statistics:")
print("Mean:\n", df.mean(numeric_only=True))
print("\nMedian:\n", df.median(numeric_only=True))
print("\nMode:\n", df.mode().iloc[0])
print("\nStandard Deviation:\n", df.std(numeric_only=True))

# Visualizations
plt.figure(figsize=(10, 6))
sns.histplot(df['age'], bins=10, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig('age_distribution.png')
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x=df['age'])
plt.title('Boxplot of Age')
plt.xlabel('Age')
plt.savefig('boxplot_age.png')
plt.show()

# Correlation Heatmap
print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.savefig('correlation_heatmap.png')
plt.show()

# Category Distribution (Bar Plot)
plt.figure(figsize=(8, 5))
sns.countplot(x=df['category'])
plt.title('Category Distribution')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.savefig('category_distribution.png')
plt.show()

# Scatter Plot (Example: Age vs ID)
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['id'], y=df['age'])
plt.title('Scatter Plot of Age vs ID')
plt.xlabel('ID')
plt.ylabel('Age')
plt.savefig('scatter_age_id.png')
plt.show()

# Line Chart Example
plt.figure(figsize=(8, 5))
if 'date' in df.columns and not df['date'].isna().all():
    df_sorted = df.sort_values(by='date')
    plt.plot(df_sorted['date'], df_sorted['age'], marker='o', linestyle='-')
    plt.title('Age Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Age')
    plt.xticks(rotation=45)
    plt.savefig('age_trend.png')
    plt.show()

print("\nEDA complete. Plots saved as images.")
