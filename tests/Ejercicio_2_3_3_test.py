import pytest
from src.Ejercicio_2_3_3 import introducir_numero, bucle_numero

@pytest.mark.parametrize(
    "num1, expected",
    [
        (10, "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0"),
        (4, "4, 3, 2, 1, 0")
    ]
)
def test_bucle_numero_params(num1, expected):
    assert bucle_numero(num1) == expected


def test_introducir_numero_TypeError():
    with pytest.raises(TypeError):
        introducir_numero("a")