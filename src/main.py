import sys

from Grafo import Graph
from Csvfunction import Csvfunction
from Mapas import Mapas
from Courier import Courier, CourierCatalog
from Delivery import Delivery, DeliveryCatalog


def main():
    g = Graph()
    Mapas.populate_graph(g, sys.argv[1])

    # # hash_delivered = Csvfunction.load('../csv/delivered.csv')
    dc = DeliveryCatalog()
    #cc = CourierCatalog('../csv/ranking.csv')
    cc = CourierCatalog()

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

        elif saida == 2:
            #Desenha
            g.desenha()

        elif saida == 3:
            #Imprime entregas
            dc.print()

        elif saida == 4:
            #Imprime ranking
            CourierCatalog.print(cc)

        elif saida == 5:
            #Imprime delivered
            Csvfunction.print(hash_delivered)

        elif saida == 6:
            #Cria estafeta
            name = input("Introduza nome do estafeta: ")
            cc.create_courier(name, 147.7, 31)
            cc.save("../csv/courier.json")

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
                    result = g.greedy(Delivery.search_start(dc,key), Delivery.search_end(dc, key))

                    print(f"Caminho: {result[0]}")
                    print(f"Distância: {result[1]}")

                    time_of_travel = Delivery.time_of_travel(dc, key, result[1])

                    print(f"Tempo que demorou em minutos: {time_of_travel}")

                    co2 = Csvfunction.co2_emission(result[1], Csvfunction.check_vehicle(dc, key))
                    print(f"No transporte foram emitidas {co2} gramas de CO2")

                    checktime = Csvfunction.check_time(dc, key,time_of_travel)

                    if checktime == True:
                        rank_deduction = 0.0
                    else:
                        rank_deduction = 0.5

                    stars = float(input("\nIndique de 0 a 5 a qualidade da entrega: "))
                    rank = Csvfunction.rank_courier(dc,cc, key, rank_deduction, stars)

                    Csvfunction.deliver(dc, hash_delivered, key, time_of_travel, rank)

                elif search == 2:
                    #Procura A*
                    result = g.procura_aStar(Delivery.search_start(dc,key), Delivery.search_end(dc, key))

                    print(f"Caminho: {result[0]}")
                    print(f"Distância: {result[1]}")

                    time_of_travel = Delivery.time_of_travel(dc, key, result[1])

                    print(f"Tempo que demorou em minutos: {time_of_travel}")

                    co2 = Csvfunction.co2_emission(result[1], Csvfunction.check_vehicle(dc, key))
                    print(f"No transporte foram emitidas {co2} gramas de CO2")

                    checktime = Csvfunction.check_time(dc, key,time_of_travel)

                    if checktime == True:
                        rank_deduction = 0.0
                    else:
                        rank_deduction = 0.5

                    stars = float(input("\nIndique de 0 a 5 a qualidade da entrega: "))
                    rank = Csvfunction.rank_courier(dc,cc, key, rank_deduction, stars)

                    Csvfunction.deliver(dc, hash_delivered, key, time_of_travel, rank)
                
                elif search == 3:
                    #Procura DFS
                    result = g.procura_DFS(Delivery.search_start(dc,key), Delivery.search_end(dc, key), 
                                        path=[], visited=set())
                    
                    print(f"Caminho: {result[0]}")
                    print(f"Distância: {result[1]}")

                    time_of_travel = Delivery.time_of_travel(dc, key, result[1])

                    print(f"Tempo que demorou em minutos: {time_of_travel}")

                    co2 = Csvfunction.co2_emission(result[1], Csvfunction.check_vehicle(dc, key))
                    print(f"No transporte foram emitidas {co2} gramas de CO2")

                    checktime = Csvfunction.check_time(dc, key,time_of_travel)

                    if checktime == True:
                        rank_deduction = 0.0
                    else:
                        rank_deduction = 0.5

                    stars = float(input("\nIndique de 0 a 5 a qualidade da entrega: "))
                    rank = Csvfunction.rank_courier(dc,cc, key, rank_deduction, stars)

                    Csvfunction.deliver(dc, hash_delivered, key, time_of_travel, rank)

                elif search == 4:
                    #Procura BFS
                    result = g.procura_BFS(Delivery.search_start(dc,key), Delivery.search_end(dc, key))

                    print(f"Caminho: {result[0]}")
                    print(f"Distância: {result[1]}")

                    time_of_travel = Delivery.time_of_travel(dc, key, result[1])

                    print(f"Tempo que demorou em minutos: {time_of_travel}")

                    co2 = Csvfunction.co2_emission(result[1], Csvfunction.check_vehicle(dc, key))
                    print(f"No transporte foram emitidas {co2} gramas de CO2")

                    checktime = Csvfunction.check_time(dc, key,time_of_travel)

                    if checktime == True:
                        rank_deduction = 0.0
                    else:
                        rank_deduction = 0.5

                    stars = float(input("\nIndique de 0 a 5 a qualidade da entrega: "))
                    rank = Csvfunction.rank_courier(dc,cc, key, rank_deduction, stars)

                    Csvfunction.deliver(dc, hash_delivered, key, time_of_travel, rank)

        elif saida == 9:
            Csvfunction.save('../csv/delivered.csv', hash_delivered)
            Csvfunction.save('../csv/ranking.csv', cc)
            Csvfunction.save('../csv/delivery.csv', dc)
        


if __name__ == "__main__":
    main()