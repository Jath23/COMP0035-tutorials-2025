from pathlib import Path
import pandas as pd
import matplotlib as plt

# Pathing the csv file from another folder within the src folder
# and changing it into a dataframe
src_folder = Path(__file__).parent.parent
csv_file = src_folder.joinpath('activities','data', 'paralympics_raw.csv')
paralympics_df = pd.read_csv(csv_file)

# Printing the types of categorical data and its frequency
print(paralympics_df['type'].unique())
print(paralympics_df['type'].value_counts())

# Repeat for disabilities included column
print(paralympics_df['disabilities_included'].unique())
print(paralympics_df['disabilities_included'].value_counts())
# The issue with this is that a participant can have more than one type of disability
# in other words categorical data