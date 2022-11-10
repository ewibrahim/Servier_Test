def save_to_json(df, filename):
    """
    Function that saves a dataframe to a json file
    :param df:
    :param filename:
    :return:
    """
    df.to_json("Data/Output_transformation/"+filename+".json", orient="records")
    print("Data saved to Data/Output_transformation/"+filename+".json")

def save_to_csv(df, filename):
    """
    Function that saves a dataframe to a csv file
    :param df:
    :param filename:
    :return:
    """
    df.to_csv("Data/Output_transformation/"+filename+".csv", index=False)
    print("Data saved to Data/Output_transformation/"+filename+".csv")