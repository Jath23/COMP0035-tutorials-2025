from pathlib import Path

#.parent is done two times to get from this python file to the src folder 
# (from this file to Solutions folder and then from the Solution folder to the src folder)
project_root = Path(__file__).parent.parent

# Then find the .csv file relative to the src folder and join to that path the activities folder, then the data folder and finally the paralympics_raw.csv file
csv_file = project_root.joinpath('activities','data', 'paralympics_raw.csv')

# Check if the file exists, this will print 'true' if it exists
print(csv_file.exists())
