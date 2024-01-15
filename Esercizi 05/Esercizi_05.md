# Esercizio sulle classi in Python

Nel file `vector.py` implementare la classe `Vector` che si comporti come un vettore di valori numerici tipico della matematica o della fisica. L'oggetto `Vector` deve essere mutabile e usare una `list` come contenitore interno. Le operazioni che dovranno essere supportate sono le seguenti:

1. Somma di vettori `a + b`. Il risultato è un nuovo vettore in cui ogni elemento è la somma degli elementi di posto corrispondente. Farne anche la versione inplace `a += b`. Lancia un eccezione se le lunghezze non corrispondono.
3. Somma di un vettore e uno scalare `a + s` (`s` può essere `int` o `float`) e `s + a`. Lo scalare viene sommato a tutti gli elementi del vettore. Farne anche la versione inplace `a += s`.
4. Differenza di vettori `a - b`. Il risultato è un nuovo vettore in cui ogni elemento è la differenza degli elementi di posto corrispondente. Farne anche la versione inplace `a -= b`. Lancia un eccezione se le lunghezze non corrispondono.
5. Differenza di un vettore e uno scalare `a - s` (`s` può essere `int` o `float`) e `s - a`. Nel primo caso, lo scalare viene sottratto a tutti gli elementi del vettore; nel secondo, viene ritornato un vettore in cui ogni elemento è dato dallo scalare meno l'elemento di quella posizione. Farne anche la versione inplace `a -= s` (solo per il primo caso).
1. Prodotto (interno o scalare) di vettori `a * b`. Il risultato è uno scalare calcolato come la somma dei prodotti degli elementi di posto corrispondente. Lancia un eccezione se le lunghezze non corrispondono.
1. Prodotto per uno scalare `a * s` (`s` può essere `int` o `float`) e `s * a`. Il risultato è un nuovo vettore ottenuto moltiplicando ogni elemento di `a` per `s`. Farne anche la versione inplace `a *= s`.
5. Divisione di un vettore per uno scalare `a / s` (`s` può essere `int` o `float`) e `s / a`. Nel primo caso, viene ritornato un vettore in cui ogni elemento è dato dall'elemento del vettore `a` diviso per lo scalare `s`; nel secondo, viene ritornato un vettore in cui ogni elemento è dato dallo scalare diviso per l'elemento di `a` in quella posizione. Farne anche la versione inplace `a /= s` (solo per il primo caso). Farne anche la versione per la divisione intera `//`.
6. Opposto di un vettore `-a`. È il vettore ottenuto negando tutti i suoi elementi.

Devono funzionare anche `len(a)`, `str(a)`, `a[3]`, `a[3:5]`.

