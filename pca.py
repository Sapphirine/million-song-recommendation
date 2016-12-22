import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import metrics
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from scipy.cluster import hierarchy

'''remenber to change working path'''
raw_data = DataFrame.from_csv('/Users/shiluyuan/Downloads/bigdataproject/songs_analysis_full.csv')

'''there are total 116 features'''
raw_data = raw_data[raw_data.columns.values[1:116]]

scale_data = DataFrame(columns=raw_data.columns.values)

for col in raw_data.columns.values:
    scale_data[col] = stats.zscore(raw_data[col])

scale_data.to_csv('scale_data.csv')   
    
scale_data = DataFrame.as_matrix(scale_data)

pca = PCA(n_components=27)
pca.fit(scale_data)


for k in range(pca.explained_variance_ratio_.shape[0]):
    print k,'_', sum(pca.explained_variance_ratio_[0:k])

transform_data = pca.transform(scale_data)

'''write the scale data to csv'''
DataFrame(transform_data).to_csv('transform_data.csv')

'''try hierarchy clustering'''
Z = hierarchy.linkage(transform_data, method='ward', metric='euclidean')
plt.figure()
dn = hierarchy.dendrogram(Z)