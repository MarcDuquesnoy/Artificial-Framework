#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.multioutput import MultiOutputRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import pandas as pd
import warnings
import time

warnings.filterwarnings('ignore')


def feature(path):

    """
    :param path: a string with the path of the file
    :return: necessary ressources for the machine learning modeling
    """

    x = pd.read_excel(path)
    x = x.drop_duplicates()

    inputs = x.columns[:-3]
    outputs = x.columns[-3:]

    scale = MinMaxScaler().fit(x[outputs])
    x[outputs] = scale.transform(x[outputs])

    return x, inputs, outputs


def training(data, columns_in, columns_out, model, param_grid):

    """
    :param param_grid: a dict with parameters
    :param columns_out: a list of output features
    :param columns_in: a list of input features
    :param data: a python dataframe
    :param model: a python model
    :return: a trained model
    """

    start_time = time.time()

    XTrain, XTest, YTrain, YTest = train_test_split(data[columns_in], data[columns_out], train_size=0.8)
    estimator = GridSearchCV(MultiOutputRegressor(model), param_grid=param_grid)
    estimator = estimator.fit(XTrain, YTrain)
    print("Score = " + str(estimator.score(XTrain, YTrain)))
    print("\n")
    print("Temps d'entrainement : " + str(int((time.time()-start_time)/60)) + "mn")
    print("\n")

    YPred = pd.DataFrame(estimator.best_estimator_.predict(XTest), columns=columns_out)

    plot_prediction(YPred, YTest)

    return None


def plot_prediction(ytest, pred):

    """
    :param ytest: a dataframe of true values per features
    :param pred: a list of predicted values
    :return: a plot
    """

    for i in ytest.columns:

        fig = plt.figure(figsize=(12, 8))
        ax = plt.gca()
        ax.set_facecolor('xkcd:light grey')

        plt.plot([min(ytest[i]), max(ytest[i])], [min(ytest[i]), max(ytest[i])], label="Perfect fitting", color='black',
                 linestyle='dashed')
        plt.scatter(ytest[i], pred[i], label=i, c="red")

        plt.xlabel("True values", fontsize=15, fontweight="bold")
        plt.ylabel("Predicted values", fontsize=15, fontweight="bold")
        print("R2 score pour la variable "+i+" : "+str(r2_score(ytest[i], pred[i])))
        plt.legend()
        plt.show()


Dataset, out_features, in_features = feature(path='./DonneesInitiales.xlsx')

mod = BaggingRegressor()
grid = {"estimator__n_estimators": [10, 40, 50, 75, 90], 'n_jobs': [1, 2, 3], "estimator__bootstrap": [True],
        "estimator__oob_score": [True], "estimator__max_features": [0.5, 1.0],
        "estimator__min_samples_split": [2, 3, 5, 6, 10]}
grid = {"estimator__n_estimators": [10, 40, 50, 75, 90], 'n_jobs': [1, 2, 3], "estimator__bootstrap": [True],
        "estimator__bootstrap_features": [True], "estimator__oob_score": [True], "estimator__max_samples": [0.5, 1.0],
        "estimator__max_features": [0.5, 1.0]}

# training(Dataset, in_features, out_features, mod, grid)



from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

kernel = C(1.0, (1e-3, 1e3)) * RBF(10, (1e-2, 1e2))
gp = GaussianProcessRegressor(n_restarts_optimizer=9)


XTrain, XTest, YTrain, YTest = train_test_split(Dataset[in_features], Dataset[out_features[0]], train_size=0.8)


gp.fit(XTrain, YTrain)

y_pred, sigma = gp.predict(XTest, return_std=True)

plt.scatter(YTest, y_pred)
plt.show()

