import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

def mean():
    means_list = [df[i].mean() for i in range(len(df.columns))]
    print("List with means:", means_list)


def dispersion():
    disp_list = [pow(df[i].std(), 2) for i in range(len(df.columns))]
    print('List with dispersions', disp_list)


def histogram():
    plt.hist(column_1,50,label = 'column 1')
    plt.hist(column_2,50,label = 'column 2')
    plt.hist(column_3,50,label = 'column 3')
    plt.hist(column_4,50,label = 'column 4')
    plt.hist(column_5,50,label = 'column 5')
    plt.hist(column_6,50,label = 'column 6')
    plt.legend()
    plt.show()


def check_norm_distr():
    list_distr = [scipy.stats.kstest(column_1, "norm")[1],scipy.stats.kstest(column_2, "norm")[1],
            scipy.stats.kstest(column_3, "norm")[1],scipy.stats.kstest(column_4, "norm")[1],
            scipy.stats.kstest(column_5, "norm")[1],scipy.stats.kstest(column_6, "norm")[1]]
    for i in range (len(list_distr)):
        print('P-value for {} test is {}\n So, this is not normal distibution'.format((i+1), list_distr[i]))


def correlation_matrix(dff):
    global corr
    corr = dff.corr()
    corr.style.background_gradient(cmap='coolwarm')
    return corr


def eigenvalues_eigenvectors(corr):
    eig_val, eig_vec = np.linalg.eig(corr)
    eig_pairs = []
    for i in range(len(eig_val)):
        eig_pairs.append((eig_val[i], eig_vec[i]))
    eig_pairs = sorted(eig_pairs, key= lambda x: x[0], reverse = True)
    for i in range(len(eig_pairs)):
        print('Власне значення: {} \nВласний вектор: {} \n'.format(eig_pairs[i][0], eig_pairs[i][1]))
    return "all is good"




if __name__ == '__main__':
    a = pd.read_csv('kpi3.txt', sep='\s+', header=None)
    df = a.loc[:, a.columns != 0]
    df.columns = [i for i in range(6)]
    column_1 = df[0].values
    column_2 = df[1].values
    column_3 = df[2].values
    column_4 = df[3].values
    column_5 = df[4].values
    column_6 = df[5].values
    mean()
    dispersion()
    histogram()
    check_norm_distr()
    m = correlation_matrix(df)
    print('Correlation matrix: \n', m)
    eig = eigenvalues_eigenvectors(m)
    print(eig)
