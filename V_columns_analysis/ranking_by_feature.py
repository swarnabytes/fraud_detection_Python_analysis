# Absolute difference between each features mean based on class
v_column_mean
v_t = v_column_mean.transpose()

v_t['Absolute Difference'] = v_t[1].sub(v_t[0]).abs()
v_t

# Ranking according to absolute mean difference
v_t['Absolute Difference'].sort_values(ascending=False)

# Absolute difference between each features median based on class
v_column_median
v_c = v_column_median.transpose()

v_c['Absolute Difference'] = v_c[1].sub(v_c[0]).abs()
v_c

# Ranking according to absolute median difference
v_c['Absolute Difference'].sort_values(ascending= False)
