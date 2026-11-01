# Creates amount band
bins = [0,1,5,10,50,100,500,1000, float('inf')]
dfcopy['Amount_band'] = pd.cut(
    dfcopy['Amount'],
    bins, right = False
)

# Display all the genuine and fraudulent transactions which falls within each amount band
Amount_Table = pd.crosstab(dfcopy['Amount_band'], dfcopy['Transaction_Type'], margins= True, dropna = False)                                     
dfcopy['Transaction_Type'].shape[0]

# Creates Fraud rate per Amount Band
Fraud_rate = (Amount_Table['Fraud']/Amount_Table['All']) * 100
Amount_Table['Fraud_rate'] = round(Fraud_rate,2).astype(str) + '%'

# Creates Genuine rate per Amount Band
Genuine_rate = (Amount_Table['Genuine']/Amount_Table['All']) * 100
Amount_Table['Genuine_rate'] = round(Genuine_rate,2).astype(str) + '%'

Amount_Table
