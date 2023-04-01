# Calculas 3

**Introduction**

Consider the sequence of functions Fn(x,y) for (n≥0) defined by the recurrence formula F0(x,y)=1,F1(x,y)=x/2−y^2 and 2n^(2)Fn+1(x,y)=2nxyFn(x,y)−(2n+1)Fn−1(x,y),n≥1.

**CODE**

* I wrote a recursive function `evalFn(n,x,y)` which evaluates the function Fn with the arguments x and y. The function should return a float if *x* and *y* are scalars. If the input *x* and *y* are both two-dimensional NumPy arrays then the output should also be a two-dimensional NumPy array. If the input are numpy arrays of different shapes it should raise a ValueError.
* In addition to working numerically we can also use SymPy to study the functions Fn symbolically and obtain explicit expressions. Use `SymPy` to write a function symbolicFn(n,x,y) which gives an expression for Fn(x,y) as a polynomial in *x* and *y* of the form ∑_(i,j) a(i,j)x^iy^j. The function should take a non-negative integer n and symbolic values for *x* and *y* as input and output a polynomial in *x* and *y* of the type `sympy.Poly` with domain the rational numbers.
  - If n is not a non-negative integer the function should raise a ValueError.
  - If *x* or *y* are not symbolic expressions (i.e. of type `sympy.core.symbol.Symbol`) then a ValueError should be raised.
* Now Consider the following function of two variables: G(x,y)=1+(xy)^2. Using SymPy for the following:
  - Write a function `S(x)` with a parameter *x* to evaluate the function S(x) given by the following integral: S(x)=∫G(x,y)dy in the interval of x^2 to 1 as a symbolic expression in *x*.
  - Then a function `D(x,n)` which takes as arguments a symbol *x* and an integer *n* to evaluate the *n*-th derivative of **S(x)** with respect to *x*.
  - Finally a function `T(a)` with one argument a given by a sympy.Rational to evaluate the integeral T(a)=∫S(x)dx in the interval of 0 to a.
    - The functions **S(x)** and **D(x,n)** should both return polynomials of the type `sympy.Poly`, variable *x* and domain `sympy.QQ`.
    - The function **T(a)** should return a sympy.Rational.
    
**Conclusion**

This file shows how to use the library sympy to express recurrence formula, expressing a recurrence fomula in a symbolic expressions and integral of a function and even surface integral.
  

