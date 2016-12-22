import os
import numpy as np
import pandas as pd
from pandas import DataFrame
import h5py
from scipy.stats import kurtosis
from scipy.stats import skew
'''get song pitches'''
'''set the file path'''
file_path = []
file_dic = '/Users/shiluyuan/Downloads/bigdataproject/musicdata'
for dirpath, dirnames, filenames in os.walk(file_dic):
    for files in filenames:
        if (os.path.splitext(files)[1] == '.h5'):
            file_path.append(os.path.join(dirpath, files)) 

class songs_info:
    def __init__(self, source_data):
        self.mean = np.mean(source_data)
        self.std = np.std(source_data)
        self.q25 = np.percentile(source_data,25)
        self.median = np.percentile(source_data,50)
        self.q75 = np.percentile(source_data,75)
        self.skew = skew(source_data)
        self.kurtosis = kurtosis(source_data)

col_name = ['file_path',

            'pitch_0_mean','pitch_0_std','pitch_0_median',
            'pitch_0_skw','pitch_0_kts',

            'pitch_1_mean','pitch_1_std','pitch_1_median',
            'pitch_1_skw','pitch_1_kts',

            'pitch_2_mean','pitch_2_std','pitch_2_median',
            'pitch_2_skw','pitch_2_kts',

            'pitch_3_mean','pitch_3_std','pitch_3_median',
            'pitch_3_skw','pitch_3_kts',

            'pitch_4_mean','pitch_4_std','pitch_4_median',
            'pitch_4_skw','pitch_4_kts',

            'pitch_5_mean','pitch_5_std','pitch_5_median',
            'pitch_5_skw','pitch_5_kts',

            'pitch_6_mean','pitch_6_std','pitch_6_median',
            'pitch_6_skw','pitch_6_kts',

            'pitch_7_mean','pitch_7_std','pitch_7_median',
            'pitch_7_skw','pitch_7_kts',

            'pitch_8_mean','pitch_8_std','pitch_8_median',
            'pitch_8_skw','pitch_8_kts',

            'pitch_9_mean','pitch_9_std','pitch_9_median',
            'pitch_9_skw','pitch_9_kts',

            'pitch_10_mean','pitch_10_std','pitch_10_median',
            'pitch_10_skw','pitch_10_kts',

            'pitch_11_mean','pitch_11_std','pitch_11_median',
            'pitch_11_skw','pitch_11_kts']

def pitch_info(source_file):
    temp_zeros = np.zeros(col_name.__len__())
    file_df = DataFrame([temp_zeros],columns = col_name)
    
    file_temp = h5py.File(source_file,'r')
    pitch_matrix = np.asmatrix(file_temp['analysis']['segments_pitches'][()])

    pitch_0 = songs_info(pitch_matrix[:,0])
    pitch_1 = songs_info(pitch_matrix[:,1])
    pitch_2 = songs_info(pitch_matrix[:,2])
    pitch_3 = songs_info(pitch_matrix[:,3])
    pitch_4 = songs_info(pitch_matrix[:,4])
    pitch_5 = songs_info(pitch_matrix[:,5])
    pitch_6 = songs_info(pitch_matrix[:,6])
    pitch_7 = songs_info(pitch_matrix[:,7])
    pitch_8 = songs_info(pitch_matrix[:,8])
    pitch_9 = songs_info(pitch_matrix[:,9])
    pitch_10 = songs_info(pitch_matrix[:,10])
    pitch_11 = songs_info(pitch_matrix[:,11])

    file_df['file_path'] = source_file

    file_df['pitch_0_mean'] = pitch_0.mean
    file_df['pitch_0_median'] = pitch_0.median
    file_df['pitch_0_std'] = pitch_0.std
    file_df['pitch_0_skw'] = pitch_0.skew
    file_df['pitch_0_kts'] = pitch_0.kurtosis


    file_df['pitch_1_mean'] = pitch_1.mean
    file_df['pitch_1_median'] = pitch_1.median
    file_df['pitch_1_std'] = pitch_1.std
    file_df['pitch_1_skw'] = pitch_1.skew
    file_df['pitch_1_kts'] = pitch_1.kurtosis


    file_df['pitch_2_mean'] = pitch_2.mean
    file_df['pitch_2_median'] = pitch_2.median
    file_df['pitch_2_std'] = pitch_2.std
    file_df['pitch_2_skw'] = pitch_2.skew
    file_df['pitch_2_kts'] = pitch_2.kurtosis


    file_df['pitch_3_mean'] = pitch_3.mean
    file_df['pitch_3_median'] = pitch_3.median
    file_df['pitch_3_std'] = pitch_3.std
    file_df['pitch_3_skw'] = pitch_3.skew
    file_df['pitch_3_kts'] = pitch_3.kurtosis


    file_df['pitch_4_mean'] = pitch_4.mean
    file_df['pitch_4_median'] = pitch_4.median
    file_df['pitch_4_std'] = pitch_4.std
    file_df['pitch_4_skw'] = pitch_4.skew
    file_df['pitch_4_kts'] = pitch_4.kurtosis


    file_df['pitch_5_mean'] = pitch_5.mean
    file_df['pitch_5_median'] = pitch_5.median
    file_df['pitch_5_std'] = pitch_5.std
    file_df['pitch_5_skw'] = pitch_5.skew
    file_df['pitch_5_kts'] = pitch_5.kurtosis


    file_df['pitch_6_mean'] = pitch_6.mean
    file_df['pitch_6_median'] = pitch_6.median
    file_df['pitch_6_std'] = pitch_6.std
    file_df['pitch_6_skw'] = pitch_6.skew
    file_df['pitch_6_kts'] = pitch_6.kurtosis


    file_df['pitch_7_mean'] = pitch_7.mean
    file_df['pitch_7_median'] = pitch_7.median
    file_df['pitch_7_std'] = pitch_7.std
    file_df['pitch_7_skw'] = pitch_7.skew
    file_df['pitch_7_kts'] = pitch_7.kurtosis


    file_df['pitch_8_mean'] = pitch_8.mean
    file_df['pitch_8_median'] = pitch_8.median
    file_df['pitch_8_std'] = pitch_8.std
    file_df['pitch_8_skw'] = pitch_8.skew
    file_df['pitch_8_kts'] = pitch_8.kurtosis


    file_df['pitch_9_mean'] = pitch_9.mean
    file_df['pitch_9_median'] = pitch_9.median
    file_df['pitch_9_std'] = pitch_9.std
    file_df['pitch_9_skw'] = pitch_9.skew
    file_df['pitch_9_kts'] = pitch_9.kurtosis


    file_df['pitch_10_mean'] = pitch_10.mean
    file_df['pitch_10_median'] = pitch_10.median
    file_df['pitch_10_std'] = pitch_10.std
    file_df['pitch_10_skw'] = pitch_10.skew
    file_df['pitch_10_kts'] = pitch_10.kurtosis


    file_df['pitch_11_mean'] = pitch_11.mean
    file_df['pitch_11_median'] = pitch_11.median
    file_df['pitch_11_std'] = pitch_11.std
    file_df['pitch_11_skw'] = pitch_11.skew
    file_df['pitch_11_kts'] = pitch_11.kurtosis

    return file_df

pitch_details = DataFrame()

wrong_file = []
for k in range(file_path.__len__()):
    try:
        df_temp = pitch_info(file_path[k])
        pitch_details = pitch_details.append(df_temp)
        print k
    except:
        wrong_file.append(file_path[k])
        print "wrong file is:",k


pitch_details.index = range(pitch_details.shape[0])        
pitch_details.to_csv('pitch_details.csv')


