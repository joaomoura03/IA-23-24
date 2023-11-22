import sys

from Grafo import Graph
from csvfunction import csvfunction
from mapas import mapas


# TODO (final) calcular o caminho com base no consumo do veículo para ver o mais ecológico
#   ou seja: um caminho pode ser mais ecologico mas a bicicleta nao chega a tempo, e a mota consegue
#   mas outro caminho menos ecologico que a bicicleta consiga alcancar pode obter um consumo total inferior


def main():
    g = Graph()
    mapas.populate_graph(g, sys.argv[1])

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
            line = input("\nIntroduza id da encomenda: ")
            
            if line == '0':
                print("A sair\n")
            
            else:

                print("\n1-Greedy (Informada)")
                print("2-A* (Informada)")
                print("3-DFS (Não informada)")
                print("4-BFS (Não informada)")
                print("0-Sair")

                search = int(input("\nQual é o algoritmo que deseja utilizar: "))
                print("")

                if search == 0:
                    print("A sair\n")

                elif search == 1:
                    result = g.greedy(csvfunction.search_start(line), csvfunction.search_end(line))

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

                    csvfunction.remove_delivery(line)

                elif search == 2:

                    result = g.procura_aStar(csvfunction.search_start(line), csvfunction.search_end(line))

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

                    csvfunction.remove_delivery(line)
                
                elif search == 3:
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

                    csvfunction.remove_delivery(line)

                elif search == 4:
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

                    csvfunction.remove_delivery(line)

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