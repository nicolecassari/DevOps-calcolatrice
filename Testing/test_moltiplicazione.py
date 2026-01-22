import pytest
from operazioni import moltiplicazione


def test_moltiplicazione_interi():
    assert moltiplicazione(-3, 2) == -6


def test_moltiplicazione_float_e_int():
    assert moltiplicazione(2.5, 2) == 5.0


def test_moltiplicazione_divisione():
    assert moltiplicazione(3 / 2.5, 2) == (3 / 2.5) * 2


#def test_moltiplicazione_a_non_numero():
 #   assert moltiplicazione("a", 2.5) == "A is Not a number"


#def test_moltiplicazione_b_non_numero():
 #   assert moltiplicazione(3, "+") == "B is Not a number"

