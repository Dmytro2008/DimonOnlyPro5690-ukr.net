from math import cos, sin, pi
import matplotlib.pyplot as plt
import numpy as np
# from scipy import stats


# def ksi_t(t_i, eta1, eta2, M):
#     ksi1 = 0
#     for i in range(M):
#         lambda_val = pi * i
#         ksi1 = ksi1 + eta1[i] * cos(lambda_val * t_i) + eta2[i] * sin(lambda_val * t_i)
#     return ksi1


# m = 100
# t = np.arange(0, 1, 1/m)
# num1 = 1000
# n1 = np.empty((0, num1), float)
# n2 = np.empty((0, num1), float)
# for i in range(m):
#     mu = 0
#     sd = 1/((1+pi*(i**2))**2)
#     # print(sd)
#     n1 = np.append(n1, [np.random.normal(mu, sd, num1)], axis=0)
#     n2 = np.append(n2, [np.random.normal(mu, sd, num1)], axis=0)
#     plt.plot(n1[i])
#     plt.plot(n2[i])
# plt.show()
# print(n1)
# print(n2)

# ksi = [[] for i in range(num1)]
# for i in range(m):
#     for j in t:
#         x = ksi_t(j, n1[i], n2[i], num1)
#         ksi[i].append(x)
#     plt.plot(t, ksi[i])
#
#
# plt.show()
m = 100

num1 = 100
t = np.arange(0, 1, 1/num1)
# n1 = np.empty((0, num1), float)
# n2 = np.empty((0, num1), float)
# for i in range(m):
#     mu = 0
#     sd = 1/((1+pi*(i**2))**2)
#     n1 = np.append(n1, [np.random.normal(mu, sd, num1)], axis=0)
#     n2 = np.append(n2, [np.random.normal(mu, sd, num1)], axis=0)
#
# print(n1)
# print(n2)
tru = []
for k in range(num1):
    n1 = np.empty((0, num1), float)
    n2 = np.empty((0, num1), float)
    for i in range(m):
        mu = 0
        sd = 1/((1+pi*(i**2))**2)
        n1 = np.append(n1, [np.random.normal(mu, sd, num1)], axis=0)
        n2 = np.append(n2, [np.random.normal(mu, sd, num1)], axis=0)
    ksi = []
    res = 0
    for i in range(num1):
        for j in range(m):
            lambda_val = j*pi
            # print(i, j ,k)
            res = res + n1[j][i] * cos(lambda_val * t[k]) + n2[j][i] * sin(lambda_val * t[k])
        ksi.append(res)
        res = 0
    tru.append(ksi)
    plt.plot(t, ksi)

# print(tru)

for i in range(num1):
    print("Moment of time {}: ".format(i))
    l = [j[i] for j in tru]
    mean_val = np.mean(l)
    var_val = np.var(l)
    print("Mean - {}\nVariation - {}".format(mean_val, var_val))

plt.show()