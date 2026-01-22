from testing import somma, sottrazione


def calcolatrice (operazione: str, a: float,b: float):
    if operazione == "somma":
        return somma (a, b)
    if operazione == "sottrazione":
        return sottrazione (a, b)
    else:
        return None
    
if __name__=="__main__":
    print("somma di 3 a 5:", calcolatrice("somma", 3,5))
    