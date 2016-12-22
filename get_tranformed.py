import h5py
import numpy as np
import pandas as pd
from pandas import DataFrame
from scipy import stats
from sklearn.decomposition import PCA
from scipy.spatial import distance

# Load and parse the data
raw_data_total = DataFrame.from_csv('/Users/shiluyuan/Downloads/bigdataproject/songs_analysis_full.csv')

'''there are total 116 features'''
raw_data = raw_data_total[raw_data_total.columns.values[1:116]]

scale_data = DataFrame(columns=raw_data.columns.values)

for col in raw_data.columns.values:
    scale_data[col] = stats.zscore(raw_data[col])
    
scale_data = DataFrame.as_matrix(scale_data)

pca = PCA(n_components=27)
pca.fit(scale_data)

'''transform data is the low dimension data'''
transform_data = pca.transform(scale_data)
song_num = transform_data.shape[0]


file_path = raw_data_total['file_path']

artist_name = np.array([])
song_name = np.array([])

'''get song title and artist name'''
for k in range(song_num):
    file_temp = h5py.File(file_path[k],'r')
    song_info = DataFrame(file_temp['metadata']['songs'][()])
    artist_name_temp = song_info['artist_name']
    song_name_temp = song_info['title']
    
    artist_name = np.append(artist_name,artist_name_temp)
    song_name = np.append(song_name,song_name_temp)

song_artist = DataFrame({'artist_name':artist_name,
                         'song_name':song_name})
'''all the song names and artist names'''
song_artist.to_csv('song_artist.csv')

feature_data = DataFrame(transform_data)

recommender_data = pd.concat([song_artist,feature_data],axis=1)
recommender_data.to_csv('recommend_data.csv')    
    
    
    