# Mean and Median for all V columns
v_columns = [c for c in dfcopy.columns if c.startswith('V')]
col_mean = dfcopy[v_columns].mean()
col_median = dfcopy[v_columns].median()

# Merge both columns
pd.concat([col_median, col_mean],keys=['Median','Mean'] ,axis = 1)

# MultiIndex V1-V28 dataframe
v_column = [c for c in dfcopy.columns if c.startswith('V')] + ['Class']

v_column_mean = dfcopy[v_column].groupby('Class').mean()
v_column_median = dfcopy[v_column].groupby('Class').median()

v_col = pd.concat([v_column_median, v_column_mean], keys= ['Median','Mean'])
v_col
