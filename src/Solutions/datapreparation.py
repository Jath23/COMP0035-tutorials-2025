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
    # Robustly map all category values to lowercase and remove spaces
    df[Col_Name] = df[Col_Name].str.strip().str.lower()

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

# Function that changes dates in a string format to a datetime format
def convert_dates(df: pd.DataFrame, columns = ['start','end'], date_format = '%d/%m/%Y'):
    """
    Converts date strings to a datetime format and localises timezone

    Parameters:
    df, the dataframe
    columns: list of column names to be converted into datetime format
    date_format: format of the string dates
    timezone: identifies the timezone
    
    Returns:
    dataframe with converted columns    
    """
    for col in columns:
        df[col] = pd.to_datetime(df[col], format = date_format)
        
    return df


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
    
    # Remove rows with indices 0,17 and 31 as they have missing/incorrect data
    # Reset the index so that it is consecutive from zero
    df_prepared = df_prepared.drop(index=[0,17,31])
    df_prepared = df_prepared.reset_index(drop=True)
    
    # Code that changes all the float datatypes to integer 
    column_type_float = ['countries','events','participants_m','participants_f','participants']
    df_prepared[column_type_float] = df_prepared[column_type_float].astype('int')
    
    # Convert the start and end dates to datetime format
    convert_dates(df_prepared)

    # Add a new column called duration with its values calculated by subtracting the start date from the end date
    duration_values = (df_prepared['end']-df_prepared['start']).dt.days.astype('Int64')
    # Insert the values as a new column the 'end' column
    # 'df_prepared.insert(df_prepared.columns.get_loc('end')+1' finds the index of the 'end' column 
    # and adds 1 to set the position of the new column
    # 'duration' is the name of the new column
    # 'duration_values' are the values for the new column
    df_prepared.insert(df_prepared.columns.get_loc('end')+1,'duration',duration_values)
    
    # Finding the path to the npc_codes.csv file and converting it to a DataFrame
    npc_path = Path(__file__).parent.parent.joinpath('activities','data','npc_codes.csv')
    npc_df = pd.read_csv(npc_path, encoding = 'utf-8', encoding_errors = 'ignore', usecols = ['Code','Name'])

    # Creating replacement names for the countries under the 'country' column in df_prepared dataframe
    replacement_names = {'UK':'Great Britain',
                         'USA':'United States of America',
                         'Korea':'Republic of Korea',
                         'Russia':'Russian Federation',
                         'China':"People's Republic of China"}
    
    # Replacing the original names with the replacement names
    df_prepared['country'] = df_prepared['country'].replace(replacement_names)

    # Merging the npc_df and df_prepared dataframe together
    merged_df = df_prepared.merge(npc_df, how='left', left_on='country', right_on='Name')
    # There is an extra column 'Name' at the end of the table, which can be dropped
    # as it is the same as the 'country' column
    merged_df = merged_df.drop(columns=['Name'])

    # Define the output path and save the merged dataframe to be reused
    # Its name is updated to 'cleaned_paralympics.csv'
    output_path = src_folder.joinpath('activities','data','cleaned_paralympics.csv')
    merged_df.to_csv(output_path, index=False)

    print(f"\n{merged_df}")

    