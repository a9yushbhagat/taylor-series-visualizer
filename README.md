# Taylor Series Visualizer

A Python project that computes Taylor polynomial approximations for `exp`, `sin`, and `cos`, compares them with the exact functions, measures approximation error, and visualizes how the approximation improves as the polynomial degree increases.

## Project Overview

The project builds Taylor polynomial approximations centered at 0 for three functions:

- exponential function `exp(x)`
- sine function `sin(x)`
- cosine function `cos(x)`

The program calculates the coefficients of the Taylor series, evaluates the polynomial at a chosen value of `x`, compares the approximation with the exact function value, and calculates the absolute error.

It can also plot several Taylor polynomial approximations together with the original function.

## Features

- Calculates factorial values
- Computes Taylor coefficients
- Builds Taylor polynomial approximations
- Evaluates approximations at chosen values
- Calculates exact function values
- Measures approximation error
- Creates readable polynomial expressions
- Visualizes multiple polynomial degrees
- Supports `exp`, `sin`, and `cos`

## Main File

- `taylor_series.py` — contains the Taylor coefficient calculations, polynomial evaluation, error calculations, tests, and visualization

## Core Mathematics

A Taylor polynomial centered at 0 can be written as:

**P_n(x) = a_0 + a_1x + a_2x^2 + ... + a_nx^n**

The coefficients depend on the derivatives of the function.

For example, the exponential function has the series:

**e^x = 1 + x + x^2/2! + x^3/3! + ...**

The program calculates these coefficients and uses them to construct the approximation.

## Approximation Error

The program compares the Taylor polynomial with the exact function value using:

**Error = |Exact Value - Taylor Approximation|**

This makes it possible to study how the approximation improves as the polynomial degree increases.

## Example

For the exponential function at:

**x = 1**

a degree-4 Taylor approximation gives approximately:

**2.70833**

while the exact value of `e` is approximately:

**2.71828**

The error is therefore approximately:

**0.00995**

## Visualization

The program can plot:

- the original function
- several Taylor polynomial approximations
- different polynomial degrees on the same graph

This makes it easier to see how higher-degree Taylor polynomials more closely follow the original function.

## Technologies and Concepts

- Python
- Python 3
- Calculus
- Taylor series
- Polynomial approximation
- Factorials
- Numerical approximation
- Error analysis
- Matplotlib

## Status

**Completed**

This project was created to connect Taylor series calculations with numerical approximation and visualization.
