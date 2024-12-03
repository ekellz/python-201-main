# Adapt your file counter script so that it records more different file types
# in your CSV file. Remember that the format of your output needs to be
# consistent across multiple runs of your script. This means you'll need to
# make a compromise and choose which file types you want to record beforehand.

import pathlib
import csv

# Define the path to the directory
directory = pathlib.Path('/Users/ericajansen/Documents/codingnomads/python-201-main/03_file-input-output')
output_csv_path = directory / 'file_counts.csv'

# Create a list of file types to count
file_types = ['txt', 'csv', 'py']

# Prep the dict
file_counts = {file_type:0 for file_type in file_types}

# Iterate through the directory
for file in directory.iterdir():
    if file.is_file():
        file_ext = file.suffix[1:]
        if file_ext in file_counts:
            file_counts[file_ext] += 1

# Write the results to a CSV file  
with output_csv_path.open('w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['file_type', 'Count'])
    for file_type, count in file_counts.items():
        writer.writerow([file_type, count])

print(output_csv_path)