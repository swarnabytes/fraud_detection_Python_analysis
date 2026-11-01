plot_data = hour_table.drop('All', axis=0, errors= 'ignore').drop('All', axis =1, errors= 'ignore')
plot_data = hour_table.dropna(axis=0)
plot_data.reset_index()

# Creates the line graph
plot_data.plot(kind='line', marker='o', linewidth=2, figsize=(12, 6), grid= False)
plt.show()
