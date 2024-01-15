# Esercizio ulteriore sulle stringhe

Per comunicare in modo non palese un numero ad una persona è possibile inviargli un messaggio scritto in cui le singole cifre del numero vengono elencate a parole in mezzo ad altro testo che viene ignorato. Ad esempio per comunicare il numero 1732 si potrebbe inviare il messaggio "Ciao, **uno** dei miei amici mi ha lasciato **sette** volumetti di Demon Slayer. Ho letto fino al numero **tre** e la storia dei **due** fratelli è veramente bella." 

Nel file `secret.py` implementare la definizione della funzione:
```py
def extract_number(message: str) -> str
```
La funzione riceve una stringa con un testo in italiano e deve ritornare una nuova stringa in cui inserirà la rappresentazione di un numero estratto dalle parole presenti in `message`. Se `message` è `None`, la funzione ritorna `None`.

Ogni parola italiana corrispondente ai numeri da 0 a 9 scritti **in minuscolo, in maiuscolo o loro combinazione** viene inserita come carattere nella stringa di output. Con "parola" intendiamo una sequenza di caratteri diversi da spazio.

Ad esempio data la stringa `"Era una di quelle vecchie filastrocche per bambini che ricordava fin dall'infanzia:\n\nDieci poveri negretti se ne andarono a mangiar; uno fece indigestione, solo nove ne restar ..."` la funzione `extract_number()` restituirebbe la stringa `"19"`.

Data la stringa `"otto canotto Cinque seitan settembre quattro"` la funzione `extract_number()` restituirebbe la stringa `"854"`.