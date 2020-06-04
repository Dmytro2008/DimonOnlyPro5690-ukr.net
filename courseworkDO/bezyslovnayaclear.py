import numpy as np
import matplotlib.pyplot as plt

counter1 = 0


def evaluate_f(x1, x2):
    global counter1
    counter1 += 1
    #return (100*(x1**2 - x2)**2) + (x1 - 1)**2
    return (10 * (x1 - x2) ** 2 + (x1 - 1) ** 2) ** (1 / 4)


def grad_center(x, h_epsilon):
    h = h_epsilon * np.linalg.norm(x)
    dx = (evaluate_f(x[0] + h, x[1]) - evaluate_f(x[0] - h, x[1])) / (2 * h)
    dy = (evaluate_f(x[0], x[1] + h) - evaluate_f(x[0], x[1] - h)) / (2 * h)
    return np.array([dx, dy])


def grad_right(x, h_epsilon):
    h = h_epsilon * np.linalg.norm(x)
    dx = (evaluate_f(x[0] + h, x[1]) - evaluate_f(x[0], x[1])) / h
    dy = (evaluate_f(x[0], x[1] + h) - evaluate_f(x[0], x[1])) / h
    return np.array([dx, dy])


def grad_left(x, h_epsilon):
    h = h_epsilon * np.linalg.norm(x)
    dx = (evaluate_f(x[0], x[1]) - evaluate_f(x[0] - h, x[1])) / h
    dy = (evaluate_f(x[0], x[1]) - evaluate_f(x[0], x[1] - h)) / h
    return np.array([dx, dy])


def gold(start, svenn, direction, epsilon_la):
    x0 = start[0]
    y0 = start[1]
    x = direction[0]
    y = direction[1]
    current_interval = svenn
    L = current_interval[1] - current_interval[0]
    la_1 = current_interval[0] + 0.382 * L
    la_2 = current_interval[0] + 0.618 * L
    f_la1 = evaluate_f(x0 + (la_1 * x), y0 + (la_1 * y))
    f_la2 = evaluate_f(x0 + (la_2 * x), y0 + (la_2 * y))
    while (L > epsilon_la):
        if (f_la1 < f_la2):
            current_interval = [current_interval[0], la_2]
            f_la2 = f_la1
            L = current_interval[1] - current_interval[0]
            la_1 = current_interval[0] + 0.382 * L
            la_2 = current_interval[0] + 0.618 * L
            f_la1 = evaluate_f(x0 + (la_1 * x), y0 + (la_1 * y))

        elif (f_la1 > f_la2):
            current_interval = [la_1, current_interval[1]]
            f_la1 = f_la2
            L = current_interval[1] - current_interval[0]
            la_1 = current_interval[0] + 0.382 * L
            la_2 = current_interval[0] + 0.618 * L
            f_la2 = evaluate_f(x0 + (la_2 * x), y0 + (la_2 * y))

    return (current_interval[0] + current_interval[1]) / 2


def svenn_la2(direction, start, dx, case, la0=0):
    x0 = start[0]
    y0 = start[1]
    x = direction[0]
    y = direction[1]
    nX = np.linalg.norm(start)
    f0 = evaluate_f(x0 + ((la0) * x), y0 + ((la0) * y))
    values_list = [f0]
    la_list = [la0]
    f1_l = evaluate_f(x0 + ((la0 - dx) * x), y0 + ((la0 - dx) * y))
    f1_r = evaluate_f(x0 + ((la0 + dx) * x), y0 + ((la0 + dx) * y))
    if f1_l > f0 and f0 > f1_r:
        determinator = 1
        values_list.append(f1_r)
        la_list.append(la0 + dx)
    elif f1_l < f0 and f0 < f1_r:
        determinator = -1
        values_list.append(f1_l)
        la_list.append(la0 - dx)
    elif f1_l > f0 and f0 < f1_r:
        if case == 1:
            return [la0 - dx, la0 + dx]
        else:
            return [la0 - dx, la0, la0 + dx]
    i = 1

    while (values_list[i] < values_list[i - 1]):
        la_i = la_list[i] + determinator * (2 ** i) * dx
        la_list.append(la_i)
        values_list.append(evaluate_f(x0 + ((la_i) * x), y0 + ((la_i) * y)))
        i += 1

    last4 = [la_list[i], (la_list[i] + la_list[i - 1]) / 2, la_list[i - 1], la_list[i - 2]]
    last4_evaluated = []

    for la in last4:
        last4_evaluated.append(evaluate_f(x0 + ((la) * x), y0 + ((la) * y)))

    ind = last4_evaluated.index(min(last4_evaluated))
    if case == 1:
        return sorted([last4[ind + 1], last4[ind - 1]])
    else:
        return sorted([last4[ind + 1], last4[ind], last4[ind - 1]])


