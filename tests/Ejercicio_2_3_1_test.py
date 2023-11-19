import pytest
from src.Ejercicio_2_3_1 import bucle_edad, introducir_edad

@pytest.mark.parametrize(
    "edad, expected",
    [
        (10, "1 2 3 4 5 6 7 8 9 10"),
        (5, "1 2 3 4 5")
    ]
)
def test_bucle_edad_params(edad, expected):
    assert bucle_edad(edad) == expected


def test_introducir_edad_TypeError():
    with pytest.raises(TypeError):
        introducir_edad("a")