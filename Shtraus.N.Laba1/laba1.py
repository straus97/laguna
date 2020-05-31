import random as rnd
import matplotlib.pyplot as plt

def laba1():
    N = 11
    M = 10000
    Mass = []
    T_sred = []
    veroyat = 0
    
    while veroyat <= (1 / N):    
        Mass.append(veroyat)
        veroyat += 0.01
      
    for i in range(len(Mass)):
        R = []
        for j in range(M):
            s1 = []  
            for k in range(N):
                s1.append(rnd.choices([1, 0], weights = [Mass[i], 1-Mass[i]])[0])
            sum_s1 = sum(s1)
            if len(R) == 0:
                R.append(0)
            elif R[j-1] <= 0 :
                R.append(sum_s1)
            else:
                R.append(R[j-1] - 1 + sum_s1)
        if Mass[i] == 0:
            T_sred.append(0)
        else:
            T_sred.append(sum(R) / Mass[i])
    
    plt.plot(Mass, T_sred, color='red')
    
laba1()
