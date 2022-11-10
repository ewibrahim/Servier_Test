import os
import pandas as pd
import json

def open_json(file):
    """
    Open a json file
    :param file:
    :return:
    """
    with open(file) as f:
        data = json.load(f)
    return data

def convert_to_int(df, column):
    """
    Function that converts a column type to int
    :param df:
    :param column:
    :return:
    """
    df[column] = df[column].astype(int)

def convert_to_string(df, column):
    """
    Function that converts a column type to string
    :param df:
    :param column:
    :return:
    """
    df[column] = df[column].astype('string')
    print("converted")

def titlecase(df, column):
    """
    Lowercase a column values then title() them
    :param df:
    :param column:
    :return:
    """
    print("\n"+df[column][0])
    df[column] = df[column].str.lower()
    df[column] = df[column].str.title()
    "/n"
    print(df[column][0])

def remove_nans(df):
    """
    Remove rows with at least one NaN value
    :param df:
    :return:
    """
    for i in df:
        df[i] = df[i].dropna()

def uniformat_date(df, column):
    """
    Uniformat a date to column to YYYY-MM-DD
    :param df:
    :return:
    """
    df[column] = pd.to_datetime(df[column], format="%Y-%m-%d")

def check_path(path):
    """
    Function check if path exists taking a path as input
    :param path:
    :return:
    """
    if os.path.exists(path):
        return True
    else:
        print("Path does not exist")

def list_files(path):
    """
    Function that lists all files of a folder
    :param path:
    :return:
    """
    global files
    if check_path(path):
        files = os.listdir(path)
        if len(files) == 0:
            print("Folder is empty")
        print("Files listed \n")

def extract_from_csv(file):
    """
    Extract data from csv file
    :param file_to_process:
    :return:
    """
    df = pd.read_csv(file)
    return df

def extract_from_json(file):
    """
    Extract data from json file
    :param file_to_process:
    :return:
    """
    df = pd.read_json(file, lines=True)
    return df

# def create_df(path):
#     """
#     Function that creates a dataframe for each file in files and names it after the file name
#     :param path:
#     :return:
#     """
#     check_path(path)
#     list_files(path)
#     for i in files:
#         if i.endswith(".csv"):
#             # Rename i to remove .csv
#             df = i[:-4]
#             df = pd.read_csv(path+df+".csv")
#             print(df+" dataframe created")
#         elif i.endswith(path+df+".json"):
#             # Rename i to remove .json
#             df = i[:-5]
#             df = pd.read_json(df, lines=True)

def check_nulls(df):
    """
    Function that checks for nulls in a dataframe
    :param df:
    :return:
    """
    print(df.isnull().sum())

def check_nulls_column(df, column):
    """
    Check for nulls in a specific column
    :param df:
    :param column:
    :return:
    """
    if df[column].isnull().values.any():
        print("Column "+column+" contains nulls")
    else:
        print("Column "+column+" does not contain nulls")

def check_nans_column(df, column):
    """
    Check for nans in a specific column
    :param df:
    :param column:
    :return:
    """
    if df[column].isna().values.any():
        print("Column "+column+" contains nans")
    else:
        print("Column "+column+" does not contain nans")

def isDfEmpty(df):
    """
    Function that checks if a dataframe is empty
    :param df:
    :return:
    """
    if df.empty:
        print("Dataframe is empty")
