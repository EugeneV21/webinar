from pandas import *
import random
import matplotlib.pyplot as plt
import numpy as np

def is_numeric(s):
	try:
		int(s)
		return True
	except (ValueError, TypeError):
		return False

def delete(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n

def lab_8_var_7_1():
    df = read_csv("C:\lab8\DailySmokers.csv",",", header=1)
    locations = np.unique(df['LOCATION']) 
    n = input("Введите число стран для выборки: ")
    if is_numeric(n):
        n = int(n)
        if (n>0):
            if (n<=44):  
                loc = []
                while (len(loc)<n):
                    a = random.randint(0, 43)
                    loc.append(locations[a])
                    loc = delete(loc)
                df.drop(['INDICATOR', 'MEASURE', 'FREQUENCY', 'Flag Codes'], axis='columns', inplace=True)
                for i in range(len(loc)):
                    df1 = df[df['LOCATION'] == loc[i]]
                    subjects = np.unique(df1['SUBJECT'])
                    fig, ax = plt.subplots(len(subjects), 1, figsize =(16,8))
                    label = str('Результат измерений для страны '+str(loc[i]))
                    for j in range(len(subjects)):
                        df2 = df1[df1['SUBJECT'] == subjects[j]]
                        time = df2['TIME']
                        values = df2['Value']
                        plot = plt.figure()
                        ax[j].plot(time,values,label='Число измерений', color=np.random.rand(3,))
                        ax[j].set_ylabel(str(subjects[j]))
                        ax[j].legend()
                    ax[0].set_title(label)
                    ax[-1].set_xlabel('Год')
            else:
                print("Число стран должно быть не больше 44, но больше нуля")
        else:
            print("Число стран должно быть целым положительным числом не больше 44")
    else:
        print("Необходимо ввести целое число стран от 1 до 44")

def lab_8_var_7_2():
    df = read_csv("C:\lab8\DailySmokers.csv",",", header=1)
    loc = np.unique(df['LOCATION'])
    dict = {'LOCATION':[], 'MEAN':[], 'SD':[]}
    data = DataFrame(dict)
    for i in range(len(loc)):
        df1 = df[df['LOCATION'] == loc[i]]
        mean = df1['Value'].mean()
        sd = df1['Value'].std()
        data.loc[i] = [loc[i], mean, sd]
    data.to_csv("C:\lab8\Data.csv",sep=",")
lab_8_var_7_2()