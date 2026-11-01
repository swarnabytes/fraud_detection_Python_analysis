# Correlation matrix
corr1 = dfcopy[['Class', 'Amount', 'Time']].corr()
corr1
sns.heatmap(corr1)

# Correlation of V columns with Class column
corr2 = dfcopy[v_column + ['Class']].corr()
corr2
sns.heatmap(corr2)


# Correlation of V columns against the Class column
corr3 = dfcopy[v_columns].corrwith(dfcopy['Class']).sort_values()
corr3
