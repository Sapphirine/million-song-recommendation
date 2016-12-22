""" get all the basic information songs """
import os
import numpy as np
import pandas as pd
from pandas import DataFrame
import h5py
from scipy.stats import kurtosis

'''get an tree structurename  '''
file_path = []
file_dic = '/Users/shiluyuan/Downloads/bigdataproject/musicdata'
for dirpath, dirnames, filenames in os.walk(file_dic):
    for files in filenames:
        if (os.path.splitext(files)[1] == '.h5'):
            file_path.append(os.path.join(dirpath, files))


'''get an tree structurename  '''
file_tree_name = []
file0 = h5py.File(file_path[0],'r')

def showtreename(name):
    file_tree_name.append(name)           
            
file0.visit(showtreename)

'''get all the songs information'''
analysis_songs = DataFrame()
metadata_songs = DataFrame()
musicbrainz_songs = DataFrame()

file_example = h5py.File(file_path[0],'r')
analysis_songs_example = DataFrame(file_example['analysis']['songs'][()])
metadata_songs_example = DataFrame(file_example['metadata']['songs'][()])
musicbrainz_songs_example = DataFrame(file_example['musicbrainz']['songs'][()])

for k in range(file_path.__len__()):
    file_temp = h5py.File(file_path[k],'r')
    file_temp_analysis_songs = DataFrame(file_temp['analysis']['songs'][()])
    file_temp_metadata_songs = DataFrame(file_temp['metadata']['songs'][()])
    file_temp_musicbraniz_songs = DataFrame(file_temp['musicbrainz']['songs'][()])
    if (file_temp_analysis_songs.columns.values in analysis_songs_example.columns.values and 
    	file_temp_metadata_songs.columns.values in metadata_songs_example.columns.values and
    	file_temp_musicbraniz_songs.columns.values in musicbrainz_songs_example.columns.values):
    	
        analysis_songs = analysis_songs.append(file_temp_analysis_songs)
        metadata_songs = metadata_songs.append(file_temp_metadata_songs)
        musicbrainz_songs = musicbrainz_songs.append(file_temp_musicbraniz_songs)
    print k
songs_summary = pd.concat([analysis_songs, metadata_songs,musicbrainz_songs], axis=1)
songs_summary.index = range(file_path.__len__())

songs_summary.to_csv("songs_info.csv")

