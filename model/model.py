# Importazioni
import copy
from flet_core import row

# Definire la classe Model
class Model:

    # Definire il metodo __init__
    def __init__(self):
        self._n_iterazioni = 0
        self._n_soluzioni = 0
        self._soluzioni = []

    # Ci possono essere due metodi per sviluppare questo problema:
    # 1. ciclare sui numeri --> provare a inserire in ogni cella lo stesso numero --> inserire, per esempio, l'1 nella
    # prima cella (1,1) e poi provare inserendolo nelle altre celle
    # 2. ciclare sulle celle --> per ogni cella provare a inserire tutti i numeri --> per la prima cella (1,1) provare,
    # ad esempio, a inserire tutti i numeri disponibili e continuare questo procedimento per tutte le altre celle
    # Entrambi i metodi vanno bene: nel primo caso conviene utilizzare delle tuple, invece nel secondo caso
    # le celle vengono visualizzate come elementi di una lista

    # Proveremo a utilizzare la seconda opzione

    # Definire il metodo risolvi_quadrato_magico
    def risolvi_quadrato_magico(self, N):
        # Resettare le variabili dell'__init__
        self._n_iterazioni = 0
        self._n_soluzioni = 0
        self._soluzioni = []
        self._ricorsione([], set(range(1,(N*N) +1)), N)

    # Definire il metodo _ricorsione
    def _ricorsione(self, parziale, rimanenti, N):
        self._n_iterazioni = self._n_iterazioni + 1
        # Caso terminale
        if len(parziale) == N * N:
            if self._is_soluzione(parziale, N): # inserendo la condizione dei vincoli nel caso terminale, il programma
                # impiega più tempo a compierla... per velocizzarla si potrebbe inserire poco prima della ricorsione
                # (vedere if _is_soluzione_parziale nel caso ricorsivo)
                print(parziale)
                self._n_soluzioni = self._n_soluzioni + 1
                self._soluzioni.append(copy.deepcopy(parziale))
        # Caso ricorsivo
        else:
            for i in rimanenti:
                parziale.append(i)
                if self._is_soluzione_parziale(parziale, N):
                    nuovi_rimanenti = copy.deepcopy(rimanenti)  # è necessario fare una copia per evitare di arrivare ad
                    # avere un insieme vuoto (stesso ragionamento fatto per gli esercizi precedenti nel parziale)
                    nuovi_rimanenti.remove(i)
                    self._ricorsione(parziale, nuovi_rimanenti, N)
                    parziale.pop()

    # Definire il metodo _is_soluzione, che verifica che i vincoli del quadrato magico siano rispettati
    def _is_soluzione(self, parziale, N):
        # Definire il numero magico, tramite la formula data dall'esercizio
        numero_magico = (N*((N*N)+1))/2
        # Vincolo sulle righe
        for row in range(N): # equivale alla formula: per ognuna delle N righe
            somma = 0
            sottolista = parziale[row*N:(row+1)*N] # in questo modo vengono presi gli elementi di ogni riga
            # Per ciascun elemento della sottolista (ossia della riga), viene calcolata la somma degli elementi della
            # riga stessa
            for elemento in sottolista:
                somma = somma + elemento
            # Se la somma è diversa dal numero magico, allora quella proposta non rappresenta una soluzione
            if somma != numero_magico:
                return False
        # Vincolo sulle colonne
        for col in range(N):
            somma = 0
            sottolista = parziale[(0*N)+col:((N-1)*N)+col+1:N]
            for elemento in sottolista:
                somma = somma + elemento
            if somma != numero_magico:
                return False
        # Vincolo sulla prima diagonale
        somma = 0
        for riga_col in range(N):
            somma = somma + parziale[(riga_col*N) + riga_col]
        if somma != numero_magico:
            return False
        # Vincolo sulla seconda diagonale
        somma = 0
        for riga_col in range(N):
            somma = somma + parziale[(riga_col * N) + (N-1-riga_col)]
        if somma != numero_magico:
            return False
        # Se tutti i vincoli sono soddisfatti,...
        return True

    # Definire il metodo _is_istruzione_parziale
    def _is_soluzione_parziale(self, parziale, N):
        numero_magico = (N * ((N * N) + 1)) / 2
        # Vincolo sulle righe
        n_righe = len(parziale)//N
        for row in range(n_righe):  # equivale alla formula: per ognuna delle n_righe
            somma = 0
            sottolista = parziale[row * N:(row + 1) * N]
            for elemento in sottolista:
                somma = somma + elemento
            # Se la somma è diversa dal numero magico, allora quella proposta non rappresenta una soluzione
            if somma != numero_magico:
                return False
        # Vincolo sulle colonne
        n_col = max(len(parziale) - (N*(N-1)), 0)
        for col in range(n_col):
            somma = 0
            sottolista = parziale[(0 * N) + col:((N - 1) * N) + col + 1:N]
            for elemento in sottolista:
                somma = somma + elemento
            if somma != numero_magico:
                return False
        # Vincolo sulla prima diagonale
        # Vincolo sulla seconda diagonale
        # Se tutti i vincoli sono soddisfatti,...
        return True

    # Definire il metodo stampa_soluzioni, che stampa in maniera un po più carina dal punto di vista estetico le
    # soluzioni
    def stampa_soluzione(self, soluzione, N):
        print("-----------------")
        for row in range(N):
            print([v for v in soluzione[row*N:(row+1)*N]])
        print("-----------------")

# Prova
if __name__ == '__main__':
    N = 3
    model = Model()
    model.risolvi_quadrato_magico(N)
    print(f"Quadrato di lato {N} risolto con {model._n_iterazioni} iterazioni.")
    print(f"Le soluzioni trovate sono {model._n_soluzioni}.")
    for soluzione in model._soluzioni:
        model.stampa_soluzione(soluzione, N)