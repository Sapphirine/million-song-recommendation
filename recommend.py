#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 16:49:16 2016

@author: shiluyuan
"""
import numpy as np
from pandas import DataFrame
from scipy.spatial import distance
'''remember to change file path'''
'''this is only a demo, more detail programs are in recommendation_system folder'''
recommend_data = DataFrame.from_csv('/Users/shiluyuan/Downloads/bigdataproject/recommend_data.csv')

input_song = 'My Love (Album Version)'

song_name = recommend_data['song_name']
artist_name = recommend_data['artist_name']

feature = recommend_data[recommend_data.columns.values[2:39]]

feature_matrix = np.asmatrix(feature)

index = np.where(song_name==input_song)
index = index[0][0]
song_distance = np.array([])

song_num = recommend_data.shape[0]

for j in range(song_num):
    
    dist = distance.cosine(feature_matrix[index],feature_matrix[j])
    song_distance = np.append(song_distance,dist)
dist_df = DataFrame({'song_name':song_name,
                     'artist_name':artist_name,
                     'song_dist':song_distance})

dist_df_sort = dist_df.sort(['song_dist'],ascending=True)
'''give the top three'''
top_three_df = dist_df_sort[1:4]

similiar_artist = np.array(top_three_df['artist_name'])
similiar_song = np.array(top_three_df['song_name'])
recommend_dic = {'similiar_song':similiar_song,'similiar_artist':similiar_artist}