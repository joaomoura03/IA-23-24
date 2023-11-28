import csv


class Csvfunction:
    def load(file_path):
        hash = {}
        with open(file_path, 'r') as csv_file:
            reader_csv = csv.reader(csv_file)
            for row in reader_csv:
                key = row[0]
                values = row[1:]
                hash[key] = values
        return hash


    def save(file_path, hash):
        with open(file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for key, values in hash.items():
                csv_writer.writerow([key] + values)


    def print(hash):
        for name, values in hash.items():
            print([name] + values)


    #Função que procura qual é o nodo onde começa a entrega
    def search_start(line):
        with open('csv/delivery.csv', 'r') as delivery_csv:
            reader_csv = csv.reader(delivery_csv)
            for row in reader_csv:
                if row[0] == line:
                    line_row = row[4]
                    return line_row


    #Função que procura qual é o nodo onde acaba a entrega
    def search_end(line):
        with open('csv/delivery.csv', 'r') as delivery_csv:
            reader_csv = csv.reader(delivery_csv)
            for row in reader_csv:
                if row[0] == line:
                    line_row = row[5]
                    return line_row


    #Função que calcula quanto tempo demorou a entrega a ser feita
    def time_of_travel(line, distance):
        with open('csv/delivery.csv', 'r') as delivery_csv:
            reader_csv = csv.reader(delivery_csv)
            for row in reader_csv:
                if row[0] == line:
                    if row[2] == 'Bicicleta':
                        final_time = (distance/(10 - 0.6 * float(row[3])))*60
                        return final_time

                    if row[2] == 'Mota':
                        final_time = (distance/(35 - 0.5 * float(row[3])))*60
                        return final_time

                    if row[2] == 'Carro':
                        final_time = (distance/(50 - 0.1 * float(row[3])))*60
                        return final_time


    #Funçáo que pergunta qual rank deve dar ao estafeta e atualiza o seu ranking atual
    def rank_courier(line, rank_deduction):
        with open('csv/delivery.csv', 'r') as delivery_csv:
            reader_delivery_csv = csv.reader(delivery_csv)
            for row in reader_delivery_csv:
                if row[0] == line:
                    courier = row[1]

        with open("csv/ranking.csv", 'r') as ranking_csv:
            reader_ranking_csv = csv.reader(ranking_csv)
            data = list(reader_ranking_csv)
            i = 0
            for row in data:
                if row[0] == courier:
                    stars = float(input("\nIndique de 0 a 5 a qualidade da entrega: "))
                    new_numero = float(row[3]) + stars - rank_deduction
                    new_total = float(row[2]) + 1.0
                    new_classificaçao = new_numero/new_total
                    row = [courier, new_classificaçao, new_total, new_numero]
                    data[i] = row
                i += 1

        with open("csv/ranking.csv", 'w') as ranking_csv:
            writer_csv = csv.writer(ranking_csv)
            writer_csv.writerows(data)
        
        return new_classificaçao

    
    #Função que verifica se o estafeta fez a entrega a tempo
    def check_time(line, time):
        with open("csv/delivery.csv", 'r') as delivery_csv:
            reader_delivery_csv = csv.reader(delivery_csv)
            for row in reader_delivery_csv:
                if row[0] == line:
                    if int(row[6]) >= time:
                        print("\nO estafeta fez a entrega a tempo")
                        return True
                    else:
                        print("\nO estafeta não fez a entrega a tempo")
                        print("O estafeta terá uma dedução automática no seu ranking")
                        return False
                    
    
    #Função que passa uma encomenda de por fazer para feita
    def deliver(line, time, rank):
        line_delivered = []
        with open("csv/delivery.csv", 'r') as delivery_csv:
            reader_delivery_csv = csv.reader(delivery_csv)
            for row_delivery in reader_delivery_csv:
                if row_delivery[0] == line:
                    line_delivered = row_delivery

        line_delivered.append(time)
        line_delivered.append(rank)

        with open("csv/delivered.csv", 'a', newline='\n') as delivered_csv:
            writer_delivered_csv = csv.writer(delivered_csv)
            writer_delivered_csv.writerow(line_delivered)


    #Função que remove do csv a encomenda já entregue
    def remove_delivery(line):
        with open ("csv/delivery.csv", 'r', newline='') as delivery_csv:
            data = list(csv.reader(delivery_csv))

        del data[int(line)]

        with open("csv/delivery.csv", 'w', newline='') as delivery_csv:
            csv.writer(delivery_csv).writerows(data)

    
    def co2_emission(distance, vehicle):
        if vehicle == "Carro":
            gasol = distance/14
            co2_carro = gasol*2.3
            return co2_carro
        elif vehicle == "Moto":
            gasol = distance/25
            co2_mota = gasol*0.1
            return co2_mota
        elif vehicle == "Bicicleta":
            co2_bicicleta = distance*0.001
            return co2_bicicleta
    

    def check_vehicle(line):
        with open("csv/delivery.csv", 'r') as delivery_csv:
            data = list(csv.reader(delivery_csv))
            for row in data:
                if row[0] == line:
                    return row[2]