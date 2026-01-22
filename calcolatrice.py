from operazioni import somma, sottrazione, moltiplicazione


def calcolatrice (operazione: str, a: float,b: float):
    if operazione == "somma":
        return somma (a, b)
    if operazione == "sottrazione":
        return sottrazione (a, b)
    else:
        return None
    
if __name__=="__main__":
    
    x = input("Inserisci il primo numero: ")
    y = input("Inserisci il secondo numero: ")
    print("Somma di", x, "e", y, ":", calcolatrice("somma", float(x), float(y)))
    print("Sottrazione di", x, "e", y, ":", calcolatrice("sottrazione", float(x), float(y)))
    print("Moltiplicazione di", x, "e", y, ":", calcolatrice("moltiplicazione", float(x), float(y)))



    # print(

        # "Somma di 3 e 5:", calcolatrice("somma", 3,5), "\n",
       #  "Sottrazione di 10 a 7:", calcolatrice("sottrazione", 10,7), "\n",
       #  "Moltiplicazione di 3 e 5:", calcolatrice("moltiplicazione", 3,5)
   # )