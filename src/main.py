import sys

from Grafo import Graph
from csvfunction import csvfunction
from mapas import mapas
from Courier import courier


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
        print("7-Realizar encomenda")
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

        elif saida == 4:
            #Imprime delivered
            csvfunction.print_delivered()

        elif saida == 5:
            #Cria estafeta
            csvfunction.new_courier()

        elif saida == 6:
            #Cria encomenda
            csvfunction.create_order()

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
                    #Procura Greedy
                    result = g.greedy(csvfunction.search_start(line), csvfunction.search_end(line))

                    print(f"Caminho: {result[0]}")
                    print(f"Distância: {result[1]}")

                    time_of_travel = csvfunction.time_of_travel(line, result[1])

                    print(f"Tempo que demorou em minutos: {time_of_travel}")

                    co2 = csvfunction.co2_emission(result[1], csvfunction.check_vehicle(line))
                    print(f"No transporte foram emitidas {co2} gramas de CO2")

                    checktime = csvfunction.check_time(line,time_of_travel)

                    if checktime == True:
                        rank_deduction = 0.0
                    else:
                        rank_deduction = 0.5

                    rank = csvfunction.rank_courier(line, rank_deduction)

                    csvfunction.deliver(line, time_of_travel, rank)

                    csvfunction.remove_delivery(line)

                elif search == 2:
                    #Procura A*
                    result = g.procura_aStar(csvfunction.search_start(line), csvfunction.search_end(line))

                    print(f"Caminho: {result[0]}")
                    print(f"Distância: {result[1]}")

                    time_of_travel = csvfunction.time_of_travel(line, result[1])

                    print(f"Tempo que demorou em minutos: {time_of_travel}")

                    co2 = csvfunction.co2_emission(result[1], csvfunction.check_vehicle(line))
                    print(f"No transporte foram emitidas {co2} gramas de CO2")

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

                    co2 = csvfunction.co2_emission(result[1], csvfunction.check_vehicle(line))
                    print(f"No transporte foram emitidas {co2} gramas de CO2")

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

                    co2 = csvfunction.co2_emission(result[1], csvfunction.check_vehicle(line))
                    print(f"No transporte foram emitidas {co2} gramas de CO2")

                    checktime = csvfunction.check_time(line,time_of_travel)

                    if checktime == True:
                        rank_deduction = 0.0
                    else:
                        rank_deduction = 0.5

                    rank = csvfunction.rank_courier(line, rank_deduction)

                    csvfunction.deliver(line, time_of_travel, rank)

                    csvfunction.remove_delivery(line)


if __name__ == "__main__":
    main()