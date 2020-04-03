import pandas as pd
import numpy as np



def dispersion(df):
    print('Однофакторный анализ:')
    disp = []
    for i in range(len(df.columns)):
        disp.append(df[i].values.var())
    print('dispersions:',disp)
    g = (max(disp))/sum(disp)
    print("g = ",g)


def Qevaluate(df):
    summ = []
    Q1 = 0
    Q2 = 0
    Q3 = 0
    for i in range(len(df.columns)):
        summ.append(sum(df[i].values))
        Q1 += np.square((df[i].values)).sum()
        Q2 += (1/(len(df[i].values)))*(np.square((summ[i])).sum())
        Q3 += (1/(len(df[i].values)*(len(df.columns))))*(pow(sum(summ), 2))
    S0 = (Q1-Q2)/((len(df[1].values) - 1)*len(df.columns))
    SA = (Q2 - Q3)/(len(df.columns)-1)
    otnishenue = SA/S0
    print('Odnofakt otnosh:', otnishenue)
    F_fisher = 2.21
    if F_fisher<otnishenue:
        print('Факторы значимые')

    print(otnishenue)

def twoway_analys_preporation(df):
    print('Двофакторный анализ:')
    sl = int(len(df[1].values)/4)
    print(sl)
    dff = []
    for i in range (len(df.columns)):
        dff.append(df[i].values)
    dff1 = []
    dff2 = []
    dff3 = []
    dff4 = []
    dffn = [dff1, dff2, dff3, dff4]
    for j in range(len(df.columns)):
        dff1.append(dff[j][:sl])
        dff2.append(dff[j][sl:(2 * sl)])
        dff3.append(dff[j][(2 * sl):(3 * sl)])
        dff4.append(dff[j][(3 * sl):(4 * sl)])
    a = []
    for i in range(len(dffn)):
        b = [np.mean(dffn[i][j]) for j in range(len(dffn[i]))]
        a.append(b)
    names = [0, 1, 2, 3]
    zipped = list(zip(names, a))
    data = dict(zipped)
    stats_t = pd.DataFrame(data)
    stats = stats_t.transpose()
    return stats

def twowayoriginal(df):
    dff = twoway_analys_preporation(df)
    a = []
    b = []
    for i in range(len(dff.columns)):
        a.append(sum(dff[i].values))
    for i in range(len(dff[0].values)):
        b.append(sum(dff.loc[i, :]))
    print('\nСумма по столбцам: {}'.format(sum(a)))
    print('Сумма по рядкам: {}'.format(sum(b)))
    q1 = np.sum(dff.values ** 2)
    q2 = np.sum(np.array(a)**2) / len(dff[0])
    q3 = np.sum(np.array(b)**2) / len(dff.loc[0, :])
    q4 = (np.sum(np.array([a])) ** 2) * (1 / (len(dff[0]) * len(dff.loc[0, :])))
    q5 = np.sum(df.values ** 2)
    #print(q1, q2, q3, q4, q5)
    s02 = (q1 + q4 - q2 - q3) / (5*3)
    sa2 = (q2 - q4) / 3
    sb2 = (q3 - q4) / 5
    sab2 = (q5 - q1*6) / (5*6*4)
    s1 = sa2 / s02
    s2 = sb2 / s02
    s3 = 6 * s02 / sab2
    f_3_15 = 3.29
    f_5_15 = 2.90
    f_3_120 = 3.87
    if s1 < f_3_15:
        print('Первый фактор не значимый')
    else:
        print('Первый фактор значимый')
    if s2 < f_5_15:
        print('Второй фактор не значимый')
    else:
        print('Второй фактор значимый')
    if s3 < f_3_120:
        print('Влияние двух факторов не значимое')
    else:
        print('Влияние двух факторов значимое')














if __name__ == '__main__':
    a = pd.read_csv('kpi3.txt', sep='\s+', header=None)
    df = a.loc[:, a.columns != 0]
    df.columns = [i for i in range(6)]
    dispersion(df)
    Qevaluate(df)
    #twoway_analys_preporation(df)
    twowayoriginal(df)
