from collections import Counter 

import numpy as np

import os

from sklearn.cluster import KMeans

from sklearn.decomposition import PCA


class TagClassifier:
	''' Initialize by recording the numeric count of certain words in the article
		body scraped. '''

	def __init__(self, text):
        counts = Counter(text)
        self.features = len(counts.keys())
        self.input_dat = np.array(list(counts.items()), dtype=dtype)

	''' The number of components to remove was determined by a component vs. info.
        loss plot not shown
        12 appears to be the "elbow" at which the information loss and feature
        numbers are balanced'''

    def perf_PCA(self):
        pca = PCA(n_components=12)
        princ_comp = pca.fit_transform(self.input_dat)

	''' PCA was performed to speed up the k-means algorithm. Also, Euclidean dists.
        become inflated
        in higher dimensional spaces; chose few features to properly fit the data.
        Spectral clustering chosen because of the small number of clusters and
        relatively small number of samples'''
    def perf_km(self):
        perf_PCA()
        km = KMeans(init='k-means ++', n_clusters=2, n_init=30)
        km.fit(self.input_dat)
        classes = Kmeans.score(self.input_dat)
        return classes



