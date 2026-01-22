#lezione 1: Testing Perteghella
#     TDD  -> refactoring -> write a failing test -> make the test pass ->...
# ancora prima di scrivere codice fai in modo che fallisca


# OPERAZIONE SOMMA
def somma(a:float, b:float):
    if not isinstance(a, (int, float)):
        return "A Not a number"

    if not isinstance(b, (int, float)):
        return "B Not a number"
    return a + b


# OPERAZIONE SOTTRAZIONE
def sottrazione(a:float, b:float):
    if not isinstance(a, (int, float)):
        return "A Not a number"

    if not isinstance(b, (int, float)):
        return "B Not a number"
    return a - b


# OPERAZIONE MOLTIPLICAZIONE

def moltiplicazione(a:float, b:float):
    if not isinstance(a, (int, float)):
        return "A Not a number"

    if not isinstance(b, (int, float)):
        return "B Not a number"
    return a * b

