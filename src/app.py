import math

def add (a, b):
    return a+b

def subtract (a, b):
    return a-b

def multiply (a, b):
    return a * b

def divide (a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def log (a, b):
    if a <= 0:
        raise ValueError("Logarithm argument must be positive.")
    if b <= 0 or b == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1.")
    return math.log(a, b)

def square (a):
    return a ** 2

def sin (a):
    return math.sin(a)

def cos (a):
    return math.cos(a)

def square_root (a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number.")
    return a ** 0.5

def percent (a, b):
    if b == 0:
        raise ValueError("Cannot calculate percentage with a denominator of zero.")
    return (a / b) * 100


