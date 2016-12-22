import os
import numpy as np
import pandas as pd
from pandas import DataFrame
import h5py
'''remember to change path'''
'''count the word frequency for each cluster'''
cluster_data = DataFrame.from_csv("/Users/shiluyuan/Downloads/bigdataproject/cluster.csv")

'''group number is 0,1,2 and 3'''
def get_word_frequency(group):
    artist_terms_0 = np.array([])
    artist_terms_0_freq = np.array([])

    for k in range(cluster_data.shape[0]):
        file_name = cluster_data['file_path'][k]
        file_temp = h5py.File(file_name,'r')
        artist_terms = file_temp['metadata']['artist_terms'][()]
        artist_terms_freq = file_temp['metadata']['artist_terms_freq'][()]
        artist_terms_weight = file_temp['metadata']['artist_terms_weight'][()]
	    
        if cluster_data['cluster'][k] == group:
            for word in artist_terms:
                if not word in artist_terms_0:
                    artist_terms_0 = np.append(word,artist_terms_0)

    artist_terms_0 = np.ndarray.tolist(artist_terms_0)
    artist_terms_0_freq = np.zeros(artist_terms_0.__len__())
    artist_terms_0_weight = np.zeros(artist_terms_0.__len__())
    artist_terms_0_addone = np.zeros(artist_terms_0.__len__())

    for k in range(cluster_data.shape[0]):
        file_name = cluster_data['file_path'][k]
        file_temp = h5py.File(file_name,'r')
        artist_terms = file_temp['metadata']['artist_terms'][()]
        artist_terms_freq = file_temp['metadata']['artist_terms_freq'][()]
        artist_terms_weight = file_temp['metadata']['artist_terms_weight'][()] 
        if cluster_data['cluster'][k] == group:
            for word in artist_terms:
                index = artist_terms_0.index(word)
                index_in = np.where(artist_terms == word)
                weight = artist_terms_weight[index_in]
                freq = artist_terms_freq[index_in]
                
                artist_terms_0_freq[index] += freq
                artist_terms_0_weight[index] += weight
                artist_terms_0_addone[index] += 1

    frequency_table_0 = DataFrame({'artist_terms':artist_terms_0,
                                   'frenquency':artist_terms_0_freq,
                                   'weight':artist_terms_0_weight,
                                   'add_one':artist_terms_0_addone})
    return frequency_table_0
 '''if you want to save to each word cloud file, please change number 0 to 1, 2, 3 for other cluster'''           
group_file = get_word_frequency(0)	
group_file.to_csv('group_0.csv')