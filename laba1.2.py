import random as rnd
import matplotlib.pyplot as plt

def laba1_2():
    N = 11
    M = 500
    Mass = []
    T_sred = []
    veroyat = 0.005
    
    while veroyat <= (1 / N):    
        Mass.append(veroyat)
        veroyat += 0.005
      
    for i in range(len(Mass)):
        colliz = 0
        all_z = 0
        for j in range(M):
            s1 = []  
            for k in range(N):
                s1.append(rnd.choices([1, 0], weights = [Mass[i], 1-Mass[i]])[0])
            if sum(s1) > 1:
                colliz += sum(s1)
            all_z += sum(s1)
        T_sred.append(colliz / all_z)
    plt.plot(Mass, T_sred, color='red') 
    
laba1_2()