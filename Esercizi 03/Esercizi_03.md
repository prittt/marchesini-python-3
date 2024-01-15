# Alfabeto Farfallino

Nel file `farfallino.py` implementare la definizione della seguente funzione:

```py
def farfallino_encode(s: str) -> str
```

La funzione accetta una stringa e ritorna una stringa, contenente quella originale codificata con l'Alfabeto Farfallino. 
L'Alfabeto Farfallino è un gioco linguistico per bambini che consiste nel raddoppiare ogni vocale con l'aggiunta di una *f* interposta: per esempio, `"a"` diventa `"afa"`, `"e"` diventa `"efe"`, e così via (quindi `"ciao"` diventa `"cifiafaofo"`). 

# Traduci

Nel file `translate.py` implementare la definizione della funzione:

```py
def translate(s: str, from_lst: str, to_lst: str) -> str
```

La funzione deve cercare ogni carattere di `s` in `from_lst` e se il carattere è presente, sostituirlo con l'elemento di posizione corrispondente in `to_lst`. Ad esempio, data la stringa `s = "ciao"`, chiamare la funzione `translate(s, "abdc", "wxzy")` trasforma `s` in `"yiwo"`.

Se `from_lst` e `to_lst` hanno lunghezze diverse, la funzione non modifica `s`.


# Conta Parole

Nel file `conta.py` implementare la definizione della funzione:

```py
def conta_parole (s: str) -> int;
```

La funzione accetta come parametro una stringa e deve restituire quante parole sono presenti all'interno della stringa, dove **con "parola" intendiamo una sequenza di caratteri diversi da spazio**. 

Ad esempio, chiamare la funzione passando la stringa `"  Questa e' una stringa lunga 45 caratteri.  "` dovrebbe ritornare 7. Con la stringa `"1 2 3 a b c"` dovrebbe ritornare 6. Con la stringa `"! @?$ ciao,prova"` dovrebbe ritornare 3.


# Hex String

Creare il file `hexstring.py` che consenta di utilizzare la seguente funzione:

```py
def hexstring2vec(s: str) -> list[int];
```
La funzione accetta come input una stringa contenente da 0 a 8 coppie di caratteri che rappresentano cifre esadecimali, ovvero da `'0'` a `'9'` e da `'A'` a `'F'` e da `'a'` a `'f'`. La funzione deve ritornare una lista contenente sempre 8 valori (di tipo int) corrispondenti ad ogni coppia di caratteri in `s` interpretata come numero esadecimale a due cifre. Se `s` contiene meno di 8 coppie di cifre esadecimali, i restanti valori dovranno essere zero.

Alcuni esempi:
```
s                  | out 
------------------ | -------------------------------------------------
"12AB34CD56EF7890" | [ 0x12, 0xAB, 0x34, 0xCD, 0x56, 0xEF, 0x78, 0x90 ]
"12ab34cd56ef7890" | [ 0x12, 0xAB, 0x34, 0xCD, 0x56, 0xEF, 0x78, 0x90 ]
"35AF"             | [ 0x35, 0xAF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ]
"0A0a0B0bcCdD"     | [ 0x0A, 0x0A, 0x0B, 0x0B, 0xCC, 0xDD, 0x00, 0x00 ]
""                 | [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ]
```

La stringa `s` sarà sempre formattata correttamente, ovvero conterrà solo lettere da A a F minuscole o maiuscole o numeri, conterrà sempre un numero pari di cifre esadecimali e mai superiore a 16.

# Rimuovi Singoli Spazi

Nel file `rimuovi_singoli_spazi.py` inserire la definizione della funzione:

```py
def rimuovi_singoli_spazi(s: str) -> str
```

La funzione accetta come parametro una stringa `s`, e ritorna una nuova stringa formata eliminando da `s` i singoli spazi, ma non le sequenze di più spazi consecutivi.

Ad esempio:
```
Input: " a b c "
Output: "abc"
```
```
Input: "  a  b  c  "
Output: "  a  b  c  "
```
```
Input: "  abc   def ghi   jkl    mno pqr  s "
Output: "  abc   defghi   jkl    mnopqr  s"
```

# Formato Data

Nel file `formato.py` definire la funzione corrispondente alla seguente dichiarazione: 

```py
def is_date(s: str) -> bool
```
La funzione accetta una stringa e deve verificare se rispetta il formato di una data in cui il giorno e il mese sono rappresentati da due cifre, l'anno da quattro cifre e sono separati dal carattere "/".
La funzione ritorna `True` se il formato è corretto, `False` altrimenti.
Ad esempio la stringa `"10/07/2015"` rispetta il formato, mentre `"10-7-15"` o `"10.07.2015"` no.
