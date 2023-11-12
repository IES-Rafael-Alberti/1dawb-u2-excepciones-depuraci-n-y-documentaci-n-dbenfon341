import pytest
from src.Ejercicio_2_3_4 import pedirNumero

def test_pedirNumero_ValueError():
    with pytest.raises(ValueError):
        pedirNumero("a")