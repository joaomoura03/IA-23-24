import sys

from Grafo import Graph
from Csvfunction import Csvfunction
from Mapas import Mapas
from Courier import Courier, CourierCatalog
from Delivery import Delivery, DeliveryCatalog


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
            Csvfunction.print(hash_delivered)

        elif saida == 6:
            #Cria estafeta
            name = input("Introduza nome do estafeta: ")
            courier = Courier(name=name, classification=0.0, total=0)
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
                    result = g.greedy("Central", dc.search_end(key))

                    print(f"Caminho: {result[0]}")
                    print(f"Distância: {result[1]}")

                    time_of_travel = dc.time_of_travel(key, result[1])

                    print(f"Tempo que demorou em minutos: {time_of_travel}")

                    co2 = Csvfunction.co2_emission(result[1], dc.check_vehicle(key))
                    print(f"No transporte foram emitidas {co2} gramas de CO2")

                    checktime = dc.check_time(key, time_of_travel)

                    if checktime == True:
                        rank_deduction = 0.0
                    else:
                        rank_deduction = 0.5

                    stars = float(input("\nIndique de 0 a 5 a qualidade da entrega: "))
                    rank = cc.rank_courier(rank_deduction, stars, dc.get_courier(key))

                    #Csvfunction.deliver(dc, hash_delivered, key, time_of_travel, rank)

                elif search == 2:
                    #Procura A*
                    result = g.procura_aStar("Central", dc.search_end(key))

                    print(f"Caminho: {result[0]}")
                    print(f"Distância: {result[1]}")

                    time_of_travel = dc.time_of_travel(key, result[1])

                    print(f"Tempo que demorou em minutos: {time_of_travel}")

                    co2 = Csvfunction.co2_emission(result[1], dc.check_vehicle(key))
                    print(f"No transporte foram emitidas {co2} gramas de CO2")

                    checktime = dc.check_time(key, time_of_travel)

                    if checktime == True:
                        rank_deduction = 0.0
                    else:
                        rank_deduction = 0.5

                    stars = float(input("\nIndique de 0 a 5 a qualidade da entrega: "))
                    rank = cc.rank_courier(rank_deduction, stars, dc.get_courier(key))

                    #Csvfunction.deliver(dc, hash_delivered, key, time_of_travel, rank)
                
                elif search == 3:
                    #Procura DFS
                    result = g.procura_DFS("Central", dc.search_end(key), 
                                        path=[], visited=set())
                    
                    print(f"Caminho: {result[0]}")
                    print(f"Distância: {result[1]}")

                    time_of_travel = dc.time_of_travel(key, result[1])

                    print(f"Tempo que demorou em minutos: {time_of_travel}")

                    co2 = Csvfunction.co2_emission(result[1], dc.check_vehicle(key))
                    print(f"No transporte foram emitidas {co2} gramas de CO2")

                    checktime = dc.check_time(key, time_of_travel)

                    if checktime == True:
                        rank_deduction = 0.0
                    else:
                        rank_deduction = 0.5

                    stars = float(input("\nIndique de 0 a 5 a qualidade da entrega: "))
                    rank = cc.rank_courier(rank_deduction, stars, dc.get_courier(key))

                    #Csvfunction.deliver(dc, hash_delivered, key, time_of_travel, rank)

                elif search == 4:
                    #Procura BFS
                    result = g.procura_BFS("Central", dc.search_end(key))

                    print(f"Caminho: {result[0]}")
                    print(f"Distância: {result[1]}")

                    time_of_travel = dc.time_of_travel(key, result[1])

                    print(f"Tempo que demorou em minutos: {time_of_travel}")

                    co2 = Csvfunction.co2_emission(result[1], dc.check_vehicle(key))
                    print(f"No transporte foram emitidas {co2} gramas de CO2")

                    checktime = dc.check_time(key, time_of_travel)

                    if checktime == True:
                        rank_deduction = 0.0
                    else:
                        rank_deduction = 0.5

                    stars = float(input("\nIndique de 0 a 5 a qualidade da entrega: "))
                    rank = cc.rank_courier(rank_deduction, stars, dc.get_courier(key))

                    #Csvfunction.deliver(dc, hash_delivered, key, time_of_travel, rank)

        elif saida == 9:
            cc.save("../data/courier.json")
            dc.save("../data/delivery.json")
        


if __name__ == "__main__":
    main()