def dsk_powell(x, la, s, accuracy):

    la = sorted(la)
    s_norm = 1
    x1 = la[0]
    x2 = la[1]
    x3 = la[2]
    dx = abs(x2 - x1)
    f1 = evaluate_f(x[0] + x1 * s[0] / s_norm, x[1] + x1 * s[1] / s_norm)
    f2 = evaluate_f(x[0] + x2 * s[0] / s_norm, x[1] + x2 * s[1] / s_norm)
    f3 = evaluate_f(x[0] + x3 * s[0] / s_norm, x[1] + x3 * s[1] / s_norm)
    x_dsk = x2 + (dx * (f1 - f3)) / (2 * (f1 - 2 * f2 + f3))
    f_dsk = evaluate_f(x[0] + x_dsk * s[0] / s_norm, x[1] + x_dsk * s[1] / s_norm)
    if ((x2 - x_dsk) < accuracy) and ((f2 - f_dsk) < accuracy):
        return x_dsk
    x_top = x_dsk
    end = False
    while not end:
        lis = sorted([x1, x2, x3, x_top])
        ind = lis.index(x_top)
        if ind == 0:
            lis = [lis[ind], lis[ind + 1], lis[ind + 2]]
        elif ind == 3:
            lis = [lis[ind - 2], lis[ind - 1], lis[ind]]
        else:
            lis = [lis[ind - 1], lis[ind], lis[ind + 1]]
        x1 = lis[0]
        x2 = lis[1]
        x3 = lis[2]
        f1 = evaluate_f(x[0] + x1 * s[0] / s_norm, x[1] + x1 * s[1] / s_norm)
        f2 = evaluate_f(x[0] + x2 * s[0] / s_norm, x[1] + x2 * s[1] / s_norm)
        f3 = evaluate_f(x[0] + x3 * s[0] / s_norm, x[1] + x3 * s[1] / s_norm)
        a1 = (f2 - f1) / (x2 - x1)
        a2 = (1 / (x3 - x2)) * ((f3 - f1) / (x3 - x1) - (f2 - f1) / (x2 - x1))

        x_top = (x1 + x2) / 2 - a1 / (2 * a2)
        f_x_top = evaluate_f(x[0] + x_top * s[0] / s_norm, x[1] + x_top * s[1] / s_norm)
        f_list = [f1, f2, f3, f_x_top]
        list_x = [x1, x2, x3, x_top]
        f_min = min(f_list)
        inx_min = f_list.index(f_min)
        x_min = list_x[inx_min]
        if (((f_min - f_x_top) < accuracy) and (x_min - x_top < accuracy)):
            end = True
    return x_top


