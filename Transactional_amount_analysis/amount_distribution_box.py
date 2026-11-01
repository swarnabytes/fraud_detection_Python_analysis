# Creates a canvas
fig, ax = plt.subplots(figsize=(8,6))

# Set a clean style
sns.set_theme(style="whitegrid") 

# Creates the Boxplot
sns.boxplot(
    data = dfcopy,
    x = 'Class', y = 'Amount', ax = ax, order = [0,1], patch_artist=True, medianprops={"color": "white", "linewidth": 1},
    palette = ["#4E78E2", "#0EC48A"], showfliers = False, showmeans = True, width = 0.3)

# Labels the Graph
ax.set_xticks([1,0])
ax.set_xticklabels([ "Genuine","Fraud"])
ax.set_title("Transaction Amount Distribution: Fraud vs Genuine", fontweight="bold", pad=10)
ax.set_xlabel("Transaction Type", fontweight="bold", labelpad=10)
ax.set_ylabel("Transaction Amount", fontweight="bold", labelpad=10)
ax.grid(axis='y', alpha= 1)

# Clean up the borders
sns.despine(left=False, bottom=False)

plt.tight_layout()
plt.show()
