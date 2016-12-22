import os
import numpy as np
import pandas as pd
from pandas import DataFrame
import h5py
from scipy.stats import kurtosis
from scipy.stats import skew
'''set the correct path'''
'''get all the feature information'''
file_path = []
file_dic = '/Users/shiluyuan/Downloads/bigdataproject/musicdata'
for dirpath, dirnames, filenames in os.walk(file_dic):
    for files in filenames:
        if (os.path.splitext(files)[1] == '.h5'):
            file_path.append(os.path.join(dirpath, files)) 

'''calcualte all the feature statistics'''
class songs_info:
    def __init__(self, source_data):
        self.mean = np.mean(source_data)
        self.std = np.std(source_data)
        self.median = np.percentile(source_data,50)
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
details_col = ['file_path',
           'BarCon_mean','BarCon_std',
           'BarCon_median','BarCon_skw','BarCon_kts',
           
           'BarSta_mean','BarSta_std',
           'BarSta_median','BarSta_skw','BarSta_kts',
           
           'BeatsC_mean','BeatsC_std',
           'BeatsC_median','BeatsC_skw','BeatsC_kts',
           
           'BeatsS_mean','BeatsS_std',
           'BeatsS_median','BeatsS_skw','BeatsS_kts',
           
           'SC_mean','SC_std',
           'SC_median','SC_skw','SC_kts',
           
           'SS_mean','SS_std',
           'SS_median','SS_skw','SS_kts',
           
           'SLM_mean','SLM_std',
           'SLM_median','SLM_skw','SLM_kts',
           
           'SLMT_mean','SLMT_std',
           'SLMT_median','SLMT_skw','SLMT_kts',
           
           'SLS_mean','SLS_std',
           'SLS_median','SLS_skw','SLS_kts',
           
           'TC_mean','TC_std',
           'TC_median','TC_skw','TC_kts',
           
           'TS_mean','TS_std',
           'TS_median','TS_skw','TS_kts']

pitch_col = [
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


def get_details(source_file):
    temp_zeros = np.zeros(details_col.__len__())
    file_df = DataFrame([temp_zeros],columns=details_col)
    
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
    file_df['BarCon_median'] = bars_confidence.median
    file_df['BarCon_skw'] = bars_confidence.skew
    file_df['BarCon_kts'] = bars_confidence.kurtosis

    file_df['BarSta_mean'] = bars_start.mean
    file_df['BarSta_std'] = bars_start.std
    file_df['BarSta_median'] = bars_start.median
    file_df['BarSta_skw'] = bars_start.skew
    file_df['BarSta_kts'] = bars_start.kurtosis

    file_df['BeatsC_mean'] = beats_confidence.mean
    file_df['BeatsC_std'] = beats_confidence.std
    file_df['BeatsC_median'] = beats_confidence.median
    file_df['BeatsC_skw'] = beats_confidence.skew
    file_df['BeatsC_kts'] = beats_confidence.kurtosis

    file_df['BeatsS_mean'] = bars_start.mean
    file_df['BeatsS_std'] = bars_start.std
    file_df['BeatsS_median'] = bars_start.median
    file_df['BeatsS_skw'] = bars_start.skew
    file_df['BeatsS_kts'] = bars_start.kurtosis

    file_df['SC_mean'] = segments_confidence.mean
    file_df['SC_std'] = segments_confidence.std
    file_df['SC_median'] = segments_confidence.median
    file_df['SC_skw'] = segments_confidence.skew
    file_df['SC_kts'] = segments_confidence.kurtosis

    file_df['SS_mean'] = segments_start.mean
    file_df['SS_std'] = segments_start.std
    file_df['SS_median'] = segments_start.median
    file_df['SS_skw'] = segments_start.skew
    file_df['SS_kts'] = segments_start.kurtosis

    file_df['SLM_mean'] = segments_loudness_max.mean
    file_df['SLM_std'] = segments_loudness_max.std
    file_df['SLM_median'] = segments_loudness_max.median
    file_df['SLM_skw'] = segments_loudness_max.skew
    file_df['SLM_kts'] = segments_loudness_max.kurtosis

    file_df['SLMT_mean'] = segments_loudness_max_time.mean
    file_df['SLMT_std'] = segments_loudness_max_time.std
    file_df['SLMT_median'] = segments_loudness_max_time.median
    file_df['SLMT_skw'] = segments_loudness_max_time.skew
    file_df['SLMT_kts'] = segments_loudness_max_time.kurtosis

    file_df['SLS_mean'] = segments_loudness_start.mean
    file_df['SLS_std'] = segments_loudness_start.std
    file_df['SLS_median'] = segments_loudness_start.median
    file_df['SLS_skw'] = segments_loudness_start.skew
    file_df['SLS_kts'] = segments_loudness_start.kurtosis

    file_df['TC_mean'] = tatums_confidence.mean
    file_df['TC_std'] = tatums_confidence.std
    file_df['TC_median'] = tatums_confidence.median
    file_df['TC_skw'] = tatums_confidence.skew
    file_df['TC_kts'] = tatums_confidence.kurtosis

    file_df['TS_mean'] = tatums_start.mean
    file_df['TS_std'] = tatums_start.std
    file_df['TS_median'] = tatums_start.median
    file_df['TS_skw'] = tatums_start.skew
    file_df['TS_kts'] = tatums_start.kurtosis

    return file_df

		
def get_pitch(source_file):
    temp_zeros = np.zeros(pitch_col.__len__())
    file_df = DataFrame([temp_zeros],columns = pitch_col)
    
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

song_analysis_full = DataFrame()  
wrong_file = []

for k in range(file_path.__len__()):
    try:
        details = get_details(file_path[k])
        pitches = get_pitch(file_path[k])
        df_temp = pd.concat([details,pitches],axis = 1)
        song_analysis_full = song_analysis_full.append(df_temp)
        print k
    except:
        wrong_file.append(file_path[k])
        print "wrong file is:",k

song_analysis_full.index = range(song_analysis_full.shape[0])
        
song_analysis_full.to_csv('songs_analysis_ful.csv')

