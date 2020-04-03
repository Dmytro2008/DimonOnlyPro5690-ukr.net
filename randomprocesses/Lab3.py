import random
from functools import reduce


def squared_sum(array):
    return reduce(lambda total, current: total + current ** 2, array, 0)


def estimate_dispersion(array):
    return (squared_sum(array) - (sum(array) ** 2) / n) / (len(array) - 1)


def S0_squared(factors):
    factor_values_length = len(list(factors.values())[0])
    return (sum([squared_sum(factor) for factor in factors.values()]) -
            (squared_sum([sum(factor) for factor in factors.values()]) / factor_values_length)) / (
                   len(factors) * (factor_values_length - 1))


def S_squared(factors):
    factor_values_length = len(list(factors.values())[0])
    return (sum([squared_sum(factor) for factor in factors.values()]) -
            ((sum([sum(factor) for factor in factors.values()]) ** 2) / (factor_values_length * len(factors)))) / (
                   len(factors) * factor_values_length - 1)


def average(array):
    return sum(array) / len(array)


def SA_squared(factors):
    factor_values_length = len(list(factors.values())[0])
    factors_average = [average(factor) for factor in factors.values()]
    total_average = average(factors_average)

    return (sum(
        [(factor_average - total_average) ** 2 for factor_average in factors_average])) * factor_values_length / (
                   len(factors) - 1)


def build_double_factor_dispersion_data(coefficients):
    return [[[value + random.random() for _ in range(m)] for value in row] for row in coefficients]


def double_factor_dispersion_cell_average(data):
    return [[average(values) for values in row] for row in data]


def Q1(matrix):
    return sum(sum([value ** 2 for value in row]) for row in matrix)


def Q2(matrix):
    def add_vectors(first, second):
        return [first[i] + second[i] for i in range(len(first))]

    def columns_sum(array):
        return reduce(lambda columns_total, current: add_vectors(columns_total, current), array,
                      [0 for _ in range(len(array[0]))])

    return sum([value ** 2 for value in columns_sum(matrix)]) / len(matrix)


def Q3(matrix):
    return (sum([sum(row) ** 2 for row in matrix])) / (len(matrix[0]))


def Q4(matrix):
    return (sum([sum(row) for row in matrix]) ** 2) / (len(matrix) * len(matrix[0]))


def S0_squared_double(matrix):
    return (Q1(matrix) + Q4(matrix) - Q2(matrix) - Q3(matrix)) / ((len(matrix) - 1) * (len(matrix[0]) - 1))


def SA_squared_double(matrix):
    return (Q2(matrix) - Q4(matrix)) / (len(matrix) - 1)


def SB_squared_double(matrix):
    return (Q3(matrix) - Q4(matrix)) / (len(matrix[0]) - 1)


def Q5(factors):
    return sum([sum([sum([value ** 2 for value in array]) for array in row]) for row in factors])


def SAB_squared_double(factors):
    averages = double_factor_dispersion_cell_average(factors)
    return (Q5(factors) - m * Q1(averages)) / (len(averages) * len(averages[0]) * (m - 1))


N = 5
n = 1000
m = 100
with open("V2.txt") as f:
    data = f.read()

data = data.split('\n')

x, y, z = zip(*[map(float, s.split(',')) for s in data])

print(x[0])
print(y[0])
print(z[0])
single_data = {
    "A1": y,
    "A2": z
}

factors_dispersion = dict()
for key, values in single_data.items():
    factors_dispersion[key] = estimate_dispersion(values)

print("Single-factor dispersion analysis:")
print("g - {0}".format(max(factors_dispersion.values()) / sum(factors_dispersion.values())))
print("S0^2 - {0}".format(S0_squared(single_data)))
print("S^2 - {0}".format(S_squared(single_data)))
print("SA^2 - {0}".format(SA_squared(single_data)))
print("SA^2 / S^2 - {0}".format(SA_squared(single_data) / S_squared(single_data)))
