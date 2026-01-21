import pytest
from testingsomma import somma, sottrazione


def test_sottrazione_interi():
    assert sottrazione(5, 3) == 2


def test_sottrazione_float_e_int():
    assert sottrazione(5.5, 2) == 3.5


def test_sottrazione_divisione():
    assert sottrazione(3 / 2.5, 1) == (3 / 2.5) - 1


def test_sottrazione_a_non_numero():
    assert sottrazione("a", 2) == "A is Not a number"


def test_sottrazione_b_non_numero():
    assert sottrazione(3, "+") == "B is Not a number"


#  Test parametrizzato (consigliato)
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5, 3, 2),
        (5.5, 2, 3.5),
        (3 / 2.5, 1, (3 / 2.5) - 1),
        (-3, -2, -1),
    ],
)
def test_sottrazione_parametrizzato(a, b, expected):
    assert sottrazione(a, b) == expected
