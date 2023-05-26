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

def file_identification():
    import os
    import csv

    directory = 'path/to/files'

    def identify_file_with_decode_error(directory):
        for filename in os.listdir(directory):
            if filename.endswith('.csv'):  # Adjust the file extension as needed
                file_path = os.path.join(directory, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        csv_reader = csv.reader(file)
                        # Perform any necessary processing on the CSV file
                except UnicodeDecodeError:
                    print(f"UnicodeDecodeError occurred in file: {file_path}")
                    # Handle the file with the error as needed
                    # You can choose to skip it or perform any necessary action

    # Call the function to identify the file with a UnicodeDecodeError
    identify_file_with_decode_error(directory)

