from operazioni import somma, sottrazione, moltiplicazione


def calcolatrice (operazione: str, a: float,b: float):
    if operazione == "somma":
        return somma (a, b)
    if operazione == "sottrazione":
        return sottrazione (a, b)
    else:
        return None
    
if __name__=="__main__":
    print(
         ("somma di 3 a 5:", calcolatrice("somma", 3,5)), "\n",
         ("sottrazione di 10 a 7:", calcolatrice("sottrazione", 10,7)), "\n",
         ("moltiplicazione di 3 e 5:", calcolatrice("moltiplicazione", 3,5))
    )