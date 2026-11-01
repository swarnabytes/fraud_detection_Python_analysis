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
