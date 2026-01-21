# README
Questo codice contiene una semplice calcolatrice che esegue operazioni di:
somma tra due numeri

Include anche test unitari per verificare il corretto funzionamento della funzione di somma.

## Requisiti
- Creare un ambiente virtuale
    -python3 -m venv .venv (molto lento perchè usa python che è un linguaggio interpretativo di conseguenza più lento di uno compilato)

    -Attivare l'ambiente virtuale
    -source .venv/bin/activate     (Linux/Mac)
    -.venv\Scripts\activate    (Windows)

    - rm -rf .venv (per cancellare l'ambiente già esistente)
    - uv venv

- Verifica che l'interprete sia quello giusto
    -which python  (Linux/Mac)
    -where python  (Windows)

## Installare le dipendenze
- pip install pytest
- uv pip compile requirements.in -o requirements.txt
- source .venv/bin/activate && uv pip install -r docker/local/requirements.txt

## Esecuzione normale
- python3 calcolatrice.py

## Esecuzione dei test
- pytest test_calcolatrice.py
- pytest -v 

## Github
- echo "# DevOps-calcolatrice" >> README.md
- git init
- git add README.md
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/nicolecassari/DevOps-calcolatrice.git
- git push -u origin main