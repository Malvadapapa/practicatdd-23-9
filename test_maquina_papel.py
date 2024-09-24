import pytest   
from maquina_papel import *

def test_inicializacion_clase ():
    maquina_x28 = MaquinaPapel('x28', 'Gris')
    assert isinstance(maquina_x28, MaquinaPapel)


def test_atributos():
    maquina_x28 = MaquinaPapel('x28', 'Gris')
    assert maquina_x28.modelo == 'x28'
    assert maquina_x28.color == 'Gris'

def test_rep_str():
    maquina_5 = MaquinaPapel('5', 'rojo')
    string = 'La maquina es el modelo 5 y es de color rojo'
    assert str(maquina_5) == string

def test_getter_modelo():
    maquina_5 = MaquinaPapel('5', 'rojo')
    assert maquina_5.modelo == '5'

def test_setter_modelo():
    maquina_x28 = MaquinaPapel('x28', 'Gris')
    maquina_x28.modelo = '5'
    assert maquina_x28.modelo == '5'