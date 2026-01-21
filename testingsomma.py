#lezione 1: Testing Perteghella
#     TDD  -> refactoring -> write a failing test -> make the test pass ->...
# ancora prima di scrivere codice fai in modo che fallisca

def somma(a:float, b:float):
    if not isinstance(a, (int, float)):
        return "A Not a number"

    if not isinstance(b, (int, float)):
        return "B Not a number"
    return a + b

def sottrazione(a:float, b:float):
    if not isinstance(a, (int, float)):
        return "A Not a number"

    if not isinstance(b, (int, float)):
        return "B Not a number"
    return a + b

