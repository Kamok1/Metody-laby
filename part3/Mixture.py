from sklearn.cluster import KMeans
from sklearn.base import BaseEstimator, clone
from typing import List
import numpy as np

class SimpleMixtureOfExperts:
    def __init__(self, experts: List[BaseEstimator], random_state: int = 1) -> None:
        self.experts: List[BaseEstimator] = experts
        self.n_clusters: int = len(experts)
        self.kmeans: KMeans = KMeans(n_clusters=self.n_clusters, random_state=random_state)
        self.cluster_experts: dict[int, BaseEstimator] = {}

    def fit(self, X: np.ndarray, y: np.ndarray) -> 'SimpleMixtureOfExperts':
        clusters = self.kmeans.fit_predict(X)
        for i in range(self.n_clusters):
            idx = np.where(clusters == i)
            X_cluster, y_cluster = X[idx], y[idx]
            expert = clone(self.experts[i])
            expert.fit(X_cluster, y_cluster)
            self.cluster_experts[i] = expert

        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        clusters = self.kmeans.predict(X)
        preds = np.zeros(X.shape[0])
        for i in range(self.n_clusters):
            idx = np.where(clusters == i)
            if len(idx[0]) > 0:
                preds[idx] = self.cluster_experts[i].predict(X[idx])
        return preds
