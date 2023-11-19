import csv

from Grafo import Graph


class csvfunction:

    def print_delivery():
        with open('csv/delivery.csv', 'r') as entrega_csv:
            leitor_csv = csv.reader(entrega_csv)
            for linha in leitor_csv:
                print(linha)

    def print_ranking():
        with open('csv/ranking.csv', 'r') as ranking_csv:
            leitor_csv = csv.reader(ranking_csv)
            for linha in leitor_csv:
                print(linha)

    def altera_tempo(line):
        #Imprime linha a alterar
        with open('csv/delivery.csv', 'r') as delivery_csv:
            reader_csv = csv.reader(delivery_csv)
            for current_line_number, row in enumerate(delivery_csv, start=0):
                if current_line_number == line:
                    print(f"Line {line}: {row}")
        
        #Altera o tempo
        tempo = int(input("Introduza o tempo limite do estafeta em minutos "))
        lines_csv = []
        with open('csv/delivery.csv', 'r') as delivery_csv:
            reader_csv = csv.reader(delivery_csv)
            for linha in reader_csv:
                lines_csv.append(linha)
        if 0 < line <= len(lines_csv):
            lines_csv[line][6] = str(tempo)
        else:
            print(f"Linha {line} não existe no arquivo CSV.")

        with open('csv/delivery.csv', 'w', newline='') as delivery_csv:
            writer_csv = csv.writer(delivery_csv)

            writer_csv.writerows(lines_csv)

    
    def search_start(line):
        lines_csv = []
        with open('csv/delivery.csv', 'r') as delivery_csv:
            reader_csv = csv.reader(delivery_csv)
            for linha in reader_csv:
                lines_csv.append(linha)
            
            return lines_csv[line][4]
        

    def search_end(line):
        lines_csv = []
        with open('csv/delivery.csv', 'r') as delivery_csv:
            reader_csv = csv.reader(delivery_csv)
            for linha in reader_csv:
                lines_csv.append(linha)
            
            return lines_csv[line][5]
        

    def time_of_travel(line):
        lines_csv = []
        time = 0
        with open('csv/delivery.csv', 'r') as delivery_csv:
            reader_csv = csv.reader(delivery_csv)
            for linha in reader_csv:
                lines_csv.append(linha)

        if lines_csv[2] == 'Carro':
            time == Graph.calcula_custo()
