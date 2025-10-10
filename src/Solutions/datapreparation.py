from pathlib import Path
import pandas as pd
import matplotlib as plt

# Define a new function that locates columns with the sae=me categorical data and maps them as the same
# e.g. Summer = summer and Winter = winter
def standardise_categories(df: pd.DataFrame, Col_Name):
    """
    
    """
    # Locate the exact datapoints in the 'type' column, where the rows contain 'Summer'
    # Map them to 'summer'
    df.loc[df[Col_Name] == 'Summer',Col_Name] = 'summer'
    df.loc[df[Col_Name] == 'winter ',Col_Name] = 'winter'

    print(df[Col_Name].unique())
    print(df[Col_Name].value_counts())



if __name__ == "__main__":

    # Pathing the csv file from another folder within the src folder
    # and changing it into a dataframe
    src_folder = Path(__file__).parent.parent
    csv_file = src_folder.joinpath('activities','data', 'paralympics_raw.csv')
    paralympics_df = pd.read_csv(csv_file)

    standardise_categories(paralympics_df, 'type')