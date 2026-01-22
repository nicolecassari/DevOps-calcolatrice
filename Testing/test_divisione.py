
import pytest
from operazioni import divisione


def test_divisione_interi():
    assert divisione(-3, 2) == -1


def test_divisione_float_e_int():
    assert divisione(2.5, 2) == 4.5


#def test_divisione_divisione():
 #   assert divisione(3 / 2.5, 1) == (3 / 2.5) + 1
