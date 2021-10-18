"""
@completion: October 12, 2020
@author: Rui Min
@topic: Bisection method to find an approximate solution
"""

from math import *

# the math function is defined here and can be changed
def f(x):
    return x**5-x**3+3*x-5


# Main function of the method
def bisection(a, b, N):
    if f(a)*f(b) >= 0:
        print("Bisection method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(0, N):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Bisection method fails.")
            return None
        print(m_n)
    return a_n, b_n


# main entry point of the program
if __name__ == "__main__":
    a = float(input("input left interval boundary: "))
    b = float(input("input right interval boundary: "))
    if a >= b:
        print("invalid input")
        pass
    else:
        '''Be careful here err is better to choose <=0.01; <=0.001; <=0.0001; ...
        to confirm exact decimal places of 0.1; 0.01; 0.001; ...
        In fact, no actual smallest err to ensure length of decimal positions
        (due to .xxx49999 vs. .xxx50000)'''
        err = float(input("input acceptable difference from exact value: "))
        
        '''this is derived from |x(true)-x(N)| <= (b-a)/2^(N) <= err
        Here 2^(N), because bisection() will return m_n !! 
        If returned (a_n + b_n)/2, then here should be 2^(N+1) and N should minus 1!'''
        N = ceil((log((b-a)/err)) / log(2))
        result = bisection(a, b, N)
        print(result)
        input()