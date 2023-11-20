import sys

from Grafo import Graph
from csvfunction import csvfunction

# TODO change how to calculate the time to the local

#se for para criar encomendas:
#   cliente poe primeiro e ultimo sitio e tempo limite e peso da encomenda
#   sistema vê o caminho mais ecológico e calcula tempo médio
#   sistema dá um estafeta atoa e pôe um veículo possível (que consiga entregar a tempo)


# TODO (final) calcular o caminho com base no consumo do veículo para ver o mais ecológico
#   ou seja: um caminho pode ser mais ecologico mas a bicicleta nao chega a tempo, e a mota consegue
#   mas outro caminho menos ecologico que a bicicleta consiga alcancar pode obter um consumo total inferior

def populate_graph(g, map):
    if (map == '1'):
        g.add_edge("Avenida São Pedro", "Rua da Laje", 357)
        g.add_edge("Rua da Laje", "Rua das Forças Armadas", 120)
        g.add_edge("Rua das Forças Armadas", "Beco dos Unidos", 281)
        g.add_edge("Rua das Forças Armadas", "Rua dos Padrões", 400)
        g.add_edge("Rua das Forças Armadas", "Avenida São Pedro", 93)
        g.add_edge("Rua dos Padrões", "Rua da Laje", 123)
        g.add_edge("Avenida São Pedro", "Rua Humberto Delgado", 40)
        g.add_edge("Rua Humberto Delgado", "Rua da Laje", 40)

    elif (map == '2'):
        g.add_edge("Avenida São Pedro", "Rua da Laje", 357)
        g.add_edge("Rua da Laje", "Rua das Forças Armadas", 120)
        g.add_edge("Rua das Forças Armadas", "Beco dos Unidos", 281)
        g.add_edge("Rua das Forças Armadas", "Rua dos Padrões", 400)
        g.add_edge("Rua das Forças Armadas", "Avenida São Pedro", 93)
        g.add_edge("Rua dos Padrões", "Rua da Laje", 123)
        g.add_edge("Avenida São Pedro", "Rua Humberto Delgado", 40)
        g.add_edge("Rua Humberto Delgado", "Rua da Laje", 40)
        g.add_edge("Rua de Pesqueiras", "Rua Humberto Delgado", 320)
        g.add_edge("Rua Nova de Santa Cruz", "Rua de Pesqueiras", 631)
        g.add_edge("Rua de Pesqueiras", "Rua do Paço", 55)
        g.add_edge("Rua do Paço", "Avenida São Pedro", 60)
        
    elif (map == '3'):
        g.add_edge("Balança", "Campo do Gerês", 1)
        g.add_edge("Campo do Gerês", "Carvalheira", 1)
        g.add_edge("Carvalheira", "Chamoim e Vilar", 1)
        g.add_edge("Chamoim e Vilar", "Chorense e Monte", 1)
        g.add_edge("Chorense e Monte", "Cibões e Brufe", 1)
        g.add_edge("Cibões e Brufe", "Covide", 1)
        g.add_edge("Covide", "Gondoriz", 1)
        g.add_edge("Gondoriz", "Moimenta", 1)
        g.add_edge("Moimenta", "Ribeira", 1)
        g.add_edge("Ribeira", "Rio Caldo", 1)
        g.add_edge("Rio Caldo", "Souto", 1)
        g.add_edge("Souto", "Valdosende", 1)
        g.add_edge("Valdosende", "Vilar da Veiga", 1)
        g.add_edge("Vilar da Veiga", "Balança", 1)

    else:
        print("Mapa não existe")  


def main():
    g = Graph()
    populate_graph(g, sys.argv[1])

    saida = -1
    while saida != 0:
        print("\n1-Desenha Grafo (Mapa)")
        print("2-Imprime entregas")
        print("3-Imprime ranking")
        print("4-Criar estafeta")
        print("5-Criar encomenda")
        print("6-Simular encomendas")
        print("0-Saír")

        saida = int(input("\nIntroduza a sua opção "))
        if saida == 0:
            print("A sair\n")

        elif saida == 1:
            #Desenha
            g.desenha()

        elif saida == 2:
            #Imprime entregas
            csvfunction.print_delivery()

        elif saida == 3:
            #Imprime ranking
            csvfunction.print_ranking()
        
        elif saida == 6:
            #Encomenda
            line = input("\nIntroduza número da linha de encomenda ")
            print("0-Sair")
            
            if line == '0':
                print("A sair\n")
            
            else:

                print("\n1-Greedy (Informada)")
                print("2-DFS (Não informada)")
                print("3-BFS (Não informada)")
                print("0-Sair")

                search = int(input("\nQual é o algoritmo que deseja utilizar "))

                if search == 0:
                    print("A sair\n")
                
                elif search == 2:
                    #Procura DFS
                    result = g.procura_DFS(csvfunction.search_start(line), csvfunction.search_end(line), 
                                        path=[], visited=set())
                    print(result)
                    print(csvfunction.time_of_travel(line, result[1]))

                    csvfunction.rank_courier(line)

                elif search == 3:
                    #Procura BFS
                    result = g.procura_BFS(csvfunction.search_start(line), csvfunction.search_end(line))
                    print(result)
                    print(csvfunction.time_of_travel(line, result[1]))

            
        elif saida == 4:
            #Cria estafeta
            csvfunction.create_courier()

        elif saida == 5:
            #Cria encomenda
            csvfunction.create_order()

if __name__ == "__main__":
    main()