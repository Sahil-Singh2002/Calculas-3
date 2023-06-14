# Recurrence Formula

## Introduction

Consider the sequence of functions ${F_n(x,y)}$ for ${n \geq 0}$ defined by the recurrence formula:

${ F_0(x,y) = 1}$ ,

${ F_1(x,y) = \frac{x}{2} - y^2 }$

and

${ 2n^2F_{n+1}(x,y) = 2nxyF_n(x,y) - (2n+1)F_{n-1}(x,y)}$ for ${n \geq 1}$.

## CODE

- Recursive Function: `evalFn(n, x, y)`

I have implemented a recursive function `evalFn(n, x, y)` which evaluates the function ${F_n}$ with the arguments $x$ and $y$. The function behaves as follows:
- If $x$ and $y$ are scalars, it returns a float.
- If $x$ and $y$ are both two-dimensional NumPy arrays, it returns a two-dimensional NumPy array.
- If the input arrays have different shapes, it raises a ValueError.

- Symbolic Function: `symbolicFn(n, x, y)`

To study the functions $F_n$ symbolically and obtain explicit expressions, I have written a function `symbolicFn(n, x, y)` using SymPy. It provides an expression for $F_n(x,y)$ as a polynomial in $x$ and $y$ of the form ${ \sum_{i,j} a(i,j)x^iy^j }$. The function has the following behavior:
- It takes a non-negative integer $n$ and symbolic values for $x$ and $y$ as input.
- It outputs a polynomial in $x$ and $y$ of the type `sympy.Poly` with the ${ \mathbf{D}  \subset \mathbb{Q} }$ .
- If $n$ is not a non-negative integer, it raises a ValueError.
- If $x$ or $y$ are not symbolic expressions (i.e., of type `sympy.core.symbol.Symbol`), it raises a ValueError.

- Integration and Differentiation: Functions `S(x)`, `D(x, n)`, and `T(a)`

Now, let's consider the function ${ G(x, y) = 1 + (xy)^2 }$. Using SymPy, I have implemented the following functions:
- `S(x)`: Evaluates the function ${ S(x) }$ given by the integral ${ S(x) = \int_{x^2}^{1} G(x, y) \, dy }$ as a symbolic expression in $x$.
- `D(x, n)`: Computes the $n$-th derivative of $S(x)$ with respect to $x$.
- `T(a)`: Evaluates the integral ${ T(a) = \int_{0}^{a} S(x) \, dx }$ using a sympy.Rational.

Both `S(x)` and `D(x, n)` return polynomials of the type `sympy.Poly` with variable $x$ and domain $sympy.QQ$. The function `T(a)` returns a `sympy.Rational`.

## Conclusion

This file demonstrates how to use the SymPy library to work with recurrence formulas.


