#lezione 1: Testing Perteghella
#     TDD  -> refactoring -> write a failing test -> make the test pass ->...
# ancora prima di scrivere codice fai in modo che fallisca

from operazioni import somma
from operazioni import sottrazione
from operazioni import moltiplicazione



print(
    "test 1:", somma(-3, 2), "\n",
    "test 2:", somma(2.5, 2), "\n",
    "test 3:", somma(3, 2.5), "\n",
    "test 4:", somma(3, 2.5), "\n",
    "test 5:", somma(3, 2), "\n",
    "test 6:", sottrazione(3, 1), "\n",
    "test 7:", moltiplicazione(3, 1), "\n"
)
