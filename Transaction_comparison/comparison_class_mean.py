# Data to pass - Fraud mean_value and Genuine mean_value
fraud_amount_mean = dfcopy[dfcopy["Class"] == 1]["Amount"].mean()
genuine_amount_mean = dfcopy[dfcopy["Class"] == 0]["Amount"].mean()

# Creates categories and their values for Bar Graph
height = [ round(fraud_amount_mean,2),round(genuine_amount_mean,2)]
x_label = ["Fraud", "Genuine"]

# Creates the Bar graph
plt.figure(figsize=(6,6), edgecolor ="black", linewidth = 2)
bars = plt.bar(x_label, height, color =["#4E78E2", "#0EC48A"])

# Labels the graph
plt.title('Comparison of Mean Transaction Amounts', fontweight ="bold")
plt.bar_label(bars, fmt='%.2f', padding=3, fontsize=11, weight='bold')

plt.xlabel("Transaction Type", fontweight= "bold")
plt.ylabel("Average Amount", fontweight= "bold")
plt.ylim(0, max(height) * 1.15)


plt.show()
