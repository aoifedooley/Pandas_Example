import pandas as pd

# df = pd.read_csv(r"C:\Users\Public\Aoife DA Course\Pandas Example\netflix_titles.csv")
df = pd.read_csv(r"C:\Users\ained\Documents\Aoife\PyCharm Projects\Pandas Example\netflix_titles.csv")

# First 5 rows
print("FIRST 5 ROWS")
print(df.head())
print()

# Last 5 rows
print("LAST 5 ROWS")
print(df.tail())
print()

# Number of columns and rows
print("# OF COLUMNS AND ROWS")
print(df.shape)
print()

# Column titles
print("COLUMN TITLES")
print(df.columns)
print()

# Data types
print("DATA TYPES")
print(df.dtypes)
print()

# Show date added
print("SHOW DATE ADDED")
df['date_added'] = pd.to_datetime(df['date_added'])
print(df['date_added'])
print()

# Checking for any null values
print("CHECK IF NULL VALUES PRESENT")
print(df.isnull())
print("TOTAL NUMBER OF NULL VALUES")
print(df.isnull().sum())
print()

# dropna() functions drops missing values
print("DROP ROWS W/ MISSING VALUES")
df_row = df.dropna(axis=0)
# Show new total with dropped rows
print(df_row.shape)
print()
print("DROP COLUMNS W/ MISSING VALUES")
df_row = df.dropna(axis=1)
# Show new total with dropped columns
print(df_row.shape)
print()

# Use fillna() function to fill missing values
print("FORWARD FILL BY ROW")
df_filled = df.fillna(method="ffill", axis=0).fillna(0)
print(df_filled.isnull().sum())
print()

# Check for duplicate values
print("CHECK FOR DUPLICATE VALUES")
print(df[(df.duplicated())])
print()

# Drop duplicate values using show_id as key
print("DROP DUPLICATE VALUES")
drop_dup = df.drop_duplicates(subset=['show_id'])
print(drop_dup)
print()

# How to slice a DataFrame
print("PRINT FIRST 100 ROWS")

# loc function - column names
print("USING THE loc FUNCTION")
first_100_rows_loc = df.loc[0:100,"show_id":"country"]
print(first_100_rows_loc)
print()

# iloc function - column indexes
print("USING THE iloc FUNCTION")
first_100_rows_iloc = df.iloc[0:100,0:6]
print(first_100_rows_iloc)
print()

# Choose specific rows by passing a list
print("PASS LIST - PRINT SPECIFIC ROWS")
print(df.loc[[300,443,7000]])
print()
