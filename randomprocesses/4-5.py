from math import cos, sin, sqrt, log, pi
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

x1 = np.random.uniform(0, 1, 100000)
x2 = np.random.uniform(0, 1, 100000)

ksi1 = []
for x in range(len(x1)):
    ksi1.append(sqrt((-1)*log(x1[x]))*cos(2*pi*x2[x]))

ksi2 = []
for x in range(len(x1)):
    ksi2.append(sqrt((-1)*log(x1[x]))*sin(2*pi*x2[x]))

# fig, (ax1, ax2) = plt.subplots(2)
# ax1.hist(ksi1, 15, color='red')
# ax2.hist(ksi2, 15)
# plt.show()

a = True
while(a):
    n1 = 5000
    n = int(input('Enter N: '))
    uni = np.empty((0, n1), float)
    for i in range(n):
        uni = np.append(uni, [np.random.uniform(0, 1, n1)], axis=0)

    ksi = []
    res = 0
    for i in range(n1):
        for j in range(n):
            res = res + uni[j][i]-0.5
        res = res * sqrt(12/n)
        ksi.append(res)
        res = 0


    # fig, (ax1) = plt.subplots(1)
    # ax1.hist(ksi, 15, color='red')
    # plt.show()
    # print(stats.shapiro(ksi))
    print(stats.anderson(ksi, dist = 'norm'))
    # print(stats.jarque_bera(ksi))
    # print(stats.mstats.normaltest(ksi))
    # print(stats.kstest(ksi, 'norm'))
    if (int(input('Wanna continue? ')) == 0):
        a = False

print(stats.anderson(ksi1, dist = 'norm'))
print(stats.anderson(ksi2, dist = 'norm'))
# print(stats.shapiro(ksi1))
# print(stats.shapiro(ksi2))
# print(stats.jarque_bera(ksi1))
# print(stats.jarque_bera(ksi2))
# print(stats.mstats.normaltest(ksi1))
# print(stats.mstats.normaltest(ksi2))
# print(stats.kstest(ksi1, 'norm'))
# print(stats.kstest(ksi2, 'norm'))