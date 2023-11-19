import pytest
from src.burbuja import algoritmoBurbuja

@pytest.mark.parametrize(
    "lista, expected",
    [
        ([5, 2, 9, 2, 5], [2, 2, 5, 5, 9])
    ]
)
def test_algoritmoBurbuja_params(lista, expected):
    assert algoritmoBurbuja(lista) == expected