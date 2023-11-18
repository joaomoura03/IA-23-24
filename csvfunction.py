import csv


class csvfunction:

    def altera_tempo(line):
        #Imprime linha a alterar
        with open('csv/entregas.csv', 'r') as delivery_csv:
            reader_csv = csv.reader(delivery_csv)
            for current_line_number, row in enumerate(delivery_csv, start=0):
                if current_line_number == line:
                    print(f"Line {line}: {row}")
        
        #Altera o tempo
        tempo = int(input("Introduza o tempo limite do estafeta em minutos "))
        lines_csv = []
        with open('csv/entregas.csv', 'r') as delivery_csv:
            reader_csv = csv.reader(delivery_csv)
            for linha in reader_csv:
                lines_csv.append(linha)
        if 0 < line <= len(lines_csv):
            lines_csv[line][6] = str(tempo)
        else:
            print(f"Linha {line} não existe no arquivo CSV.")

        with open('csv/entregas.csv', 'w', newline='') as delivery_csv:
            writer_csv = csv.writer(delivery_csv)

            writer_csv.writerows(lines_csv)

    
    def search_start(line):
        lines_csv = []
        with open('csv/entregas.csv', 'r') as delivery_csv:
            reader_csv = csv.reader(delivery_csv)
            for linha in reader_csv:
                lines_csv.append(linha)
            
            return lines_csv[line][4]
        

    def search_end(line):
        lines_csv = []
        with open('csv/entregas.csv', 'r') as delivery_csv:
            reader_csv = csv.reader(delivery_csv)
            for linha in reader_csv:
                lines_csv.append(linha)
            
            return lines_csv[line][5]
