import os
import pytest

base_path = "Loop_Exercise"

def test_exercise01():
    assert os.system(f'python "{base_path}/Exercise01 (First 10 natural numbers).py"') == 0

def test_exercise02():
    assert os.system(f'python "{base_path}/Exercise02 (Pattern Printing).py"') == 0

@pytest.mark.skip(reason="Requires user input")
def test_exercise03():
    assert os.system(f'python "{base_path}/Exercise03 (Sum of 1-10).py"') == 0

@pytest.mark.skip(reason="Requires user input")
def test_exercise04():
    assert os.system(f'python "{base_path}/Exercise04 (Multiplication Table).py"') == 0

def test_exercise05():
    assert os.system(f'python "{base_path}/Exercise05 (Display numbers from a list).py"') == 0

@pytest.mark.skip(reason="Requires user input")
def test_exercise06():
    assert os.system(f'python "{base_path}/Exercise06 (Count the total number).py"') == 0

def test_exercise07():
    assert os.system(f'python "{base_path}/Exercise07 (Pattern Printing).py"') == 0

def test_exercise08():
    assert os.system(f'python "{base_path}/Exercise08 (Print list in reverse order ).py"') == 0

def test_exercise09():
    assert os.system(f'python "{base_path}/Exercise09 (Display numbers from -10 to -1).py"') == 0

def test_exercise10():
    assert os.system(f'python "{base_path}/Exercise10.py"') == 0

def test_exercise11():
    assert os.system(f'python "{base_path}/Exercise11 (Print all prime numbers within range).py"') == 0

def test_exercise12():
    assert os.system(f'python "{base_path}/Exercise12 (Fibonacci series up to 10 terms).py"') == 0

def test_exercise13():
    assert os.system(f'python "{base_path}/Exercise13 (Find the factorial of a given number).py"') == 0

def test_exercise14():
    assert os.system(f'python "{base_path}/Exercise14 (Reverse a integer number).py"') == 0

def test_exercise15():
    assert os.system(f'python "{base_path}/Exercise15.py"') == 0

def test_exercise16():
    assert os.system(f'python "{base_path}/Exercise16 (Cube of given numbers).py"') == 0

def test_exercise17():
    assert os.system(f'python "{base_path}/Exercise17 (Sum of series of numbers).py"') == 0

def test_exercise18():
    assert os.system(f'python "{base_path}/Exercise18 (Pattern Printing).py"') == 0