def plot_rozenbrock(way):
    rosenbrockfunction = lambda x, y: (1 - x) ** 2 + 100 * (y - x ** 2) ** 2
    X, Y = np.meshgrid(np.linspace(-2, 2., 1000), np.linspace(-1, 2, 1000))
    Z = rosenbrockfunction(X, Y)
    x_coords = []
    for i in range(len(way)):
        x_coords.append(way[i][0])
    y_coords = []
    for i in range(len(way)):
        y_coords.append(way[i][1])
    plt.contour(X, Y, Z, np.logspace(-0.5, 3.5, 20, base=10), cmap='Accent')
    plt.scatter(x_coords, y_coords, color='red')
    plt.plot(x_coords, y_coords, color='red')
    plt.title('Rosenbrock Function: $f(x,y) = (1-x)^2+100(y-x^2)^2$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def plot_kornevaya(x):
    start, stop, n_values = -2, 2, 2000
    x_vals = np.linspace(start, stop, n_values)
    y_vals = np.linspace(start, stop, n_values)
    X, Y = np.meshgrid(x_vals, y_vals)

    Z = (10 * (X - Y) ** 2 + (X - 1) ** 2) ** (1 / 4)

    x_list = []
    y_list = []
    for lis in x:
        x_list.append(lis[0])
        y_list.append(lis[1])

    plt.contour(X, Y, Z, levels=50)
    plt.plot(x_list, y_list, color="red")
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.scatter(x_list, y_list, color="red")
    plt.show()


def Koshi1(x0, epsilon, h_epsilon, odnom_epsilon, dx, derivative, case=1):
    x = [np.array(x0)]
    end = False
    k = 0
    while not end:
        grad = derivative(x[k], h_epsilon)
        S = -grad
        svenn = svenn_la2(S, x[k], dx, case=case)
        if case == 1:
            odnom_pousk = gold(x[k], svenn, S, odnom_epsilon)
        else:
            odnom_pousk = dsk_powell(x[k], svenn, S, odnom_epsilon)
        la_opt = odnom_pousk
        x_new = x[k] + la_opt * (S)
        x.append(x_new)
        print('Koshu:', x_new)
        if (np.linalg.norm(x[k] - x[k + 1]) / np.linalg.norm(x[k]) < epsilon) \
                and ((evaluate_f(x[k][0], x[k][1]) - evaluate_f(x[k + 1][0], x[k + 1][1])) < epsilon):
            break
        k += 1
    return x


def Partan(x0, epsilon, h_epsilon, odnom_epsilon, dx, derivative, case=1):
    x = [np.array(x0)]
    end = False
    k = 1
    while not end:
        grad = derivative(x[k - 1], h_epsilon)
        if k % 3 == 0:
            S = x[k - 1] - x[k - 3]
        else:
            S = -grad
        svenn = svenn_la2(S, x[k - 1], dx, case=case)
        if case == 1:
            odnom_pousk = gold(x[k - 1], svenn, S, odnom_epsilon)
        else:
            odnom_pousk = dsk_powell(x[k - 1], svenn, S, odnom_epsilon)
        la_opt = odnom_pousk
        x_new = x[k - 1] + la_opt * (S)
        x.append(x_new)
        print('Partan', x_new)
        if (np.linalg.norm(grad) < epsilon): # (np.linalg.norm(x[k-1]-x[k])/np.linalg.norm(x[k-1])<epsilon) \
#                 and ((evaluate_f(x[k-1][0],x[k-1][1])-evaluate_f(x[k][0],x[k][1]))<epsilon):
            break
        k += 1
    return x


def analysis(epsilon, h_epsilon, odnom_epsoilonnn, dx, deriv):
    x_Koshu = []
    x_Partan = []
    f_Koshu = []
    f_Partan = []
    counter_Koshu = []
    counter_Partan = []
    deriv_type = deriv.__name__
    for dxx in dx:
        global counter1
        counter1 = 0
        x1 = Koshi1([-1.2, 0], epsilon, h_epsilon, odnom_epsoilonnn , dxx, grad_center,case=1)
        counter_Koshu.append(counter1)
        counter1 = 0
        x2 = Partan([-1.2, 0], epsilon, h_epsilon, odnom_epsoilonnn, dxx, grad_center, case=1)
        counter_Partan.append(counter1)
        counter1 = 0
        x_Koshu.append(x1)
        x_Partan.append(x2)
        f_Koshu.append(evaluate_f(x1[0], x1[1]))
        f_Partan.append(evaluate_f(x2[0], x2[1]))
    return x_Koshu, x_Partan, f_Koshu, f_Partan, counter_Koshu, counter_Partan, deriv_type


