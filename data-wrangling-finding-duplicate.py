import pandas as pd
import matplotlib.pyplot as plt

url = 'survey_data_with_duplicate.csv'

df = pd.read_csv(url)
print(df.shape)
#print(df.head())

#Calculating duplicate rows, comparing all columns, in each row.
duplicate_count = df.duplicated().sum()
print('Number of duplicate rows: ', duplicate_count)

# View duplicate rows.
duplicate_rows = df[df.duplicated()]
print('Number of duplicate rows: ', duplicate_rows.shape) #(rows,columns)
#print(duplicate_rows.head())

# Calculating duplicate rows, comparing three columns, in each row.
dup_subset = df[df.duplicated(subset=['MainBranch', 'Employment', 'RemoteWork'])]
print('Number of duplicate subset: ', dup_subset.shape)

# Visulaize duplicate distribution by Country

duplicate_countries = dup_subset['Country'].value_counts()
duplicate_countries.plot(kind='bar', figsize=(10,5))
plt.title("Duplicate Distribution by Country")
plt.xlabel("Country")
plt.ylabel("Number of Duplicates")
plt.show()

# Visulaize duplicate distribution by Employment
duplicate_employment = dup_subset['Employment'].value_counts()
duplicate_employment.plot(kind='pie', autopct='%1.1f%%', figsize=(7,7))
plt.title("Duplicate Distribution by Employment")
plt.show()

# Remove duplicate records, comparing three columns.
unique_pattern = df[['MainBranch', 'Employment', 'RemoteWork']].drop_duplicates()
print("Unique combinations:", unique_pattern.shape)

print()
print("Original rows:", df.shape[0]) #.shape[0] returns only rows, not column.
print("Duplicates:", df.shape[0] - unique_pattern.shape[0])
print()
print("Unique patterns:", unique_pattern.shape[0])


