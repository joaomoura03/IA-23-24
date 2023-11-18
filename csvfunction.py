import csv


class csvfunction:

    def altera_tempo(line):
        #Imprime linha a alterar
        with open('csv/entregas.csv', 'r') as entrega_csv:
            leitor_csv = csv.reader(entrega_csv)
            for current_line_number, row in enumerate(entrega_csv, start=0):
                if current_line_number == line:
                    print(f"Line {line}: {row}")
        
        #Altera o tempo
        tempo = int(input("Introduza o tempo limite do estafeta"))
        linhas_csv = []
        with open('csv/entregas.csv', 'r') as entrega_csv:
            leitor_csv = csv.reader(entrega_csv)
            for linha in leitor_csv:
                linhas_csv.append(linha)
        if 0 < line <= len(linhas_csv):
            linhas_csv[line][6] = str(tempo)
        else:
            print(f"Linha {line} não existe no arquivo CSV.")

        with open('csv/entregas.csv', 'w', newline='') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)

            escritor_csv.writerows(linhas_csv)
