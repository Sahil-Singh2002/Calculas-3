import numpy as np
import sympy

def evalFn(n, x, y):
    if not isinstance(x, (int, np.ndarray)) or not isinstance(y, (int, np.ndarray)):
        raise ValueError("x and y must be integers or NumPy arrays.")
    if isinstance(x, np.ndarray) and isinstance(y, np.ndarray):
        if x.shape != y.shape:
            raise ValueError("x and y must have the same shape.")
    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    if n == 0:
        return np.ones_like(x) if isinstance(x, np.ndarray) else 1
    elif n == 1:
        return (x / 2) - (y ** 2)

    return ((2 * (n - 1) * x * y * evalFn(n - 1, x, y)) - ((2 * (n - 1) + 1) * evalFn(n - 2, x, y))) / (2 * ((n - 1) ** 2))

def symbolicFn(n, x, y):
    if not isinstance(x, sympy.Symbol) or not isinstance(y, sympy.Symbol):
        raise ValueError("x and y must be symbolic expressions.")
    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    if n == 0:
        return sympy.Poly(1, x, y, domain=sympy.QQ)
    elif n == 1:
        return sympy.Poly((x / 2) - (y ** 2), x, y, domain=sympy.QQ)

    return sympy.Poly(((2 * (n - 1) * x * y * symbolicFn(n - 1, x, y)) - ((2 * (n - 1) + 1) * symbolicFn(n - 2, x, y)))
                      / (2 * ((n - 1) ** 2)), x, y, domain=sympy.QQ)

def S(x):
    y = sympy.symbols('y')
    z = 1 + (x * y) ** 2
    S = sympy.integrate(z, (y, x ** 2, 1))
    return S.as_poly()

def D(x, n):
    d_x = S(x)
    for loop in range(n):
        d_x = sympy.diff(d_x, x)
    return d_x.as_poly()

def T(a):
    x = sympy.symbols('x')
    s = S(x).as_expr()
    T = sympy.integrate(s, (x, 0, a))
    return sympy.Rational(T)
