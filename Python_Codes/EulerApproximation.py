"""
@completion: April 17, 2021
@author: Rui Min
@topic: Euler's method to find a approximate solution of differential equation(s)
"""
# Euler's method to find a approximate solution of differential equation(s)

# the math function is defined here
def fPrime_t(t, y,a=2,b=1,k=0.5):
    # The funciton in next line can be changed
    return k*(a-y)*((b-y)**0.5)     # no relationship with parameter - t;


# Main function of the method
def eulermethod(steps, initial=0, end=1, y0=0):
    size = (end - initial)/steps
    t = []
    t.append(initial)
    fPrimelist = []
    fPrimelist.append(fPrime_t(t, y0))
    ylist = []
    ylist.append(y0)
    for i in range(1, steps+1):
        t.append(t[i-1]+size)       # t value at i'th step
        ylist.append(ylist[i-1] + size*fPrimelist[i-1])    # Euler's Method
        fPrimelist.append(fPrime_t(t[i], ylist[i]))

    # print (t, "\n", ylist,"\n", fPrimelist)
    return ylist[steps]


# main entry point of the program & check if this is the main
if __name__ == "__main__":
    # a = float(input("input initial concentration of hydrogen(mol/L): "))
    # b = float(input("input initial concentration of bromine(mol/L): "))
    # y0 = float(input("input initial concentration of HBr(mol/L): "))
    # k = float(input("input rate proportional to growth: "))
    # assert a>=0 and b>=0 and x0>=0 and k>=0
    # t = float(input("input end time t: "))
 
    steps = int(input("input the number of steps n: "))
    assert steps > 0, "illegal input of steps n, please restart the program"

    result = eulermethod(steps)
    print(result)
    input()
