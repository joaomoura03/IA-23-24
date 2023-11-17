from Grafo import Graph

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
    # g.add_edge("Avenida São Pedro", "Rua da Laje", 357)
    # g.add_edge("Rua da Laje", "Rua das Forças Armadas", 120)
    # g.add_edge("Rua das Forças Armadas", "Beco dos Unidos", 281)
    # g.add_edge("Rua das Forças Armadas", "Rua dos Padrões", 400)
    # g.add_edge("Rua das Forças Armadas", "Avenida São Pedro", 93)
    # g.add_edge("Rua dos Padrões", "Rua da Laje", 123)
    # g.add_edge("Avenida São Pedro", "Rua Humberto Delgado", 40)
    # g.add_edge("Rua Humberto Delgado", "Rua da Laje", 40)
    # g.add_edge("Rua de Pesqueiras", "Rua Humberto Delgado", 320)
    # g.add_edge("Rua Nova de Santa Cruz", "Rua de Pesqueiras", 631)
    # g.add_edge("Rua de Pesqueiras", "Rua do Paço", 55)
    # g.add_edge("Rua do Paço", "Avenida São Pedro", 60)


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
        print("\n1-Desenha Grafo(Mapa)")
        print("2-Fazer encomenda")
        print("0-Saír")

        saida = int(input("\nIntroduza a sua opção "))
        if saida == 0:
            print("A sair\n")
        elif saida == 1:
            g.desenha()


if __name__ == "__main__":
    main()