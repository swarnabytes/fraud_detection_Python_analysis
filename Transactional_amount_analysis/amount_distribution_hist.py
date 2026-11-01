
plt.figure(figsize=(20,6), edgecolor ="black", linewidth = 2)
upper = dfcopy['Amount'].quantile(0.95)

# Creates the Histogram for Fraudulent Transaction Amounts
plt.subplot(1,2, 1)

plt.hist(dfcopy[dfcopy["Class"] == 1]["Amount"], bins = 30, 
         color  = "#4E78E2", range = (lower_limit, upper_limit))

# Labels the Histogram
plt.title('Distribution of Fraudulent Transaction Amounts', fontweight = 'bold', pad = 10)
plt.xlabel('Transaction Amount', fontweight= 'bold', labelpad = 10)
plt.ylabel('No. of Transactions', fontweight = 'bold',labelpad = 10)

plt.xlim(-10, upper)                                             # Zooms the window to focus strictly from -10 to 95th percentile
plt.yscale('log')


# Creates the Histogram for Genuine Transaction Amounts
plt.subplot(1, 2, 2)

plt.hist(dfcopy[dfcopy["Class"]==0]["Amount"], bins= 30, 
         color = "#0EC48A", range = (lower_limit, upper_limit))

# Labels the Histogram
plt.title('Distribution of Genuine Transaction Amounts', fontweight = 'bold', pad = 10)
plt.xlabel('Transaction Amount', fontweight= 'bold', labelpad = 10)
plt.ylabel('No. of Transactions', fontweight = 'bold',labelpad = 10)

plt.xlim(-10, upper)                                                                       # Zooms the window to focus strictly from -10 to 95th percentile
plt.yscale('log')

plt.show()
