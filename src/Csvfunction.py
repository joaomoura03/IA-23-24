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
    def search_start(hash_delivery, key):
        return hash_delivery.get(key)[3]


    #Função que procura qual é o nodo onde acaba a entrega
    def search_end(hash_delivery, key):
        return hash_delivery.get(key)[4]


    #Função que calcula quanto tempo demorou a entrega a ser feita
    def time_of_travel(hash_delivery, key, distance):
        if hash_delivery.get(key)[1] == 'Bicicleta':
            final_time = (distance/(10 - 0.6 * float(hash_delivery.get(key)[2])))*60
        elif hash_delivery.get(key)[1] == 'Mota':
            final_time = (distance/(35 - 0.6 * float(hash_delivery.get(key)[2])))*60
        elif hash_delivery.get(key)[1] == 'Carro':
            final_time = (distance/(50 - 0.6 * float(hash_delivery.get(key)[2])))*60
        return final_time



    #Funçáo que pergunta qual rank deve dar ao estafeta e atualiza o seu ranking atual
    def rank_courier(hash_delivery, hash_ranking, key, rank_deduction, stars):
        courier = hash_delivery.get(key)[0]
        for key_ranking, values in hash_ranking.items():
            if key_ranking == courier:
                new_numero = float(values[2]) + float(stars) - float(rank_deduction)
                new_total = float(values[1]) + 1.0
                new_classificaçao = new_numero/new_total
        hash_ranking[courier][0] = new_classificaçao
        hash_ranking[courier][1] = new_total
        hash_ranking[courier][2] = new_numero

        return new_classificaçao


    #Função que verifica se o estafeta fez a entrega a tempo
    def check_time(line, time):
        with open("../csv/delivery.csv", 'r') as delivery_csv:
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
    def deliver(hash_delivery, hash_delivered, key, time, rank):
        for key_delivery, values in hash_delivery.items():
            if key_delivery == key:
                values.append(time)
                values.append(rank)
                hash_delivered[key_delivery] = values


    #Função que remove do csv a encomenda já entregue
    def remove_delivery(hash_delivery, key):
        hash_delivery.pop(key,None)

    
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
    

    def check_vehicle(hash_delivery, key):
        return hash_delivery.get(key)[1]