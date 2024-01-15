# Esercizi Dizionari

1\. Scrivi la funzione `dict_invert` che dato un dizionario con valori univoci (non serve controllare) genera e ritorna un nuovo dizionario con chiavi e valori invertiti:

Esempio:
```
students = {
  'Theodore': 10,
  'Mathew': 11,
  'Roxanne': 9,
}
invstud = dict_invert(students)
# invstud becomes
# {
#   10: 'Theodore',
#   11: 'Mathew',
#   9:  'Roxanne',
# }
```
2\. Scrivi la funzione `dict_invert_inplace` che dato un dizionario con valori univoci scambia chiavi e valori *in-place*.

3\. Scrivi la funzione `generate_dict` che dato un dizionario e una funzione (`func`) genera e ritorna un nuovo dizionario contenente le stesse chiavi del dizionario di input e i cui valori sono ottenuti passando quelli originali alla funzione `func`.

4\. Scrivi la funzione `occorrenze` che data una lista (o una stringa) crea e ritorna un dizionario che ha per chiavi gli elementi della lista (o i caratteri della stringa) e per valore il numero di occorrenza di quell'elemento (o di quel carattere).

5\. Scrivi la funzione `third_largest` che data una lista di numeri ritorna il terzo più grande in essa contenuto. Se la lista contiene meno di tre elementi la funzione ritorna `None`.

6\. Scrivi la funzione `max_product` che data una lista di numeri trova e ritorna la coppia che ha prodotto massimo.

7\. Scrivi la funzione `remove_common` che date due liste rimuove dalla prima gli elementi che sono già nella seconda.
