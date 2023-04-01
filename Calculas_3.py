import numpy as np
import sympy
#________________________________________________________________________________
def evalFn(n,x,y):
 #raise value if n<0 and if the data type would be correct.
    if type(x) != int and type(y) != int:
        if x.shape != y.shape:
            raise ValueError
    if n<0:
        raise ValueError
#when n is postive Integer how the function behaves. the conditions are these.    
    elif n == 0:
        return 1 if type(x) == int else np.ones(x.shape)
    elif n == 1:
        return (x/2) - (y**2)
#Below if the function in it self.        
    return ((2*(n-1)*x*y*evalFn(n-1,x,y))-((2*(n-1)+1)*evalFn(n-2,x,y)))/(2*((n-1)**2))

#________________________________________________________________________________
def symbolicFn(n,x,y):
#VALIDATING THE DATA TYPE
    if type(x) != sympy.core.symbol.Symbol and type(y) != sympy.core.symbol.Symbol:
        raise ValueError
    if n<0:
        raise ValueError
#THE INITUAL CONDITION OF THE FUNCTION
    elif n == 0:
        return sympy.Poly(1,x,y,domain=sympy.QQ)
    elif n == 1:
        return ((x/2) - (y**2)).as_poly(domain=sympy.QQ)
#FINISHING THE RECURSION     
    return sympy.Poly(((2*(n-1)*x*y*symbolicFn(n-1,x,y))-((2*(n-1)+1)*symbolicFn(n-2,x,y)))/(2*((n-1)**2)),x,y,domain=sympy.QQ)

#________________________________________________________________________________
def S(x):
    z= 1+(x*y)**2
    S = sympy.integrate(z, (y, x**2, 1))
    return S.as_poly()

def D(x,n):
    d_x = S(x)
    for loop in range(n):
        d_x = sympy.diff(d_x,x)
    return d_x.as_poly()
    
def T(a):
    s= S(x).as_expr()    
    T = sympy.integrate(s, (x, 0, a))
    return sympy.Rational(T)
