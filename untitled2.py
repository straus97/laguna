import numpy as np
from scipy.stats import expon
from math import log, ceil
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'fantasy'
rcParams['font.fantasy'] = 'Times New Roman'
#генератор случайных чисел для эрланговского закона распределения
def generate(lambd):
    r = np.random.exponential(1/lambd)
    return(r)
A_list= [] #выборка элементов
x_min = 0 #минимальный элемент выборки A_list
x_max = 0 #максимальный элемент выбории A_list
delta = 0 #дельта выборки A_list
N = 0 #количество элементов в выборке A_list
number_i = [0]*10 #интервалы
M_list =[] #список для хранения значений МО
D_test_list = []  
D_list = [] #список для хранения значений дисперсии
#заданные параметры для эрланговского распределения

lambd = 4
#пока минимальное количество элементов не будет равно 100 , выполняй:
while min(number_i) < 100: 
    print('min=',min(number_i))
    #добавляем в выборку один элемент
    A_list.append(generate(lambd))
    #число элементов в выборке увеличивается
    N = N + 1
    print('A_list[i]=',A_list[N-1])
    #считаем, в какой интервал попало число
    #если последнее добавленное число в выборке находится за пределами значений,
    #которые находятся в выборке, то:
    if (A_list[N-1] < x_min or A_list[N-1] > x_max) and (x_max == x_min):   
            #A_list_new=A_list[N-1]
            #считаем вероятность попадания СВ за границы интервала
            probability = (N - sum(number_i))/ N
            print('probability =',probability)
            #если вероятность >= заданного значений,то:
            if probability >= 0.01:
                #пересчитываем минмальный элемент выборки
                x_min = min(A_list)
                #пересчитываем максимальный элемент выборки
                x_max = max(A_list)
                #пересчитываем дельта
                delta = (x_max - x_min)/10
#пересчитать N[i], очищая сначала весь список с количеством элементов
                number_i = [0]*10
                #если дельта == 0 
                if delta == 0:  
           #в нулевом интервале становится на один элемент больше,
                    #т.е. значение новой попало в нулевой интервал
                    number_i[0] = number_i[0] + 1
                #иначе, рассчитываем номер интервала по формуле:
                else:
                    #берем все элементы из выборки
                    for c in range(len(A_list)):
                        #отнимаем 1, так как счет в python идет с 0
                        j = ceil((A_list[c] - x_min)/delta) - 1
                        #если номер интервала меньше 0, то значение попало в нулевой интервал          
                        if j == -1: 
                            j = 0
                        number_i[j] = number_i[j] + 1
    #если новый элемент выборки попадает в диапазон xmin,xmax, то:
    else:        
        #считаем номер интервала, куда попало значение
        #единицу вычитаем, так как счет в python идет с 0
        i = ceil((A_list[N-1] - x_min)/delta) - 1
        if i == -1: 
            i = 0
        #если номер интервала от 0 до 9 (так как у нас всего 10 интервалов)          
        if i >=0 and i<=9:
            print('i=',i)
            #добавляем элемент в определенный номер интервала
            number_i[i] = number_i[i] + 1
            #рассчитываем верояность попадания вне интервала
        probability = (N - sum(number_i))/ N
        print('probability =',probability)
        #если вероятность больше заданного числа, то 
        #пересичтываем мах,мин, дельта, и пересчитываем количество значений, которые попали в интервал
        if probability >= 0.01:
            x_min = min(A_list)
            x_max = max(A_list)
            delta = (x_max - x_min)/10
            #пересчитать N[i]
            number_i = [0]*10
            for y in range(len(A_list)):
                l = ceil((A_list[y] - x_min)/delta) - 1
                if l == -1:   
                    l = 0   
                number_i[l] = number_i[l] + 1
    M = sum(A_list)/N
    M_list.append(M)
    D = (A_list[N-1]-M)**2
    D_test_list.append(D)
    D_list.append(sum(D_test_list)/ (N))   
M_teor = pow(lambd,-1)    
D_teor = pow(lambd,-2)


#рассчитываем вектор Y
Y = []                             
for r in range(len(number_i)):
    Y.append(number_i[r]/(sum(number_i)*delta)) 
         
q = np.arange(0,10,0.001)  

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(q,expon.pdf(q,scale=1/lambd),'g')
ax.set_title('Гистограмма',fontsize=14)
delt = (x_max-x_min)/10
x = np.arange(x_min,x_max, delt)
plt.bar(x,Y,delta)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
#ax1.set_ylim([-0.5,0.5])
ax1.set_title('Оценка математического ожидания',fontsize=14)
ax1.set_xlabel('объем выборки',fontsize =10)
ax1.set_ylabel('МО ',fontsize=10) 
ax1.plot(range(N),M_list,label = u'экспериментальное значение МО')
ax1.plot(range(N),[M_teor]*N,label = u'теоретическое значение МО',ls = 'dashed')
ax1.legend(loc='best', frameon = True)
plt.legend()

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.set_title('Оценка дисперсии',fontsize=14)
ax2.set_xlabel('объем выборки',fontsize =10)
ax2.set_ylabel('D ',fontsize=10) 
ax2.plot(range(N),[D_teor]*N,label = u'теоретическое значение D',ls = 'dashed')
ax2.plot(range(N),D_list,label = u'экспериментальное значение D')
ax2.legend(loc='best', frameon = True)
plt.legend()
