import re


def dijkstra(grafo, origem, fim):
    controle = { }
    distanciaAtual = { }
    noAtual = { }
    naoVisitados = []
    atual = origem
    noAtual[atual] = 0
    aux = []

    
    for vertice in grafo.keys():
        naoVisitados.append(vertice)   
        distanciaAtual[vertice] = float('inf')

    distanciaAtual[atual] = [0,origem] 

    naoVisitados.remove(atual)

    while naoVisitados:
        for vizinho, peso in grafo[atual].items():
             pesoCalc = peso + noAtual[atual]
             if distanciaAtual[vizinho] == float("inf") or distanciaAtual[vizinho][0] > pesoCalc:
                 distanciaAtual[vizinho] = [pesoCalc,atual]
                 controle[vizinho] = pesoCalc
                 
        if controle == {} : break    
        minVizinho = min(controle.items(), key=lambda x: x[1])
        atual=minVizinho[0]
        noAtual[atual] = minVizinho[1]
        naoVisitados.remove(atual)
        del controle[atual]

    aux.append(rota(distanciaAtual, origem, fim))
    return re.sub('[^a-zA-Z0-9 \\\]', '', str(aux)).split()


def rota(distancias,inicio, fim):
        if  fim != inicio:
            return rota(distancias,inicio, distancias[fim][1]), fim
        else:
            return inicio


def encontrar_todos_caminhos(grafo, origem, destino, path=[]):
    path = path + [origem]
    
    if origem == destino:
        return [path]
        
    if origem not in grafo:
        return []
    
    paths = []
    for vertice in list(grafo[origem].keys()):
        if vertice not in path:
            extended_paths = encontrar_todos_caminhos(grafo, vertice, destino, path)
            for p in extended_paths: 
                paths.append(p)
    return paths


# dá um jeito do grafo vim nesse formato de dicionario
grafo = { "work" : { "school" : 1, "home":2 },
          "school" : { "party":2, "E":4 },
          "home" : { "E":2 },
          "party" : { "F": 6 },
          "E" : { "F": 7 },
          "F" : { }
          }

# exemplo de execução
origem = 'work'
destino = 'E'

caminho_minimo = dijkstra(grafo,origem,destino)

lista_todos_caminho = encontrar_todos_caminhos(grafo, origem, destino)

print(caminho_minimo)
print(lista_todos_caminho)