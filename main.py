import sys

from Grafo import Graph
from csvfunction import csvfunction


# TODO (final) calcular o caminho com base no consumo do veículo para ver o mais ecológico
#   ou seja: um caminho pode ser mais ecologico mas a bicicleta nao chega a tempo, e a mota consegue
#   mas outro caminho menos ecologico que a bicicleta consiga alcancar pode obter um consumo total inferior

def populate_graph(g, map):
    #Todas as distâncias estão em quilometros
    if (map == '1'):
        g.add_edge("Avenida São Pedro", "Rua da Laje", 35.7)
        g.add_edge("Rua da Laje", "Rua das Forças Armadas", 12.0)
        g.add_edge("Rua das Forças Armadas", "Beco dos Unidos", 28.1)
        g.add_edge("Rua das Forças Armadas", "Rua dos Padrões", 40.0)
        g.add_edge("Rua das Forças Armadas", "Avenida São Pedro", 9.3)
        g.add_edge("Rua dos Padrões", "Rua da Laje", 12.3)
        g.add_edge("Avenida São Pedro", "Rua Humberto Delgado", 4.0)
        g.add_edge("Rua Humberto Delgado", "Rua da Laje", 4.0)

    elif (map == '2'):
        g.add_edge("Avenida São Pedro", "Rua da Laje", 35.7)
        g.add_edge("Rua da Laje", "Rua das Forças Armadas", 12.0)
        g.add_edge("Rua das Forças Armadas", "Beco dos Unidos", 28.1)
        g.add_edge("Rua das Forças Armadas", "Rua dos Padrões", 40.0)
        g.add_edge("Rua das Forças Armadas", "Avenida São Pedro", 9.3)
        g.add_edge("Rua dos Padrões", "Rua da Laje", 12.3)
        g.add_edge("Avenida São Pedro", "Rua Humberto Delgado", 4.0)
        g.add_edge("Rua Humberto Delgado", "Rua da Laje", 4.0)
        g.add_edge("Rua de Pesqueiras", "Rua Humberto Delgado", 32.0)
        g.add_edge("Rua Nova de Santa Cruz", "Rua de Pesqueiras", 63.1)
        g.add_edge("Rua de Pesqueiras", "Rua do Paço", 5.5)
        g.add_edge("Rua do Paço", "Avenida São Pedro", 6.0)
        
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
    
    elif(map == '4'):
        g.add_edge("Avenida São Pedro", "Rua da Laje", 35.7)
        g.add_edge("Rua da Laje", "Rua das Forças Armadas", 12.0)
        g.add_edge("Rua das Forças Armadas", "Beco dos Unidos", 28.1)
        g.add_edge("Rua das Forças Armadas", "Rua dos Padrões", 40.0)
        g.add_edge("Rua das Forças Armadas", "Avenida São Pedro", 9.3)
        g.add_edge("Rua dos Padrões", "Rua da Laje", 12.3)
        g.add_edge("Avenida São Pedro", "Rua Humberto Delgado", 4.0)
        g.add_edge("Rua Humberto Delgado", "Rua da Laje", 4.0)
        g.add_edge("Rua de Pesqueiras", "Rua Humberto Delgado", 32.0)
        g.add_edge("Rua Nova de Santa Cruz", "Rua de Pesqueiras", 63.1)
        g.add_edge("Rua de Pesqueiras", "Rua do Paço", 5.5)
        g.add_edge("Rua do Paço", "Avenida São Pedro", 6.0)
        g.add_edge("Rua do Paço", "Rua das Forças Armadas", 11.5)
        g.add_edge("Rua das Forças Armadas", "Avenida José Afonso", 49.4)
        g.add_edge("Avenida Jośe Afonso", "Rua do Seixal", 3.2)
        g.add_edge("Rua do Seixal", "Rua das Forças Armadas", 6.7)
        g.add_edge("Rua do Seixal", "Travessa Dom Lopes", 8.8)
        g.add_edge("Rua do Seixal", "Rua dos Padrões", 8.9)


def main():
    g = Graph()
    populate_graph(g, sys.argv[1])

    saida = -1
    while saida != 0:
        print("\n1-Desenha Grafo (Mapa)")
        print("2-Imprime entregas")
        print("3-Imprime ranking")
        print("4-Imprime entregas entregues")
        print("5-Criar estafeta")
        print("6-Criar encomenda")
        print("7-Simular encomendas")
        print("0-Saír")

        saida = int(input("\nIntroduza a sua opção: "))
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
        
        elif saida == 7:
            #Encomenda
            line = input("\nIntroduza número da linha de encomenda: ")
            
            if line == '0':
                print("A sair\n")
            
            else:

                print("\n1-Greedy (Informada)")
                print("2-DFS (Não informada)")
                print("3-BFS (Não informada)")
                print("0-Sair")

                search = int(input("\nQual é o algoritmo que deseja utilizar: "))
                print("")

                if search == 0:
                    print("A sair\n")
                
                elif search == 2:
                    #Procura DFS
                    result = g.procura_DFS(csvfunction.search_start(line), csvfunction.search_end(line), 
                                        path=[], visited=set())
                    
                    print(f"Caminho: {result[0]}")
                    print(f"Distância: {result[1]}")

                    time_of_travel = csvfunction.time_of_travel(line, result[1])

                    print(f"Tempo que demorou em minutos: {time_of_travel}")

                    checktime = csvfunction.check_time(line,time_of_travel)

                    if checktime == True:
                        rank_deduction = 0.0
                    else:
                        rank_deduction = 0.5

                    rank = csvfunction.rank_courier(line, rank_deduction)

                    csvfunction.deliver(line, time_of_travel, rank)

                elif search == 3:
                    #Procura BFS
                    result = g.procura_BFS(csvfunction.search_start(line), csvfunction.search_end(line))

                    print(f"Caminho: {result[0]}")
                    print(f"Distância: {result[1]}")

                    time_of_travel = csvfunction.time_of_travel(line, result[1])

                    print(f"Tempo que demorou em minutos: {time_of_travel}")

                    checktime = csvfunction.check_time(line,time_of_travel)

                    if checktime == True:
                        rank_deduction = 0.0
                    else:
                        rank_deduction = 0.5

                    rank = csvfunction.rank_courier(line, rank_deduction)

                    csvfunction.deliver(line, time_of_travel, rank)

        elif saida == 4:
            csvfunction.print_delivered()
            
        elif saida == 5:
            #Cria estafeta
            csvfunction.create_courier()

        elif saida == 6:
            #Cria encomenda
            csvfunction.create_order()

if __name__ == "__main__":
    main()