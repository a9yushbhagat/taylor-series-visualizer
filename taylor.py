import check
import math
import matplotlib.pyplot as plt


'''
Works with exp, sin, and cos functions
'''


def factorial(n):
    '''
    Returns n!, the product of all integers from 1 to n
    (or 1 if n is 0).

    factorial: Nat -> Nat

    Examples:
       factorial(0) => 1
       factorial(4) => 24
    '''
    if n == 0:
        return 1
    acc = 1
    p = 1
    while p <= n:
        acc *= p
        p += 1
    return acc


def taylor_coefficient(name, k):
    '''
    Returns the kth Taylor coefficient of the function named name,
    centered at 0.

    taylor_coefficient: Str Nat -> Float
    Requires: name is one of "exp", "sin", "cos"

    Examples:
       taylor_coefficient("exp", 2) => 0.5
       taylor_coefficient("sin", 0) => 0
       taylor_coefficient("cos", 2) => -0.5
    '''
    if name == "exp":
        c_k = 1 / factorial(k)
        return c_k
    elif name == "sin":
        if k % 2 == 0:
            return 0
        elif which_odd(k, 0):
            return 1 / factorial(k)
        else:
            return -1 / factorial(k)
    else:                             # "cos"
        if k % 2 == 1:
            return 0
        elif k % 4 == 0:
            return 1 / factorial(k)
        else:
            return -1 / factorial(k)

        
def which_odd(n, m):
    '''
    Returns True if n is of the form 4*j + 1 for some integer
    j >= m, and False otherwise.

    which_odd: Nat Nat -> Bool
    '''
    while m <= n:
        if (4 * m) + 1 == n:
            return True
        m += 1
    return False


def taylor_poly(name, n, x):
    '''
    Returns the value at x of the degree-n Taylor polynomial of
    the function named name, centered at 0.

    taylor_poly: Str Nat Float -> Float
    Requires: name is one of "exp", "sin", "cos"

    Examples:
       taylor_poly("exp", 4, 1) => 2.708333333333333
       taylor_poly("cos", 2, 0) => 1.0
    '''
    return find_sum_der(name, 0, n, x)


def find_sum_der(o, k, p, m): # k starts with 0 upto p
    '''
    Returns the sum of the Taylor terms of the function named o
    from degree k up to degree p, evaluated at m.

    find_sum_der: Str Nat Nat Float -> Float
    Requires: o is one of "exp", "sin", "cos"
              k <= p
    '''
    acc = 0
    while k <= p:
        acc += taylor_coefficient(o, k) * (m ** k)
        k += 1
    return acc


def exact_value(name, x):
    '''
    Returns the exact value at x of the function named name.

    exact_value: Str Float -> Float
    Requires: name is one of "exp", "sin", "cos"

    Examples:
       exact_value("exp", 1) => 2.718281828459045
       exact_value("cos", 0) => 1.0
    '''
    if name == "exp":
        return math.exp(x)
    elif name == "sin":
        return math.sin(x)
    else:
        return math.cos(x)
    

def error(name, n, x):
    '''
    Returns the absolute difference at x between the exact value of
    the function named name and its degree-n Taylor polynomial.

    error: Str Nat Float -> Float
    Requires: name is one of "exp", "sin", "cos"

    Examples:
       error("exp", 4, 1) => 0.009948495125712054
       error("cos", 2, 0) => 0.0
    '''
    error = abs(exact_value(name, x) - taylor_poly(name, n, x))
    return error


def poly_string(name, n):
    '''
    Returns a string showing the degree-n Taylor polynomial of the
    function named name, with zero terms omitted and coefficients
    rounded to 4 decimal places.

    poly_string: Str Nat -> Str
    Requires: name is one of "exp", "sin", "cos"

    Examples:
       poly_string("exp", 4)
          => "1.0x^0 + 1.0x^1 + 0.5x^2 + 0.1667x^3 + 0.0417x^4"
       poly_string("cos", 4)
          => "1.0x^0 + -0.5x^2 + 0.0417x^4"
    '''
    acc = "" 
    p = 0
    while p <= n:
        c =  taylor_coefficient(name, p)
        if c == 0:
            p += 1
        else:
            acc += str(round(c, 4)) + "x^" + str(p)  + " + " 
            p += 1
    return acc[:-3]


def visualize(name, degrees, left, right):
    '''
    Returns None.

    Effects: Displays a plot of the function named name together
             with its Taylor polynomial for each degree in degrees,
             over the interval from left to right

    visualize: Str (listof Nat) Float Float -> None
    Requires: name is one of "exp", "sin", "cos"
              left < right

    Examples:
       visualize("exp", [1, 3, 5, 7], -3, 3) => None
       and displays the plot
    '''
    xs = []
    p = left
    while p <= right:
        xs.append(p)
        p = p + 0.05
    ys = list(map(lambda x: exact_value(name, x), xs))
    plt.plot(xs, ys, label=name)
    for n in degrees:
        approx = list(map(lambda x: taylor_poly(name, n, x), xs))
        plt.plot(xs, approx, label="Degree " + str(n))
    plt.legend()
    plt.title("Taylor Approximations of " + name + " at x = 0")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.ylim(-2, 18)
    plt.show()


## Tests:
check.expect("T1: factorial 0", factorial(0), 1)
check.expect("T2: factorial 4", factorial(4), 24)
check.within("T3: exp coefficient", taylor_coefficient("exp", 2), 0.5, 0.0001)
check.expect("T4: sin even coefficient", taylor_coefficient("sin", 0), 0)
check.within("T5: cos coefficient", taylor_coefficient("cos", 2), -0.5, 0.0001)
check.within("T6: taylor poly", taylor_poly("exp", 4, 1), 2.70833, 0.0001)
check.within("T7: exact value", exact_value("exp", 1), 2.71828, 0.0001)
check.within("T8: error", error("exp", 4, 1), 0.00995, 0.0001)
check.expect("T9: poly string cos", poly_string("cos", 4),
             "1.0x^0 + -0.5x^2 + 0.0417x^4")

visualize("exp", [1, 3, 5, 7], -3, 3)