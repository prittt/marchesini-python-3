# Esercizi elementari con le funzioni
Risolvere gli esercizi precedenti incapsulando le operazioni nelle funzioni `double()`, `add_n()`, `gcd()` e `is_prime()`.

Le funzioni devono avere il seguente prototipo: 

```python
def double(n: float) -> float
```

```python
def add_n(n: int) -> int
```

```python
def gcd(n: int, m:int) -> int
```

```python
def is_prime(n: int) -> bool
```

# Esercizi sulle liste
1. Scrivere le funzioni `media()` e `varianza()` che calcolano il corrispondente valore per una lista di numeri.
1. Scrivere la funzione `ribalta()` che restituisce una lista con gli elementi in ordine inverso rispetto a quella fornita in input.
1. Scrivere la funzione `potenze()` che accetta due numeri `base` e `maxesp` (intero). La funzione restituisce una lista con le potenze di base da 1 a `maxesp`.
1. Scrivere la funzione `nodup()` che restituisce una lista con gli stessi numeri di quella fornita in input, ma presenti una volta sola in qualsiasi ordine. Dato l'input `[4, 1, 1, 4, 7, 9, 7]` potrebbe ritornare `[1, 4, 7, 9]` o anche `[9, 4, 7, 1]` o qualsiasi altra permutazione.
1. Scrivere la funzione `nodup_ord()` che restituisce una lista con gli stessi numeri di quella fornita in input, ma presenti una volta sola e nello stesso ordine con cui sono stati incontrati la prima volta nell'input. Dato l'input `[4, 1, 1, 4, 7, 9, 7]` dovrebbe ritornare `[4, 1, 7, 9]`.