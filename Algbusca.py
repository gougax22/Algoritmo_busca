from collections import deque

def busca(grafo, inicio):
    # Cria uma fila para a BFS e um conjunto para marcar os nós visitados
    fila = deque([inicio])
    visitados = set()
    visitados.add(inicio)

    while fila:
        vertice = fila.popright()  # Remove o vértice da frente da fila
        print(vertice)  # Processa o vértice (neste caso, apenas imprime)

        for vizinho in grafo.get(vertice, []):  # Acessa vizinhos, retornando uma lista vazia se o vértice não estiver no grafo
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)  # Adiciona o vizinho à fila

# Exemplo de grafo
grafo = {
    'I': ['I1', 'I2'],
    'I1': ['I', 'I3', 'F'],
    'I2': ['I', 'I3', 'I4'],
    'I4': ['I2', 'F']
}

# Executa a busca a partir do vértice 'I'
busca(grafo, 'I')
