# Convert into the elapsed hour in which each transaction occurred
dfcopy['convert_time'] = dfcopy['Time']//3600
dfcopy['convert_time']

# Creates time band for the comparison 
time_bins = [0,5,10,15,20,25,30,35,40, float('inf')]

dfcopy['Time_band']  = pd.cut(
    dfcopy['convert_time'],
    time_bins, right = False
)

# Transactions exploration within a time band
hour_table = pd.crosstab(dfcopy['Time_band'],dfcopy['Transaction_Type'], margins= True, dropna= False)
hour_table
# Fraud rate by time band
hour_table['Fraud_rate'] = (hour_table['Fraud']/hour_table['All'])*100
hour_table['Fraud_rate'] = round(hour_table['Fraud_rate'],2).astype(str) + '%'

--------------------------hour_table--------------------------
Transaction_Type	Fraud	  Genuine	 All	  Fraud_rate
Time_band				
[0.0, 5.0)	        44	    10615	    10659	    0.41%
[5.0, 10.0)	        57	    19880	    19937	    0.29%
[10.0, 15.0)	    76	    40075	    40151	    0.19%
[15.0, 20.0)	    62	    40043	    40105	    0.15%
[20.0, 25.0)	    46	    37620	    37666	    0.12%
[25.0, 30.0)	    65	    7797	    7862	    0.83%
[30.0, 35.0)	    17	    27495	    27512	    0.06%
[35.0, 40.0)	    48	    40925	    40973	    0.12%
[40.0, inf)      	77	    59865	    59942	    0.13%
All	               492	     284315	    284807	    0.17%
