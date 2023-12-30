import networkx as nx
import matplotlib.pyplot as plt
import math
import heapq
import time

from queue import Queue
from Nodo import Node


class Graph:

    def __init__(self, directed=False):
        self.m_nodes = []
        self.m_directed = directed
        self.m_graph = {}
        self.m_h = {}


    ################################
    #   encontrar nodo pelo nome
    ################################

    def get_node_by_name(self, name):
        search_node = Node(name)
        for node in self.m_nodes:
            if node == search_node:
                return node
        return None

    ############################
    #   imprimir arestas
    ############################

    def imprime_aresta(self):
        listaA = ""
        lista = self.m_graph.keys()
        for nodo in lista:
            for (nodo2, custo) in self.m_graph[nodo]:
                listaA = listaA + nodo + " ->" + nodo2 + " custo:" + str(custo) + "\n"
        return listaA

    ################
    #   adicionar   aresta no grafo
    ################

    def add_edge(self, node1, node2, weight):
        n1 = Node(node1)
        n2 = Node(node2)
        if (n1 not in self.m_nodes):
            n1_id = len(self.m_nodes) # numeração sequencial
            n1.setId(n1_id)
            self.m_nodes.append(n1)
            self.m_graph[node1] = []

        if (n2 not in self.m_nodes):
            n2_id = len(self.m_nodes) # numeração sequencial
            n2.setId(n2_id)
            self.m_nodes.append(n2)
            self.m_graph[node2] = []

        self.m_graph[node1].append((node2, weight)) # poderia ser n1 para trabalhar com nodos no grafo

        if not self.m_directed:
              self.m_graph[node2].append((node1, weight))


    ##########################
    # devolver nodos
    ##########################

    def getNodes(self):
        return self.m_nodes

    ##############
    #    devolver o custo de uma aresta
    ##############

    def get_arc_cost(self, node1, node2):
        custoT = math.inf
        a = self.m_graph[node1]  # lista de arestas para aquele nodo
        for (nodo, custo) in a:
            if nodo == node2:
                custoT = custo

        return custoT

    ##############################
    #  dado um caminho calcula o seu custo
    ##############################

    def calcula_custo(self, caminho):
        # caminho é uma lista de nodos
        teste = caminho
        custo = 0
        i = 0
        while i + 1 < len(teste):
            custo = custo + self.get_arc_cost(teste[i], teste[i + 1])
            i = i + 1
        return custo


    ###########################
    # desenha grafo  modo grafico
    ###########################

    def desenha(self):
        ##criar lista de vertices
        lista_v = self.m_nodes
        g = nx.Graph()
        for nodo in lista_v:
            n = nodo.getName()
            g.add_node(n)
            for (adjacente, peso) in self.m_graph[n]:
                g.add_edge(n, adjacente, weight=peso)

        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.draw()
        plt.show()
        
    ####################################
    #    add_heuristica   -> define heuristica para cada nodo 
    ####################################

    def add_heuristica(self, n, estima):
        n1 = Node(n)
        if n1 in self.m_nodes:
            self.m_h[n] = estima


    def procura_DFS(self, start, end, path=[], visited=set()):
        start_time = time.time()
        path.append(start)
        visited.add(start)

        if start == end:
            custoT = self.calcula_custo(path)
            end_time = time.time()
            elapsed_time = end_time - start_time
            return (path, custoT, elapsed_time)
        for (adjacente, peso) in self.m_graph[start]:
            if adjacente not in visited:
                resultado = self.procura_DFS(adjacente, end, path, visited)
                if resultado is not None:
                    return resultado
        path.pop()
        return None


    def procura_BFS(self, start, end):
        start_time = time.time()
        # definir nodos visitados para evitar ciclos
        visited = set()
        fila = Queue()
        custo = 0
        # adicionar o nodo inicial à fila e aos visitados
        fila.put(start)
        visited.add(start)

        # garantir que o start node nao tem pais...
        parent = dict()
        parent[start] = None

        path_found = False
        while not fila.empty() and path_found == False:
            nodo_atual = fila.get()
            if nodo_atual == end:
                path_found = True
            else:
                for (adjacente, peso) in self.m_graph[nodo_atual]:
                    if adjacente not in visited:
                        fila.put(adjacente)
                        parent[adjacente] = nodo_atual
                        visited.add(adjacente)

        path = []
        if path_found:
            path.append(end)
            while parent[end] is not None:
                path.append(parent[end])
                end = parent[end]
            path.reverse()
            # funçao calcula custo caminho
            custo = self.calcula_custo(path)
            end_time = time.time()
            elapsed_time = end_time - start_time
        return (path, custo, elapsed_time)


    def getNeighbours(self, nodo):
        lista = []
        for (adjacente, peso) in self.m_graph[nodo]:
            lista.append((adjacente, peso))
        return lista


    def greedy(self, start, end):
        start_time = time.time()
        open_list = set([start])
        closed_list = set([])

        parents = {}
        parents[start] = start

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n == None or self.m_h[v] < self.m_h[n]:
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            if n == end:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)

                reconst_path.reverse()

                end_time = time.time()
                elapsed_time = end_time - start_time
                return (reconst_path, self.calcula_custo(reconst_path), elapsed_time)

            for (m, weight) in self.getNeighbours(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n


            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None


    def getH(self, nodo):
        if nodo not in self.m_h.keys():
            return 1000
        else:
            return (self.m_h[nodo])


    def procura_aStar(self, start, end):
        start_time = time.time()
        open_list = {start}
        closed_list = set([])

        g = {}

        g[start] = 0

        parents = {}
        parents[start] = start
        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n == None or g[v] + self.getH(v) < g[n] + self.getH(n):
                    n = v
            if n == None:
                print('Path does not exist!')
                return None

            if n == end:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)

                reconst_path.reverse()

                end_time = time.time()
                elapsed_time = end_time - start_time
                return (reconst_path, self.calcula_custo(reconst_path), elapsed_time)

            for (m, weight) in self.getNeighbours(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None
    

    def uniform_cost_search(self, start_node, end_node):
        start_time = time.time()
        priority_queue = [(0, start_node, [])]  # (cost, current node, path)
        visited = set()

        while priority_queue:
            cost, current_node, path = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)
            path = path + [current_node]

            if current_node == end_node:
                end_time = time.time()
                elapsed_time = end_time - start_time
                return path, cost, elapsed_time

            for neighbor, edge_cost in self.m_graph.get(current_node, []):
                if neighbor not in visited:
                    new_cost = cost + edge_cost
                    heapq.heappush(priority_queue, (new_cost, neighbor, path))

        return None, math.inf