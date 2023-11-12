import pytest
from src.Ejercicio_2_3_2 import bucle_numero

@pytest.mark.parametrize(
    "numero, expected",
    [
        (10, "1, 3, 5, 7, 9"),
        (15, "1, 3, 5, 7, 9, 11, 13, 15"),
        (5, "1, 3, 5")
    ]
)
def test_bucle_numero_params(numero, expected):
    assert bucle_numero(numero) == expected