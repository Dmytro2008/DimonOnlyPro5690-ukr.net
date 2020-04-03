import numpy as np
import pickle as pkl
from abc import ABC, abstractmethod

dataset = pkl.load(open('train_int8.pkl', mode='rb'))
class Prediction(ABC):
    @abstractmethod
    def predict(x):
        pass
    @abstractmethod
    def difference_in_distance(x_val, x_composion):
        pass
    @abstractmethod
    def sort_tags(distance_matrix, y_composion):
        pass
    @abstractmethod
    def create_matrix(matrix):
        pass


class Realisation(Prediction):
    def predict(x):
        amount = 35500
        k = 7
        x_composion = dataset[0][:amount]
        y_composion = dataset[1][:amount]
        y_sorted = sort_tags(difference_in_distance(x, x_composion), y_composion)
        nearest_neib = y_sorted[:, :k]
        matrix = np.stack(create_matrix(np.bincount(nearest_neib[i])) for i in range(nearest_neib.shape[0]))
        y = np.zeros(shape=(len(x[:, 0]), 1))
        for i in range(nearest_neib.shape[0]):
            a = matrix[i].tolist()
            y[i, 0] = a.index(max(a))
        return y


    def difference_in_distance(x_val, x_composion):
        distance_matrix = x_val @ (1 - np.transpose(x_composion)) + (1 - x_val) @ np.transpose(x_composion)
        return distance_matrix


    def sort_tags(distance_matrix, y_composion):
        distance_matrix_ordered = np.argsort(distance_matrix, kind='quicksort')
        return y_composion[distance_matrix_ordered]


    def create_matrix(matrix):
        new_matrix = np.array([0] * 10)
        for i in range(len(matrix)):
            new_matrix[i] = matrix[i]
        return new_matrix

