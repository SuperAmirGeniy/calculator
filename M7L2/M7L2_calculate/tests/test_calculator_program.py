import pytest  
from calculate.calculator_program import calculate  

def test_calculate_addition():  
    assert calculate(1, 1, '+') == 2  
    assert calculate(-1, -1, '+') == -2 
    assert calculate(0, 0, '+') == 0 

def test_calculate_subtraction():  
    assert calculate(5, 3, '-') == 2   
    assert calculate(3, 5, '-') == -2 
    assert calculate(0, 5, '-') == -5  

def test_calculate_multiplication():  
    assert calculate(3, 4, '*') == 12
    assert calculate(0, 5, '*') == 0   
    assert calculate(-2, 3, '*') == -6 

def test_calculate_division():  
    assert calculate(8, 2, '/') == 4    
    assert calculate(5, 0, '/') == "На ноль делить нельзя."    
    assert calculate(10, 5, '/') == 2  

def test_calculate_unknown_operation():  
    assert calculate(5, 5, 'unknown') == "Неизвестная операция."

