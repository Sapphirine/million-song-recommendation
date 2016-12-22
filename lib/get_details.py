import os
import os
import numpy as np
import pandas as pd
from pandas import DataFrame
import h5py
from scipy.stats import kurtosis
from scipy.stats import skew

file_path = []
'''put the data into a folder and set the correct path'''
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
        self.q50 = np.percentile(source_data,50)
        self.q75 = np.percentile(source_data,75)
        self.skew = skew(source_data)
        self.kurtosis = kurtosis(source_data)

'''
analysis/bars_confidence  BarCon
analysis/bars_start    BarSta
analysis/beats_confidence    BeatsC
analysis/beats_start    BeatsS
analysis/segments_confidence   SC
analysis/segments_loudness_max  SLM
analysis/segments_loudness_max_time    SLMT
analysis/segments_loudness_start    SLS
analysis/segments_pitches  
analysis/segments_start  SS
analysis/segments_timbre
analysis/tatums_confidence    TC
analysis/tatums_start    TS
'''
df_name = ['file_path',
           'BarCon_mean','BarCon_std','BarCon_25_quant',
           'BarCon_50_quant','BarCon_75_quant','BarCon_skw','BarCon_kts',
           
           'BarSta_mean','BarSta_std','BarSta_25_quant',
           'BarSta_50_quant','BarSta_75_quant','BarSta_skw','BarSta_kts',
           
           'BeatsC_mean','BeatsC_std','BeatsC_25_quant',
           'BeatsC_50_quant','BeatsC_75_quant','BeatsC_skw','BeatsC_kts',
           
           'BeatsS_mean','BeatsS_std','BeatsS_25_quant',
           'BeatsS_50_quant','BeatsS_75_quant','BeatsS_skw','BeatsS_kts',
           
           'SC_mean','SC_std','SC_25_quant',
           'SC_50_quant','SC_75_quant','SC_skw','SC_kts',
           
           'SS_mean','SS_std','SS_25_quant',
           'SS_50_quant','SS_75_quant','SS_skw','SS_kts',
           
           'SLM_mean','SLM_std','SLM_25_quant',
           'SLM_50_quant','SLM_75_quant','SLM_skw','SLM_kts',
           
           'SLMT_mean','SLMT_std','SLMT_25_quant',
           'SLMT_50_quant','SLMT_75_quant','SLMT_skw','SLMT_kts',
           
           'SLS_mean','SLS_std','SLS_25_quant',
           'SLS_50_quant','SLS_75_quant','SLS_skw','SLS_kts',
           
           'TC_mean','TC_std','TC_25_quant',
           'TC_50_quant','TC_75_quant','TC_skw','TC_kts',
           
           'TS_mean','TS_std','TS_25_quant',
           'TS_50_quant','TS_75_quant','TS_skw','TS_kts',
           ]
                    
           
