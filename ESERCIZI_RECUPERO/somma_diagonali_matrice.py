m = [[1,2,3],
     [4,5,6],
     [7,8,9]]

def sum_primary_diagonal(matrix: list[list[int]]) -> int:
    somma: int = 0                 #Somma diagonale principale
    somma_2: int = 0               #Somma diagonale secondaria (con counter)
    counter = len(matrix[0]) - 1   #counter = 2 (indice ultima colonna)
    somma_3: int = 0               #Somma diagonale secondaria (metodo alternativo)

    for i in range(len(matrix)):
        somma += matrix[i][i]      #Somma diagonale principale: [0][0], [1][1], [2][2] = 1+5+9=15
        somma_2 += matrix[i][counter]  #Somma diagonale secondaria: [0][2], [1][1], [2][0] = 3+5+7=15
        counter -= 1               #Decrementa counter per scorrere da destra verso sinistra
        somma_3 += matrix[i][len(matrix[i]) - 1 - i]  #Somma diagonale secondaria, alternativa senza contatore, stessa cosa: 3 + 5 + 7 = 15

    return somma, somma_2, somma_3

