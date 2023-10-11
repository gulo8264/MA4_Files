""" MA4_2.py

Student: Gustaf Lofdahl
Mail: gustaf.lofdahl.8462@student.uu.se
Reviewed by:
Date reviewed:
"""

from person import Person
import matplotlib.pyplot as plt
from time import perf_counter as pc

#Numba
from numba import njit

def fib_py(n):
    if n <= 1:
        return n
    else:
        return(fib_py(n-1) + fib_py(n-2))
    
@njit
def fib_numba(n):
    if n<= 1:
        return n
    else:
        return fib_numba(n-1) + fib_numba(n-2)

def comp(q,w,f):
    
    x = range(q,w+1)
    y_c = []
    y_n = []
    y_py = []

    for i in x:
        print(i)
        t1 = pc()
        f = Person(i)
        f.fib()
        t2 = pc()
        fib_numba(i)
        t3 = pc()
        fib_py(i)
        t4 = pc()
        y_c.append(t2-t1)
        y_n.append(t3-t2)
        y_py.append(t4-t3)
    fig, plot=plt.subplots(1)
    plot.plot(x ,y_c, "y", label="C++")
    plot.plot(x, y_n, "g", label="Numba")
    plot.plot(x, y_py, "b", label="py")
    #plt.yscale('log')
    plot.xlabel('n')
    plot.ylabel('Time (s)')
    plot.title('time comparison')
    fig.savefig(str(q) + "to" + str(w) + '.png')

def time47():
    x = 47
    t1 = pc()
    f = Person(x)
    print(f'C++: {f.fib()}')
    t2 = pc()
    print(f'numba: {fib_numba(x)}')
    t3 = pc()
    print(f'C++: {round(t2-t1,4)}')
    print(f'Numba: {round(t3-t2,4)}')

def main():
    comp(20,30,1)
    print('Phase 1')
    time47()
    print('Phase 2')
    comp(30,45,2)
    print('Done')
    

if __name__ == '__main__':
    main()
    
