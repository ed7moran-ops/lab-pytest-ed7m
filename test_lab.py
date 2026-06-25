from calculadora import sumar, restar, multiplicar
from regla import es_mayor_de_edad

def test_sumar():
    assert sumar(5, 3) == 8

def test_restar():
    assert restar(10, 4) == 6

def test_multiplicar():
    assert multiplicar(3, 4) == 12

def test_es_mayor_de_edad():
    assert es_mayor_de_edad(18) == True
