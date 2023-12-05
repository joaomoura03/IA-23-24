import csv



class Csvfunction:



    def save(file_path, hash):
        with open(file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for key, values in hash.items():
                csv_writer.writerow([key] + values)


    def print(hash):
        for name, values in hash.items():
            print([name] + values)


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

                    
    
    #Função que passa uma encomenda de por fazer para feita
    def deliver(hash_delivery, hash_delivered, key, time, rank):
        for key_delivery, values in hash_delivery.items():
            if key_delivery == key:
                values.append(time)
                values.append(rank)
                hash_delivered[key_delivery] = values
                hash_delivery.pop(key,None)
                break
    

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
    
