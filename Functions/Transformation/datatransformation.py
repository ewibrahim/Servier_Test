import pandas as pd

# Create a function that set the same format for the date column
def uniformat_date(df, column):
    """
    Uniformat a date to column to YYYY-MM-DD
    :param df:
    :return:
    """
    df[column] = pd.to_datetime(df[column]).dt.strftime('%Y-%m-%d')

# Create a function that removes special characters from a column
def remove_special_characters(df, column):
    """
    Create a function that removes special characters from a column
    :param df:
    :param column:
    :return:
    """
    df[column] = df[column].str.replace('[^\w\s]','')

# Create a new column clinical_trials["drug_id"] where the drug is mentioned and the drug_id is the same as drugs["atccode"]
def find_drug_id_in_clinical_trials(df, df2):
    """
    Create a new column clinical_trials["drug_id"] where the drug is mentioned and the drug_id is the same as drugs["atccode"]
    :param df:
    :param df2:
    :return:
    """
    df["drug_id"] = df["scientific_title"].str.extract("("+df2["drug"]+")")
    df["drug_id"] = df["drug_id"].str.replace(" ", "")
    df["drug_id"] = df["drug_id"].str.replace("(", "")
    df["drug_id"] = df["drug_id"].str.replace(")", "")