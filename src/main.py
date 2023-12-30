import sys

from Grafo import Graph
from Mapas import Mapas
from Courier import Courier, CourierCatalog
from Delivery import DeliveryCatalog
from Delivered import DeliveredCatalog
from Client import Client, ClientCatalog



def main():
    g = Graph()
    Mapas.populate_graph(g, sys.argv[1])

    signlog = -1
    while signlog != 0:

        print("\n1-Load")
        print("2-LogIn")
        print("3-SignUp")
        print("4-Save")
        print("0-Sair")

        signlog = int(input("\nIntroduza a sua opção: "))


        if signlog == 1:
            clc = ClientCatalog.load("../data/client.json")


        elif signlog == 2:
            name = str(input("\nIntroduza o username: "))
            password = str(input("\nIntroduza o password: "))
            login = clc.login(name, password)

            if login == 0:
                sys.exit()

            if name == "admin":
                saida = -1

                while saida != 0:
                    print("\n1-Load")
                    print("2-Desenha Grafo (Mapa)")
                    print("3-Realizar encomenda")
                    print("4-Save")
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
                        #Encomenda
                        print("\nDe que maneira quer definir o algoritmo de procura: ")
                        print("1- CO2")
                        print("2- Distância")

                        alg = int(input("\nIntroduza a sua opção: "))

                        key = input("\nIntroduza id da encomenda: ")

                        if key == '0':
                            print("A sair\n")

                        else :
                            list_of_keys = dc.make_more_deliveries(key)
                            courier_key = dc.get_courier_c(key)

                            for index, key in enumerate(list_of_keys):
                                
                                print(f"\nA fazer a entrega {key}")

                                result_greedy = g.greedy(dc.start_d(key), dc.end_d(key))
                                result_astar = g.procura_aStar(dc.start_d(key), dc.end_d(key))
                                result_dfs = g.procura_DFS(dc.start_d(key), dc.end_d(key), path=[], visited=set())
                                result_bfs = g.procura_BFS(dc.start_d(key), dc.end_d(key))
                                result_uni = g.uniform_cost_search(dc.start_d(key), dc.end_d(key))

                                co2_greedy = DeliveryCatalog.co2_emission(result_greedy[1], dc.check_vehicle(key))
                                co2_astar = DeliveryCatalog.co2_emission(result_astar[1], dc.check_vehicle(key))
                                co2_dfs = DeliveryCatalog.co2_emission(result_dfs[1], dc.check_vehicle(key))
                                co2_bfs = DeliveryCatalog.co2_emission(result_bfs[1], dc.check_vehicle(key))
                                co2_uni = DeliveryCatalog.co2_emission(result_uni[1], dc.check_vehicle(key))


                                if alg == 1:
                                    algorithm_co2 = min([co2_greedy, co2_astar, co2_dfs, co2_bfs, co2_uni])

                                    if algorithm_co2 == co2_greedy:
                                        result = result_greedy
                                        print("\nA usar o algoritmo Greedy")
                                    elif algorithm_co2 == co2_astar:
                                        result = result_astar
                                        print("\nA usar o algoritmo A*")
                                    elif algorithm_co2 == co2_dfs:
                                        result = result_dfs
                                        print("\nA usar o algoritmo DFS")
                                    elif algorithm_co2 == co2_bfs:
                                        result = result_bfs
                                        print("\nA usar o algoritmo BFS")
                                    elif algorithm_co2 == co2_uni:
                                        result = result_uni
                                        print("\nA usar o algoritmo Custo Uniforme")

                                elif alg == 2:
                                    algorithm = min([result_greedy[1], result_astar[1], result_dfs[1], result_bfs[1], result_uni[1]])

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
                                    elif algorithm == result_uni[1]:
                                        result = result_uni
                                        print("\nA usar o algoritmo Custo Uniforme")


                                print(f"\nCaminho: {result[0]}")
                                print(f"Distância: {result[1]}")

                                time_of_travel = dc.time_of_travel(key, result[1])

                                print(f"\nTempo que demorou em minutos: {time_of_travel}")

                                co2 = DeliveryCatalog.co2_emission(result[1], dc.check_vehicle(key))
                                print(f"\nNo transporte foram emitidas {co2} gramas de CO2")

                                dc.price_delivery(key, result[1])

                                checktime = dc.check_time(key, time_of_travel)

                                if checktime == True:
                                    rank_deduction = 0.0
                                else:
                                    rank_deduction = 0.5

                                stars = float(input("\nIndique de 0 a 5 a qualidade da entrega: "))
                                rank = cc.rank_courier(rank_deduction, stars, dc.get_courier_c(key))

                                if index < len(list_of_keys)-1:
                                    dc.change_start(list_of_keys[index + 1], dc.end_d(key))
                                    dc.change_courier(list_of_keys[index + 1], courier_key)

                                client = dc.get_client_c(key)

                                ddc.deliver(key, time_of_travel, rank, dc.remove_and_get(key), stars, client)
                                
                    elif saida == 4:
                        cc.save("../data/courier.json")
                        dc.save("../data/delivery.json")
                        ddc.save("../data/delivered.json")


            else:
                saida = -1
                while saida != 0:
                    print("\n1-Load")
                    print("2-Desenha Grafo (Mapa)")
                    print("3-Imprime entregas")
                    print("4-Imprime ranking")
                    print("5-Imprime entregas entregues")
                    print("6-Registar-se como estafeta")
                    print("7-Criar encomenda")
                    print("8-Save")
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
                        courier = Courier(name=name,number= 0.0, classification=0.0, total=0)
                        cc.add(courier)

                    elif saida == 7:
                        #Cria encomenda
                        weight = int(input("Introduza o peso da sua encomenda: "))
                        end = input("Introduza local de entrega: ")
                        time = int(input("Introduza tempo limite de entrega em minutos: "))
                        dc.create_delivery(cc, weight, end, time, name)

                    elif saida == 8:
                        cc.save("../data/courier.json")
                        dc.save("../data/delivery.json")
                        ddc.save("../data/delivered.json")


        elif signlog == 3:
            name = str(input("\nIntroduza o username: "))
            password = str(input("\nIntroduza o password: "))
            cli = Client.new_client(name, password)
            clc.signup(cli)


        elif signlog == 4:
            clc.save("../data/client.json")

if __name__ == "__main__":
    main()