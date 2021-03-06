#!/usr/bin/env python
# encoding: utf-8

import numpy as np


class Learner():

    def __init__(self, base_learner, init_x, init_y):

        if len(init_x) != len(init_y):
            raise ValueError("X and Y need to be same length")

        self.base_learner = base_learner
        self.train_x = init_x
        self.train_y = init_y

        # If training data contains single label
        self.model = self.base_learner.fit(self.train_x, self.train_y)

    def refine_model(self, feature, target):
        self.train_x = np.vstack((self.train_x, feature))
        self.train_y = np.concatenate((self.train_y, target))

        # print len(self.train_x)
        self.model = self.base_learner.fit(self.train_x, self.train_y)
        return self.get_trained_size()

    def score(self, test_x, test_y):
        return self.model.score(test_x, test_y)

    def get_pool_size(self):
        return len(self.train_pool)

    def get_trained_size(self):
        """
        Get the training size for the last fit
        """
        return len(self.train_x)

    def get_model(self):
        return self.model

    def get_model_coef(self):
        return np.reshape(self.model.coef_, self.model.coef_.shape[1])

    def is_activated(self):
        return self.activated

    @staticmethod
    def dis(x, v):
        """
        Calculate the distance between point and a hyperplane v
        """

        w = np.subtract(0, np.subtract(x, v))
        return np.linalg.norm(np.dot(v, w)) / np.linalg.norm(v)

