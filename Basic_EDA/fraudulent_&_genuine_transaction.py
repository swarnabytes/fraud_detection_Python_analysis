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

```text
+-------+----------------------------------------------+----------+
| Class |   Mean    |  Min  |  Median  |    Max    |     Std      |
+-------+-----------+-------+----------+-----------+--------------+
| 0     | 88.29102  |  0.0  |  22.00   |  25691.16 |  250.105092  | 
| 1     | 122.21132 |  0.0  |  9.25    |  2125.87  |  256.683288  |
+-------+----------------------------------------------+----------+
```
