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

Transaction_Type	    Fraud      Genuine	    All
Amount_band			
[0.0, 1.0)	            68	        16736	    16804
[1.0, 5.0)	            153	        50506	    50659
[5.0, 10.0)	            28	        29823	    29851
[10.0, 50.0)	            56	        92334	    92390
[50.0, 100.0)	            57	        37661	    37718
[100.0, 500.0)	            95	        47798	    47893
[500.0, 1000.0)	            26	        6397	    6423
[1000.0, inf)	            9	        3060	    3069
All	                   492	       284315	   284807
