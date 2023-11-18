from Grafo import Graph
import csv
from csvfunction import csvfunction

def main():
    g = Graph()

    #Mapa 1
    # g.add_edge("Avenida São Pedro", "Rua da Laje", 357)
    # g.add_edge("Rua da Laje", "Rua das Forças Armadas", 120)
    # g.add_edge("Rua das Forças Armadas", "Beco dos Unidos", 281)
    # g.add_edge("Rua das Forças Armadas", "Rua dos Padrões", 400)
    # g.add_edge("Rua das Forças Armadas", "Avenida São Pedro", 93)
    # g.add_edge("Rua dos Padrões", "Rua da Laje", 123)
    # g.add_edge("Avenida São Pedro", "Rua Humberto Delgado", 40)
    # g.add_edge("Rua Humberto Delgado", "Rua da Laje", 40)


    #Mapa 2
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


    #Mapa 3
    # g.add_edge("Balança", "Campo do Gerês", 1)
    # g.add_edge("Campo do Gerês", "Carvalheira", 1)
    # g.add_edge("Carvalheira", "Chamoim e Vilar", 1)
    # g.add_edge("Chamoim e Vilar", "Chorense e Monte", 1)
    # g.add_edge("Chorense e Monte", "Cibões e Brufe", 1)
    # g.add_edge("Cibões e Brufe", "Covide", 1)
    # g.add_edge("Covide", "Gondoriz", 1)
    # g.add_edge("Gondoriz", "Moimenta", 1)
    # g.add_edge("Moimenta", "Ribeira", 1)
    # g.add_edge("Ribeira", "Rio Caldo", 1)
    # g.add_edge("Rio Caldo", "Souto", 1)
    # g.add_edge("Souto", "Valdosende", 1)
    # g.add_edge("Valdosende", "Vilar da Veiga", 1)
    # g.add_edge("Vilar da Veiga", "Balança", 1)


    saida = -1
    while saida != 0:
        print("\n1-Desenha Grafo (Mapa)")
        print("2-Imprime entregas")
        print("3-Imprime ranking")
        print("4-Simular encomendas")
        print("0-Saír")

        saida = int(input("\nIntroduza a sua opção "))
        if saida == 0:
            print("A sair\n")

        elif saida == 1:
            #Desenha
            g.desenha()

        elif saida == 2:
            #Imprime entregas
            with open('csv/entregas.csv', 'r') as entrega_csv:
                leitor_csv = csv.reader(entrega_csv)
                for linha in leitor_csv:
                    print(linha)

        elif saida == 3:
            #Imprime ranking
            with open('csv/ranking.csv', 'r') as ranking_csv:
                leitor_csv = csv.reader(ranking_csv)
                for linha in leitor_csv:
                    print(linha)
        
        elif saida == 4:
            #Encomenda
            print("\n0-Sair")
            line = int(input("Introduza número da linha de encomenda "))
            
            if line == 0:
                print("A sair\n")
            
            else:
                csvfunction.altera_tempo(line)

                print("\n1-Greedy (Informada)")
                print("2-DFS (Não informada)")
                print("0-Sair")

                search = int(input("\nQual é o algoritmo que deseja utilizar "))

                if search == 0:
                    print("A sair\n")
                
                elif search == 2:
                    #Procura DFS
                    print(g.procura_DFS(csvfunction.search_start(line), csvfunction.search_end(line),
                                        path=[], visited=set()))

if __name__ == "__main__":
    main()