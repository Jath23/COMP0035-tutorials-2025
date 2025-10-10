from pathlib import Path
import pandas as pd
import matplotlib as plt

# Define a new function that locates columns with the sae=me categorical data and maps them as the same
# e.g. Summer = summer and Winter = winter
def standardise_categories(df: pd.DataFrame, Col_Name):
    """
    This function changes similar categories into one of the same name

    Parameters:
    df, the dataframe and the column heading where the categories are located

    Returns:
    The number of data for each standardised category
    """
    # Locate the exact datapoints in the 'type' column, where the rows contain 'Summer'
    # Map them to 'summer'
    df.loc[df[Col_Name] == 'Summer',Col_Name] = 'summer'
    df.loc[df[Col_Name] == 'winter ',Col_Name] = 'winter'

    print(df[Col_Name].unique())
    print(df[Col_Name].value_counts())

# New function that removes columns
def remove_columns(df: pd.DataFrame, columns_tobe_removed):
    """
    Function removes the specified columns listed within the main function
    and produces a new dataframe

    Parameters:
    df, the dataframe
    columns_tobe_removed: the list of column names to be dropped

    Returns:
    The new dataframe with the specified columns removed
    """

    df_removed = df.drop(columns = columns_tobe_removed)
    return df_removed



if __name__ == "__main__":

    # Pathing the csv file from another folder within the src folder
    # and changing it into a dataframe
    src_folder = Path(__file__).parent.parent
    csv_file = src_folder.joinpath('activities','data', 'paralympics_raw.csv')
    paralympics_df = pd.read_csv(csv_file)

    # Standardising categories
    standardise_categories(paralympics_df, 'type')

    # New dataframe with removed columns
    columns_tobe_removed = ['URL','disabilities_included','highlights']
    df_prepared = remove_columns(paralympics_df, columns_tobe_removed)
    print(df_prepared)