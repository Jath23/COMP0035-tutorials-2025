
from pathlib import Path

import pandas as pd

if __name__ == "__main__":

    #.parent is done two times to get from this python file to the src folder 
    # (from this file to Solutions folder and then from the Solution folder to the src folder)
    src_folder = Path(__file__).parent.parent

    # Then find the .csv file relative to the src folder and join to that path the activities folder, then the data folder and finally the paralympics_raw.csv file
    csv_file = src_folder.joinpath('activities','data', 'paralympics_raw.csv')

    # Check if the file exists, this will print 'true' if it exists
    print(csv_file.exists())

    # Repeat to find the paralympics_all_raw.xlsx file
    xlsx_file = src_folder.joinpath('activities','data','paralympics_all_raw.xlsx')
    print(xlsx_file.exists())

    # Reading contents of the csv file into a Dataframe
    paralympics_df = pd.read_csv(csv_file)

    # Reading the contents of sheet 1 and sheet 3 of the xlsx file into a Dataframe
    paralympics_game_df = pd.read_excel(xlsx_file, sheet_name=0) # Data on games
    medal_standings_df = pd.read_excel(xlsx_file, sheet_name=2) # Data on medal standings
