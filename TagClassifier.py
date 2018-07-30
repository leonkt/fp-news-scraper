from collections import Counter 

import numpy as np

from sklearn.cluster import KMeans
class TagClassifier:
	# Initialize by recording the numeric count of certain words in the article body scraped.
	def __init__(text):
		counts = Counter(text)
		self.train = np.array(list(counts.items()), dtype=dtype)

	def perf_km()
