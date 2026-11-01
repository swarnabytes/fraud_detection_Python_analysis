### Check for Outliers
df["Class"].value_counts()
dfcopy["Amount"].describe()

fraud_data = dfcopy[dfcopy['Class'] == 1]['Amount']
genuine_data = dfcopy[dfcopy['Class'] == 0]['Amount']

fraud_data.describe() , genuine_data.describe()
fraud_data = dfcopy[dfcopy['Class'] == 1]['Amount']
fraud_data.describe() 

q1 = fraud_data.quantile(0.25)
q3 = fraud_data.quantile(0.75)

IQR = q3 - q1
IQR
lower_limit = q1 - (1.5 * IQR)
upper_limit = q3 + (1.5 * IQR)
q1, q3, lower_limit, upper_limit
