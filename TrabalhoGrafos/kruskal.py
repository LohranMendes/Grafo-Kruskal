import networkx as nx
import matplotlib.pyplot as plt

# Crio uma classe Grafo e suas atribuições
class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices # Define o número de vértices
        self.arestas = [] # Cria uma lista de arestas vazias
        self.lista_adjacencia = [[] for _ in range(vertices + 1)] # Cria uma lista de adjacência com o número de vértices + 1
        
    # Define quais são as arestas do grafos e quais seus vértices 
    def adicionar_aresta(self, v1, v2, dist):
        self.arestas.append((v1, v2, dist)) # Arestas dos grafos
        self.lista_adjacencia[v1].append((v2, dist)) # Adjacência do vértice 'v1' com 'v2' e sua distância
        self.lista_adjacencia[v2].append((v1, dist)) # Adjacência do vértice 'v2' com 'v1' e sua distância

def algoritmo_kruskal(grafo):
    # Ordena as arestas em ordem crescente de distância
    arestas_ordenadas = sorted(grafo.arestas, key=lambda aresta: aresta[2])

    # Cria um conjunto para armazenar os componentes conexos de acordo com o número de vértices
    componentes_conexos = [i for i in range(grafo.vertices)]

    # Cria uma lista para armazenar as arestas da árvore geradora mínima
    arvore_geradora = []

    # Percorre as arestas ordenadas e adiciona aquelas que não criam ciclos
    for aresta in arestas_ordenadas:
        v1, v2, dist = aresta

        # Verifica se as arestas pertencem a componentes diferentes
        if componentes_conexos[v1] != componentes_conexos[v2]:
            # Adiciona a aresta à lista de árvore geradora mínima
            arvore_geradora.append((aresta))

            # Atualiza os componentes conexos
            antigo_componente = componentes_conexos[v2]
            novo_componente = componentes_conexos[v1]

            for i in range(grafo.vertices):
                if componentes_conexos[i] == antigo_componente:
                    componentes_conexos[i] = novo_componente

    return arvore_geradora # Retorna a lista que contém as arestas da árvore geradora mínima
