import pandas as pd
import numpy as np
from scipy import stats
from pandas import DataFrame

'''read the data scv'''
'''set the corrent path'''
original_data = DataFrame.from_csv('/Users/shiluyuan/Downloads/bigdataproject/songs_details.csv')

column_num = original_data.columns.values.__len__()

scale_data = DataFrame(columns=original_data.columns.values[1:column_num])

for col in original_data.columns.values[1:column_num]:
    scale_data[col] = stats.zscore(original_data[col])
    
'''get the corelation matrix'''
corr_matrix1 = DataFrame.corr(scale_data,method='pearson', min_periods=1)
corr_matrix1.to_csv('corr_matrix.csv')

'''see which variables have the high correlation'''

def show_high_corr(original_df,corr_bar):
    corr_matrix = DataFrame.corr(original_df,method='pearson', min_periods=1) 
    var_num = corr_matrix.shape[1]
    high_corr = DataFrame(columns=['var1','var2','corr'])

    for i in range(var_num-1):
        for j in range(i+1,var_num-1):
            if abs(corr_matrix.iloc[i,j]) > corr_bar:
                temp_df = DataFrame([np.zeros(3)],columns=['var1','var2','corr'])
                temp_df['var1'] = corr_matrix.columns.values[i]
                temp_df['var2'] = corr_matrix.index.values[j]
                temp_df['corr'] = corr_matrix.iloc[i,j]
                high_corr = high_corr.append(temp_df)
                high_corr.index = range(high_corr.shape[0])
    return high_corr       

show_high_corr(scale_data,0.6)