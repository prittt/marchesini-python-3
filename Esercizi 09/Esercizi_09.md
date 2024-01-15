Un'azienda vuole sostituire le lampadine ad incandescenza dei lampioni stradali con quelle a LED che sono più efficienti. Poiché le nuove lampadine sono anche più potenti, l'azienda pensa che alcuni lampioni non siano necessari e che potrebbe risparmiare ancora più energia non usandoli.

Modelliamo l'autostrada come una linea retta che misura M metri. Per convenzione, la strada parte al metro 0. L'x-esimo metro è un punto sulla strada che dista x metri dalla "partenza". Se una luce è posiziona al metro x e il LED ha un raggio di illuminazione pari a R metri, la strada sarà illuminata nel segmento da max(0, x - R) a min(M, x + R) inclusi. L'azienda vuole installare i LED in modo tale che ogni punto della strada sia illuminato, ovvero facendo sì che non ci siano zone d'ombra.

I lampioni lasciati senza lampadina non generano alcun tipo di illuminazione. 


Nei file `optimal_illumination.py` definire la funzione: 

```c
def OptimalIllumination(M: int, R: int, light: list)
```

La funzione prende in input la lunghezza dell'autostrada in metri, `M`, il raggio di illuminazione delle nuove lampadine, `R`, e le posizioni di tutti i lampioni memorizzate in ordine nella lista `light`.

La funzione deve trovare il numero minimo di lampadine che l'azienda deve installare per illuminare l'intera superstrada. La funzione ritorna la soluzione ottima memorizzata in una lista contenente 0 nelle posizioni corrispondenti a lampioni lasciati sprovvisti di lampadina, 1 nelle altre.

Se non esiste alcuna soluzione valida, la funzione ritorna una lista vuota.

Seguono alcuni esempi:

1. `M = 10`, `R = 3`, `light = [2, 7, 9]`

<img src="https://olj.ing.unimore.it/static/oljApp/fondamenti/fdi-ii/20230705/20230705_illumination_01.png" width=800px>

In questo caso è possibile illuminare tutta la strada accendendendo il primo e il secondo lampione, lasciando spento il terzo. Il vettore soluzione ritornato sarà quindi: `[1, 1, 0]`.

2. `M = 10`, `R = 2`, `light = [2, 7, 9]`

<img src="https://olj.ing.unimore.it/static/oljApp/fondamenti/fdi-ii/20230705/20230705_illumination_02.png" width=800px>

In questo caso NON è possibile illuminare tutta la strada, nemmeno accendendo tutti i lampioni. La funzione dovrà quindi ritornare `[]`.

3. `M = 10`, `R = 2`, `light = [2, 3, 7, 9]`

<img src="https://olj.ing.unimore.it/static/oljApp/fondamenti/fdi-ii/20230705/20230705_illumination_03.png" width=800px>

In questo caso è possibile illuminare tutta la strada solamente accendendendo tutti i lampioni. La lista ritornata sarà quindi: `[1, 1, 1, 1]`.
                