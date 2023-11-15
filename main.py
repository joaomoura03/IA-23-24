import networkx as nx
import matplotlib.pyplot as plt

from Grafo import Graph

def main():
    g = Graph()

    g.add_edge("Avenida São Pedro", "Rua da Laje", 357)
    g.add_edge("Rua da Laje", "Rua das Forças Armadas", 120)
    g.add_edge("Rua das Forças Armadas", "Beco dos Unidos", 281)
    g.add_edge("Rua das Forças Armadas", "Rua dos Padrões", 400)
    g.add_edge("Rua das Forças Armadas", "Avenida São Pedro", 93)
    g.add_edge("Rua dos Padrões", "Rua da Laje", 123)
    g.add_edge("Avenida São Pedro", "Rua Humberto Delgado", 40)
    g.add_edge("Rua Humberto Delgado", "Rua da Laje", 40)

    g.desenha()

if __name__ == "__main__":
    main()