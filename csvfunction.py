import csv

from Grafo import Graph


class csvfunction:

    def print_delivery():
        with open('csv/delivery.csv', 'r') as entrega_csv:
            leitor_csv = csv.reader(entrega_csv)
            for row in leitor_csv:
                print(row)

    def print_ranking():
        with open('csv/ranking.csv', 'r') as ranking_csv:
            leitor_csv = csv.reader(ranking_csv)
            for row in leitor_csv:
                print(row)


    def altera_tempo(line):
        #Imprime linha a alterar
        with open('csv/delivery.csv', 'r') as delivery_csv:
            reader_csv = csv.reader(delivery_csv, delimiter=',')
            for row in reader_csv:
                if row[0] == line:
                    print(f"Line {line}: {row}")
        
        #Altera o tempo
        tempo = int(input("Introduza o tempo limite do estafeta em minutos "))
        lines_csv = []
        with open('csv/delivery.csv', 'r') as delivery_csv:
            reader_csv = csv.reader(delivery_csv)
            for row in reader_csv:
                if row[0] == line:
                    row[6] = str(tempo)
                lines_csv.append(row)

        with open('csv/delivery.csv', 'w', newline='') as delivery_csv:
            writer_csv = csv.writer(delivery_csv)

            writer_csv.writerows(lines_csv)

    
    def search_start(line):
        with open('csv/delivery.csv', 'r') as delivery_csv:
            reader_csv = csv.reader(delivery_csv)
            for row in reader_csv:
                if row[0] == line:
                    line_row = row[4]
                    return line_row
                
        print("Linha não existe")
        

    def search_end(line):
        with open('csv/delivery.csv', 'r') as delivery_csv:
            reader_csv = csv.reader(delivery_csv)
            for row in reader_csv:
                if row[0] == line:
                    line_row = row[5]
                    return line_row
                
        print("Linha não existe")
        

    ####################################
    #    calcula tempo de viagem -> consudera custo como metros(alterar)
    ####################################
    def time_of_travel(line, consumo):
        with open('csv/delivery.csv', 'r') as delivery_csv:
            reader_csv = csv.reader(delivery_csv)
            for row in reader_csv:
                if row[0] == line:
                    if row[2] == 'Carro':
                        final_time = (consumo/1000) * (50 - 0.1 * float(row[3]))
                        return final_time
                    
                    if row[2] == 'Moto':
                        final_time = (consumo/1000) * (35 - 0.5 * float(row[3]))
                        return final_time
                    
                    if row[2] == 'Bicicleta':
                        final_time = (consumo/1000) * (10 - 0.6 * float(row[3]))
                        return final_time
