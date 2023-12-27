import sys

from Grafo import Graph
from Mapas import Mapas
from Courier import Courier, CourierCatalog
from Delivery import DeliveryCatalog
from Delivered import DeliveredCatalog


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
            #Load
            cc = CourierCatalog.load("../data/courier.json")
            dc = DeliveryCatalog.load("../data/delivery.json")
            ddc = DeliveredCatalog.load("../data/delivered.json")

        elif saida == 2:
            #Desenha
            g.desenha()

        elif saida == 3:
            #Imprime entregas
            dc.print()

        elif saida == 4:
            #Imprime ranking
            cc.print()

        elif saida == 5:
            #Imprime delivered
            ddc.print()

        elif saida == 6:
            #Cria estafeta
            name = input("Introduza nome do estafeta: ")
            courier = Courier(name=name,number= 0.0, classification=0.0, total=0)
            cc.add(courier)

        elif saida == 7:
            #Cria encomenda
            weight = int(input("Introduza o peso da sua encomenda: "))
            end = input("Introduza local de entrega: ")
            time = int(input("Introduza tempo limite de entrega em minutos: "))
            dc.create_delivery(cc, weight, end, time)

        elif saida == 8:
            #Encomenda
            key = input("\nIntroduza id da encomenda: ")

            if key == '0':
                print("A sair\n")

            else :

                list_of_keys = dc.make_more_deliveries(key)

                for index, key in enumerate(list_of_keys):
                    
                    print(f"\nA fazer a entrega {key}")
                    result_greedy = g.greedy(dc.start_d(key), dc.end_d(key))
                    result_astar = g.procura_aStar(dc.start_d(key), dc.end_d(key))
                    result_dfs = g.procura_DFS(dc.start_d(key), dc.end_d(key), path=[], visited=set())
                    result_bfs = g.procura_BFS(dc.start_d(key), dc.end_d(key))

                    algorithm = min([result_greedy[1], result_astar[1], result_dfs[1], result_bfs[1]])

                    if algorithm == result_greedy[1]:
                        result = result_greedy
                        print("\nA usar o algoritmo Greedy")
                    elif algorithm == result_astar[1]:
                        result = result_astar
                        print("\nA usar o algoritmo A*")
                    elif algorithm == result_dfs[1]:
                        result = result_dfs
                        print("\nA usar o algoritmo DFS")
                    elif algorithm == result_bfs[1]:
                        result = result_bfs
                        print("\nA usar o algoritmo BFS")

                    print(f"\nCaminho: {result[0]}")
                    print(f"Distância: {result[1]}")

                    time_of_travel = dc.time_of_travel(key, result[1])

                    print(f"\nTempo que demorou em minutos: {time_of_travel}")

                    co2 = Courier.co2_emission(result[1], dc.check_vehicle(key))
                    print(f"\nNo transporte foram emitidas {co2} gramas de CO2")

                    checktime = dc.check_time(key, time_of_travel)

                    if checktime == True:
                        rank_deduction = 0.0
                    else:
                        rank_deduction = 0.5

                    stars = float(input("\nIndique de 0 a 5 a qualidade da entrega: "))
                    rank = cc.rank_courier(rank_deduction, stars, dc.get_courier_c(key))

                    dc.change_start(list_of_keys[index + 1], dc.end_d(key))

                    ddc.deliver(key, time_of_travel, rank, dc.remove_and_get(key))
                    

        elif saida == 9:
            cc.save("../data/courier.json")
            dc.save("../data/delivery.json")
            ddc.save("../data/delivered.json")


if __name__ == "__main__":
    main()