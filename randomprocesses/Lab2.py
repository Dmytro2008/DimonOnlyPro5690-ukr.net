import random
import math


def get_population_range(length, left, right):
    return [left + (random.random() * (right - left)) for _ in range(length)]


def estimate_average(array):
    return sum(array) / len(array)


def estimate_dispersion(array):
    average = estimate_average(array)
    return sum([(value - average) ** 2 for value in array]) / (len(array) - 1)


def get_random_selection(array, selection_length):
    random_indexes = random.sample(range(len(array)), selection_length)
    return [array[i] for i in random_indexes]


def DYs(population, selection):
    return (estimate_dispersion(selection) / len(selection)) * (1 - len(selection) / len(population))


def DY(population, selection):
    return (estimate_dispersion(selection) * len(population) ** 2 / len(selection)) * (
            1 - len(selection) / len(population))


def Ys_diff(quantile, population, selection):
    return (quantile * math.sqrt(estimate_dispersion(selection)) / math.sqrt(len(selection))) * math.sqrt(
        1 - len(selection) / len(population))


def NYs_diff(quantile, population, selection):
    return (quantile * math.sqrt(estimate_dispersion(selection)) * len(population) / math.sqrt(
        len(selection))) * math.sqrt(
        1 - len(selection) / len(population))


def Ys_range(population, selection):
    selection_average = estimate_average(selection)
    difference = Ys_diff(1.96, population, selection)
    return [selection_average - difference, selection_average + difference]


def NYs_range(population, selection):
    selection_average = estimate_average(selection)
    population_length = len(population)
    difference = NYs_diff(1.96, population, selection)
    return [population_length * selection_average - difference, population_length * selection_average + difference]


def get_strats(population, left, right, quantity):
    result = []
    for i in range(quantity):
        temp = []
        for value in population:
            if i == 0:
                if left <= value < left + ((right - left) / quantity):
                    temp.append(value)
            else:
                if left + ((i * (right - left)) / quantity) <= value < left + (((i + 1) * (right - left)) / quantity):
                    temp.append(value)
        result.append(temp)
    return result


population = get_population_range(1000, 15, 71)
print("Population Average - {0}".format(estimate_average(population)))
print("Population Dispersion - {0}".format(estimate_dispersion(population)))

selection = get_random_selection(population, 100)
print("Selection Average - {0}".format(estimate_average(selection)))
print("Selection Dispersion - {0}".format(estimate_dispersion(selection)))

print("D(Ys) - {0}".format(DYs(population, selection)))
print("D(Y) - {0}".format(DY(population, selection)))

print("Ys Range - {0}".format(Ys_range(population, selection)))
print("NYs Ragne - {0}".format(NYs_range(population, selection)))
print()

strats = get_strats(population, 15, 71, 10)
strat_selections = []
for i, strat in enumerate(strats):
    print("Strat #{0}".format(i+1))
    print("Weigth - {0}".format(len(strat) / 1000))
    print("Sum - {0}".format(sum(strat)))
    print("Average - {0}".format(estimate_average(strat)))
    print("Dispersion - {0}".format(estimate_dispersion(strat)))

    strat_selection = get_random_selection(strat, int(len(strat) / (len(population) / len(selection))))
    strat_selections.append(strat_selection)
    print("Selection Average - {0}".format(estimate_average(strat_selection)))
    print("Selection Dispersion - {0}".format(estimate_dispersion(strat_selection)))
    print("Total by Selection - {0}".format(len(strat_selection) * estimate_average(strat_selection)))

    print("Strat D(Y) - {0}".format(DY(strat, strat_selection)))
    print("Strat average D(y) - {0}".format(DY(strat, strat_selection) / (1000 ** 2)))

    print()

print("Total by strats:")
sum_strats = sum([sum(strat) for strat in strats])
print("Sum - {0}".format(sum_strats))
print("Average - {0}".format(sum_strats / 1000))

sum_strats_selection = sum([sum(strat_selection) * len(strat_selection) for strat_selection in strat_selections])
print("Sum by strat selections - {0}".format(sum_strats_selection))
print("Average by strat selection - {0}".format(sum_strats_selection / 1000))

print("Total D(Y) by stats - {0}".format(
    sum([DY(strats[i], strat_selections[i]) * len(strat_selections[i]) for i in range(len(strats))])))
print("Total average D(y) by stats - {0}".format(
    sum([DY(strats[i], strat_selections[i]) / (1000 ** 2) for i in range(len(strats))])))
print("Intervals by stats - {0}".format(
    [(sum_strats_selection / 1000) - 1.96 * math.sqrt(
        sum([DY(strats[i], strat_selections[i]) / (1000 ** 2) for i in range(len(strats))])),
     (sum_strats_selection / 1000) + 1.96 * math.sqrt(sum(
         [DY(strats[i], strat_selections[i]) / (1000 ** 2) for i in range(len(strats))]))]))
