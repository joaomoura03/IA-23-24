import sys

from Grafo import Graph
from Csvfunction import Csvfunction
from Mapas import Mapas
from Courier import Courier
from Delivery import Delivery


def main():
    g = Graph()
    Mapas.populate_graph(g, sys.argv[1])

    saida = -1
    while saida != 0:
        print("\n1-Load")
        print("2-Desenha Grafo (Mapa)")
        print("3-Imprime entregas")
        print("4-Imprime ranking")
        print("5-Imprime entregas entregues")
        print("6-Criar estafeta")
        print("7-Criar encomenda")
        print("8-Realizar encomenda")
        print("9-Save")
        print("0-Sair")

        saida = int(input("\nIntroduza a sua opção: "))
        if saida == 0:
            print("A sair\n")

        elif saida == 1:
            hash_delivered = Csvfunction.load('../csv/delivered.csv')
            hash_delivery = Csvfunction.load('../csv/delivery.csv')
            hash_ranking = Csvfunction.load('../csv/ranking.csv')

        elif saida == 2:
            #Desenha
            g.desenha()

        elif saida == 3:
            #Imprime entregas
            Csvfunction.print(hash_delivery)

        elif saida == 4:
            #Imprime ranking
            Csvfunction.print(hash_ranking)

        elif saida == 5:
            #Imprime delivered
            Csvfunction.print(hash_delivered)

        elif saida == 6:
            #Cria estafeta
            name = input("Introduza nome do estafeta: ")
            Courier.new_courier(hash_ranking, name)

        elif saida == 7:
            #Cria encomenda
            weight = int(input("Introduza o peso da sua encomenda: "))
            end = input("Introduza local de entrega: ")
            time = int(input("Introduza tempo limite de entrega em minutos: "))
            Delivery.create_delivery(hash_delivery, hash_ranking, weight, end, time)

        elif saida == 8:
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
                    result = g.greedy(Csvfunction.search_start(line), Csvfunction.search_end(line))

                    print(f"Caminho: {result[0]}")
                    print(f"Distância: {result[1]}")

                    time_of_travel = Csvfunction.time_of_travel(line, result[1])

                    print(f"Tempo que demorou em minutos: {time_of_travel}")

                    co2 = Csvfunction.co2_emission(result[1], Csvfunction.check_vehicle(line))
                    print(f"No transporte foram emitidas {co2} gramas de CO2")

                    checktime = Csvfunction.check_time(line,time_of_travel)

                    if checktime == True:
                        rank_deduction = 0.0
                    else:
                        rank_deduction = 0.5

                    rank = Csvfunction.rank_courier(line, rank_deduction)

                    Csvfunction.deliver(line, time_of_travel, rank)

                    Csvfunction.remove_delivery(line)

                elif search == 2:
                    #Procura A*
                    result = g.procura_aStar(Csvfunction.search_start(line), Csvfunction.search_end(line))

                    print(f"Caminho: {result[0]}")
                    print(f"Distância: {result[1]}")

                    time_of_travel = Csvfunction.time_of_travel(line, result[1])

                    print(f"Tempo que demorou em minutos: {time_of_travel}")

                    co2 = Csvfunction.co2_emission(result[1], Csvfunction.check_vehicle(line))
                    print(f"No transporte foram emitidas {co2} gramas de CO2")

                    checktime = Csvfunction.check_time(line,time_of_travel)

                    if checktime == True:
                        rank_deduction = 0.0
                    else:
                        rank_deduction = 0.5

                    rank = Csvfunction.rank_courier(line, rank_deduction)

                    Csvfunction.deliver(line, time_of_travel, rank)

                    Csvfunction.remove_delivery(line)
                
                elif search == 3:
                    #Procura DFS
                    result = g.procura_DFS(Csvfunction.search_start(line), Csvfunction.search_end(line), 
                                        path=[], visited=set())
                    
                    print(f"Caminho: {result[0]}")
                    print(f"Distância: {result[1]}")

                    time_of_travel = Csvfunction.time_of_travel(line, result[1])

                    print(f"Tempo que demorou em minutos: {time_of_travel}")

                    co2 = Csvfunction.co2_emission(result[1], Csvfunction.check_vehicle(line))
                    print(f"No transporte foram emitidas {co2} gramas de CO2")

                    checktime = Csvfunction.check_time(line,time_of_travel)

                    if checktime == True:
                        rank_deduction = 0.0
                    else:
                        rank_deduction = 0.5

                    rank = Csvfunction.rank_courier(line, rank_deduction)

                    Csvfunction.deliver(line, time_of_travel, rank)

                    Csvfunction.remove_delivery(line)

                elif search == 4:
                    #Procura BFS
                    result = g.procura_BFS(Csvfunction.search_start(line), Csvfunction.search_end(line))

                    print(f"Caminho: {result[0]}")
                    print(f"Distância: {result[1]}")

                    time_of_travel = Csvfunction.time_of_travel(line, result[1])

                    print(f"Tempo que demorou em minutos: {time_of_travel}")

                    co2 = Csvfunction.co2_emission(result[1], Csvfunction.check_vehicle(line))
                    print(f"No transporte foram emitidas {co2} gramas de CO2")

                    checktime = Csvfunction.check_time(line,time_of_travel)

                    if checktime == True:
                        rank_deduction = 0.0
                    else:
                        rank_deduction = 0.5

                    rank = Csvfunction.rank_courier(line, rank_deduction)

                    Csvfunction.deliver(line, time_of_travel, rank)

                    Csvfunction.remove_delivery(line)

        elif saida == 9:
            Csvfunction.save('../csv/delivered.csv', hash_delivered)
            Csvfunction.save('../csv/ranking.csv', hash_ranking)
            Csvfunction.save('../csv/delivery.csv', hash_delivery)
        


if __name__ == "__main__":
    main()