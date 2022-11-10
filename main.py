from Functions.Preprocessing.datapreprocessing import *
from Functions.Transformation.datatransformation import *
from Functions.Postprocessing.datapostprocessing import *

path = "Data/Files/"

clinical_trials = extract_from_csv(path+"clinical_trials.csv")
drugs = extract_from_csv(path+"drugs.csv")
pubmed_csv = extract_from_csv(path+"pubmed.csv")

df_list = [clinical_trials, drugs, pubmed_csv]

# Check for nulls
isDfEmpty(clinical_trials)
isDfEmpty(drugs)
isDfEmpty(pubmed_csv)

# Check nulls for df_list
check_nulls(clinical_trials)
check_nulls(drugs)
check_nulls(pubmed_csv)

# Check Nulls for a specific columns
check_nulls_column(clinical_trials, "date")

# Check Nans for a specific columns
check_nans_column(clinical_trials, "scientific_title")

# Transform data
# find_drug_id_in_clinical_trials(clinical_trials, drugs)
remove_special_characters(clinical_trials, "scientific_title")

# Uniform date
uniformat_date(clinical_trials, "date")