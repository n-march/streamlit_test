import pandas as pd
import os

# Define the directory path where your CSV files are located
directory = 'path/to/csv/files'

# Create an empty dictionary to store the file names and their corresponding data frames
data_frames = {}

# Iterate over the CSV files in the directory, read each file into a data frame, and store it in the dictionary
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        df = pd.read_csv(file_path)
        data_frames[filename] = df

# Compare the structure of the data frames
columns_set = set()
for filename, df in data_frames.items():
    columns_set.add(tuple(df.columns))

if len(columns_set) > 1:
    print("Column names are different across the data frames.")
else:
    print("Column names are the same across the data frames.")
