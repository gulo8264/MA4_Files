""" MA4_2.py

Student: Gustaf Lofdahl
Mail: gustaf.lofdahl.8462@student.uu.se
Reviewed by: Ema Duljkovic
Date reviewed: 12/10 -23
"""

from person import Person
import matplotlib.pyplot as plt
from time import perf_counter as pc

#Numba
from numba import njit

def fib_p(n):
    if n <= 1:
        return n
    else:
        return(fib_p(n-1) + fib_p(n-2))
    
@njit
def fib_n(n):
    if n<= 1:
        return n
    else:
        return fib_n(n-1) + fib_n(n-2)

def comp(q,w):
    x = 0
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
        fib_n(i)
        t3 = pc()
        fib_p(i)
        t4 = pc()
        y_c.append(t2-t1)
        y_n.append(t3-t2)
        y_py.append(t4-t3)
    plt.plot(x ,y_c, "y", label="C++")
    plt.plot(x, y_n, "g", label="Numba")
    plt.plot(x, y_py, "b", label="py")
    plt.yscale('log')
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.title('time comparison')
    plt.savefig(str(q) + "to" + str(w) + 'log.png')

def time(x):
    t1 = pc()
    f = Person(x)
    print(f'C++: {f.fib()}')
    t2 = pc()
    print(f'Numba: {fib_n(x)}')
    t3 = pc()
    print(f'C++: {round(t2-t1,4)}s')
    print(f'Numba: {round(t3-t2,4)}s')

def main():
    main_start = pc()
    #time(47)
    comp(20,30)
    comp(30,45)
    main_end = pc()
    print('Done')
    print(str(main_end-main_start)+"s")
    

if __name__ == '__main__':
    main()
    
