import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

import app

def test_add():
    assert app.add(5, 6) == 11

def test_add2():
    assert app.add(5, 6) != 10

def test_subtract():
    assert app.subtract(5, 6) == -1

def test_subtract2():
    assert app.subtract(5, 6) != 11

def test_multiply():
    assert app.multiply(5, 6) == 30

def test_multiply2():
    assert app.multiply(5, 6) != 11

def test_multiply_by_zero():
    assert app.multiply(5, 0) == 0

def test_divide():
    assert app.divide(30, 5) == 6

def test_divide2():
    assert app.divide(30, 5) != 5

def test_divide_by_zero():
    try:
        app.divide(5, 0)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."

def test_log():
    assert app.log(25, 5) == 2

def test_log2():
    assert app.log(25, 5) != 11

def test_log_invalid_argument():
    try:
        app.log(-25, 5)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Logarithm argument must be positive."

def test_log_invalid_base_1():
    try:
        app.log(25, 1)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Logarithm base must be positive and not equal to 1."

def test_log_invalid_base_negative():
    try:
        app.log(25, -5)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Logarithm base must be positive and not equal to 1."

def test_square():
    assert app.square(5) == 25

def test_square2():
    assert app.square(5) != 30

def test_sin():
    assert app.sin(0) == 0

def test_sin2():
    assert app.sin(0) != 1

def test_cos():
    assert app.cos(0) == 1

def test_cos2():
    assert app.cos(0) != 0

def test_square_root():
    assert app.square_root(25) == 5

def test_square_root2():
    assert app.square_root(25) != 6

def test_square_root_negative():
    try:
        app.square_root(-25)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Cannot take square root of negative number."

def test_percent():
    assert app.percent(6, 30) == 20

def test_percent2():
    assert app.percent(5, 30) != 20

def test_percent_divide_by_zero():
    try:
        app.percent(5, 0)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Cannot calculate percentage with a denominator of zero."