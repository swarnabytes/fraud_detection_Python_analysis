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
