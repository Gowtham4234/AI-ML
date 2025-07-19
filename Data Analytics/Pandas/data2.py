import pandas as pd

# 1. Load CSV data into a DataFrame
df = pd.read_csv('sample_data.csv')  # Make sure sample_data.csv exists

# 2. Display first 5 rows
print("First 5 rows:\n", df.head())

# 3. Basic information
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())

# 4. Summary statistics
print("\nSummary statistics:\n", df.describe())

# 5. Drop rows with missing values
df_clean = df.dropna()

# 6. Filter data (example: age > 30)
filtered_df = df_clean[df_clean['age'] > 30]
print("\nFiltered rows (age > 30):\n", filtered_df)

# 7. Group by column (example: gender) and calculate mean
grouped = df_clean.groupby('gender')['salary'].mean()
print("\nAverage salary by gender:\n", grouped)

# 8. Add a new column (example: tax = 10% of salary)
df_clean['tax'] = df_clean['salary'] * 0.1

# 9. Sort data by salary descending
sorted_df = df_clean.sort_values(by='salary', ascending=False)
print("\nTop earners:\n", sorted_df.head())

# 10. Save processed data to a new CSV
sorted_df.to_csv('processed_data.csv', index=False)
print("\nProcessed data saved to 'processed_data.csv'")