def get_df(source_file):
    temp_zeros = np.zeros(df_name.__len__())
    file_df = DataFrame([temp_zeros],columns=df_name)
    
    file_temp = h5py.File(source_file,'r')
    bars_confidence = songs_info(file_temp['analysis']['bars_confidence'][()])
    bars_start = songs_info(file_temp['analysis']['bars_start'][()])
    beats_confidence = songs_info(file_temp['analysis']['beats_confidence'][()])
    beats_start = songs_info(file_temp['analysis']['beats_start'][()])
    segments_confidence = songs_info(file_temp['analysis']['segments_confidence'][()])
    segments_loudness_max = songs_info(file_temp['analysis']['segments_loudness_max'][()])
    segments_loudness_max_time = songs_info(file_temp['analysis']['segments_loudness_max_time'][()])
    segments_loudness_start = songs_info(file_temp['analysis']['segments_loudness_start'][()])
    segments_start = songs_info(file_temp['analysis']['segments_start'][()])
    tatums_confidence = songs_info(file_temp['analysis']['tatums_confidence'][()])
    tatums_start = songs_info(file_temp['analysis']['tatums_start'][()])
    
    file_df['file_path'] = source_file

    file_df['BarCon_mean'] = bars_confidence.mean
    file_df['BarCon_std'] = bars_confidence.std
    file_df['BarCon_25_quant'] = bars_confidence.q25
    file_df['BarCon_50_quant'] = bars_confidence.q50
    file_df['BarCon_75_quant'] = bars_confidence.q75
    file_df['BarCon_skw'] = bars_confidence.skew
    file_df['BarCon_kts'] = bars_confidence.kurtosis

    file_df['BarSta_mean'] = bars_start.mean
    file_df['BarSta_std'] = bars_start.std
    file_df['BarSta_25_quant'] = bars_start.q25
    file_df['BarSta_50_quant'] = bars_start.q50
    file_df['BarSta_75_quant'] = bars_start.q75
    file_df['BarSta_skw'] = bars_start.skew
    file_df['BarSta_kts'] = bars_start.kurtosis

    file_df['BeatsC_mean'] = beats_confidence.mean
    file_df['BeatsC_std'] = beats_confidence.std
    file_df['BeatsC_25_quant'] = beats_confidence.q25
    file_df['BeatsC_50_quant'] = beats_confidence.q50
    file_df['BeatsC_75_quant'] = beats_confidence.q75
    file_df['BeatsC_skw'] = beats_confidence.skew
    file_df['BeatsC_kts'] = beats_confidence.kurtosis

    file_df['BeatsS_mean'] = bars_start.mean
    file_df['BeatsS_std'] = bars_start.std
    file_df['BeatsS_25_quant'] = bars_start.q25
    file_df['BeatsS_50_quant'] = bars_start.q50
    file_df['BeatsS_75_quant'] = bars_start.q75
    file_df['BeatsS_skw'] = bars_start.skew
    file_df['BeatsS_kts'] = bars_start.kurtosis

    file_df['SC_mean'] = segments_confidence.mean
    file_df['SC_std'] = segments_confidence.std
    file_df['SC_25_quant'] = segments_confidence.q25
    file_df['SC_50_quant'] = segments_confidence.q50
    file_df['SC_75_quant'] = segments_confidence.q75
    file_df['SC_skw'] = segments_confidence.skew
    file_df['SC_kts'] = segments_confidence.kurtosis

    file_df['SS_mean'] = segments_start.mean
    file_df['SS_std'] = segments_start.std
    file_df['SS_25_quant'] = segments_start.q25
    file_df['SS_50_quant'] = segments_start.q50
    file_df['SS_75_quant'] = segments_start.q75
    file_df['SS_skw'] = segments_start.skew
    file_df['SS_kts'] = segments_start.kurtosis

    file_df['SLM_mean'] = segments_loudness_max.mean
    file_df['SLM_std'] = segments_loudness_max.std
    file_df['SLM_25_quant'] = segments_loudness_max.q25
    file_df['SLM_50_quant'] = segments_loudness_max.q50
    file_df['SLM_75_quant'] = segments_loudness_max.q75
    file_df['SLM_skw'] = segments_loudness_max.skew
    file_df['SLM_kts'] = segments_loudness_max.kurtosis

    file_df['SLMT_mean'] = segments_loudness_max_time.mean
    file_df['SLMT_std'] = segments_loudness_max_time.std
    file_df['SLMT_25_quant'] = segments_loudness_max_time.q25
    file_df['SLMT_50_quant'] = segments_loudness_max_time.q50
    file_df['SLMT_75_quant'] = segments_loudness_max_time.q75
    file_df['SLMT_skw'] = segments_loudness_max_time.skew
    file_df['SLMT_kts'] = segments_loudness_max_time.kurtosis

    file_df['SLS_mean'] = segments_loudness_start.mean
    file_df['SLS_std'] = segments_loudness_start.std
    file_df['SLS_25_quant'] = segments_loudness_start.q25
    file_df['SLS_50_quant'] = segments_loudness_start.q50
    file_df['SLS_75_quant'] = segments_loudness_start.q75
    file_df['SLS_skw'] = segments_loudness_start.skew
    file_df['SLS_kts'] = segments_loudness_start.kurtosis

    file_df['TC_mean'] = tatums_confidence.mean
    file_df['TC_std'] = tatums_confidence.std
    file_df['TC_25_quant'] = tatums_confidence.q25
    file_df['TC_50_quant'] = tatums_confidence.q50
    file_df['TC_75_quant'] = tatums_confidence.q75
    file_df['TC_skw'] = tatums_confidence.skew
    file_df['TC_kts'] = tatums_confidence.kurtosis

    file_df['TS_mean'] = tatums_start.mean
    file_df['TS_std'] = tatums_start.std
    file_df['TS_25_quant'] = tatums_start.q25
    file_df['TS_50_quant'] = tatums_start.q50
    file_df['TS_75_quant'] = tatums_start.q75
    file_df['TS_skw'] = tatums_start.skew
    file_df['TS_kts'] = tatums_start.kurtosis

    return file_df


song_details = DataFrame()  
wrong_file = []
for k in range(file_path.__len__()):
    try:
        df_temp = get_df(file_path[k])
        song_details = song_details.append(df_temp)
        print k
    except:
        wrong_file.append(file_path[k])
        print "wrong file is:",k

song_details.index = range(song_details.shape[0])
        
song_details.to_csv('songs_details.csv')
