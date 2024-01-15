## Esercizio 1

È disponibile un file con un elenco dei valori di alcuni oggetti, uno per riga. Questi sono divisi in gruppi separati da una sola riga vuota. Ad esempio:
```
1000
2000
3000

4000

-5000
6000

7000
-6000
-9000

10000
```
Nel file `gruppi.py` implementare la funzione:
```py
def read_gruppi(filename: str) -> list[int]
```
La funzione deve aprire in modalità lettura testo il file `filename` e restituire una lista di `int`, contenente in ogni elemento la somma dei valori di ogni gruppo.

Nell'esempio precedente, la funzione restituirebbe la lista `[ 6000, 4000, 1000, -8000, 10000 ]`.

Se la funzione non riesce ad aprire il file ritorna `None`.

I file passati alla funzione saranno sempre corretti (non servono controlli), al termine del file può esserci o meno un a capo dopo l'ultimo valore, e i valori e le loro somme saranno sempre rappresentabili con un `int`.

## Esercizio 2

Nel file `demography.py` implementare la funzione:
```py
def read_cities(filename: str) -> list[tuple[str, int]]
```

È definito un formato di file binario che consente di rappresentare una sequenza di città ognuna con la corrispondente popolazione. Il file comincia con un numero intero a 32 bit senza segno in little endian che indica il numero `n` di elementi nel file. Di seguito ci sono `n` coppie di città e popolazione. Ogni città è rappresentata come una sequenza di caratteri UTF-8 zero terminata, seguita da un numero intero a 32 bit senza segno in little endian (la popolazione). Ad esempio il file binario seguente (visualizzato come in un editor esadecimale):
```
Offset(h) 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F

00000000  03 00 00 00 4D 6F 64 65 6E 61 00 D9 CF 02 00 42  ....Modena.ÙÏ..B
00000010  6F 6C 6F 67 6E 61 00 0F EB 05 00 50 65 63 68 69  ologna..ë..Pechi
00000020  6E 6F 00 0A 15 76 01                             no...v.
```
contiene 3 città:
Modena (184 281 abitanti)
Bologna (387 855 abitanti)
Pechino (24 515 850 abitanti)

La funzione deve aprire il file `filename` in modalità lettura binaria e ritornare una lista di tante coppie quanto indicato dal primo valore letto dal file. Ogni elemento conterrà il nome della città e la popolazione. 

Se l'apertura del file fallisce, o se non è possibile leggere correttamente il contenuto del file, la funzione ritorna `None`.
                
