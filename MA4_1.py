""" MA4_1.py

Student: Gustaf Lofdahl
Mail: gustaf.lofdahl.8462@student.uu.se
Reviewed by:
Date reviewed:
"""

import random
import math
import matplotlib.pyplot as plt
import concurrent.futures as future
from time import perf_counter as pc


def piApp(n):

    nC = 0
    xIn = []
    yIn = []
    xOut = []
    yOut = []
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if (pow(x,2) + pow(y,2)) <= 1:
            nC += 1
            xIn.append(x)
            yIn.append(y)
        else:
            xOut.append(x)
            yOut.append(y)
    fig, plot=plt.subplots(1)
    plot.set_aspect('equal')
    plot.scatter(xIn, yIn, c='r')
    plot.scatter(xOut, yOut, c='b')
    fig.savefig("piApprox_"+str(n)+".png")
    piApp = 4*nC/n
    return piApp, nC
    

def MonteCarlo(n, d):
    V = pow(math.pi, d/2)/math.gamma(d/2+1)
    point = lambda x : pow(x,2)
    points = [[point(random.uniform(-1,1)) for ii in range(d)] for jj in range(n)]
    points_sum = list(map(sum, points))
    nV = 0
    for i in range(len(points_sum)):
        if points_sum[i] <= 1:
            nV += 1
    V_App = (nV/n)*2**d
    return V_App 


def MultiMonteCarlo(n, d, p):
    n = [int(n/p)]*p
    d = [d]*p
    with future.ProcessPoolExecutor() as ex:
        result = ex.map(MonteCarlo, n, d)
    result = sum(result)/p
    return result


def main():
    print("Python value of pi = "+str(math.pi))
    tests = [1000, 10000, 100000]
    for i in range(len(tests)):
        print("Approximation of pi, n = "+str(tests[i])+" is: "+str(piApp(tests[i])[0])+" with "+str(piApp(tests[i])[1])+" points inside ")
    

    print("Theoretical Volume:         "+str(pow(math.pi, 11/2)/math.gamma(11/2+1)))
    start_time = pc()
    #MonteCarlo(10000000, 11)
    print("Serial Estimated Volume:    "+str(MonteCarlo(10000000, 11)))
    end_time = pc()
    time = end_time - start_time
    

    start_time2 = pc()
    print("Parallell Estimated Volume: "+str(MultiMonteCarlo(10000000, 11, 10)))
    #MultiMonteCarlo(10000000, 11, 10)
    end_time2 = pc()
    time2 = end_time2 - start_time2
    

    print("Serialprosessing took: "+str(time)+"s")
    print("Multiprossesing took:  "+str(time2)+"s")


if __name__ == '__main__':
	main()


"""
Python value of pi = 3.141592653589793
Approximation of pi, n = 1000   is: 3.124   with 799   points inside 
Approximation of pi, n = 10000  is: 3.1616  with 7845  points inside 
Approximation of pi, n = 100000 is: 3.13436 with 78478 points inside 
Theoretical Volume:         1.8841038793898994
Serial Estimated Volume:    1.9073024
Parallell Estimated Volume: 1.910784
Serialprosessing took: 99.99009559300612s
Multiprossesing took:  30.176946916995803s
"""