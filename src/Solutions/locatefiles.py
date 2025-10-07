
from pathlib import Path

import pandas as pd

# Define function
def describe_df(df: pd.DataFrame):
    """
    This function takes the pandas dataframe as its argument in order to inspect datasets
    It will print information that describes the data in the dataframe
    
    Parameters:
    df is the parameter, which is used to describe any dataframe, making the function reusable

    Returns:
    Shape of dataframe (rows,columns)
    First 5 rows and last 5 rows
    Column datatypes
    Print the info
    Print the results of describe  
    """

    # Print all columns in the dataframe
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 200)
    pd.set_option("display.max_colwidth", None)

    print("\nDataframe Description")
    print("Shape", df.shape)
    print(f"\nFirst 5 rows:\n{df.head()}")
    print(f"\nLast 5 rows:\n{df.tail()}")
    print(f"\nColumn Labels:\n{df.columns.tolist()}")
    print(f"\nColumn Data Types:\n{df.dtypes}")
    print(f"\nInfo:\n{df.info()}")
    print(f"\nResults:\n{df.describe(include="all")}")

    # New code to find the number of missing values in the dataframe
    # isna() detects missing values and maps them as 'True'. Then add sum to find the total
    print(f"\nMissing values:\n{df.isna()}")

    # Copy of dataframe which only shows the rows of data that contains missing values
    print(f"\nRows with missing values:\n{df[df.isna().any(axis=1)]}")


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

    print("\nDataFrame 1")
    describe_df(paralympics_df)

    print("\nDataFrame 2")
    describe_df(paralympics_game_df)

    print("\nDataFrame 3")
    describe_df(medal_standings_df)
