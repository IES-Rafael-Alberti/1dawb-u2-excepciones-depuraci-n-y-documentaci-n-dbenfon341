import pytest
from src.Ejercicio_2_3_5 import verificar_pwd

@pytest.mark.parametrize(
    "pwd_ingresada, expected",
    [
        ("meloinvento1122", "Contraseña correcta!!")
    ]
)
def test_verificar_pwd_params(pwd_ingresada, expected):
    assert verificar_pwd(pwd_ingresada) == expected


def test_pwd_ingresada_NameError():
    with pytest.raises(NameError):
        verificar_pwd("gfdsgfdsfg")