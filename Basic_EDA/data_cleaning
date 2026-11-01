import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

df= pd.read_csv('creditcard.csv')
df.head()

# Data Cleaning
### Check for null/missing/duplicate
        df.isnull().sum()
        df.describe()
        df.duplicated().sum()
        df.info()
        df.nunique()
        df.duplicated().sum()

### Validate 'Class' column
        df["Transaction_Type"] = df["Class"].map({1: "Fraud", 0: "Genuine"})
        dfcopy =  df.copy()
        dfcopy.info()


        ### Fraudulent and Genuine Transcations
fraudulent_rows = dfcopy.query("Class == 1").shape[0]
genuine_rows = dfcopy.query("Class == 0").shape[0]
fraudulent_rows, genuine_rows

percentage_fraud = round((fraudulent_rows/dfcopy.shape[0])*100,4)
percentage_genuine = round((genuine_rows/dfcopy.shape[0])*100,4)

percentage_fraud, percentage_genuine
class_groupby = dfcopy.groupby("Class")
Class_values = class_groupby.agg({ "Amount": ["mean", "median", "min", "max", "std"]})
Class_values
