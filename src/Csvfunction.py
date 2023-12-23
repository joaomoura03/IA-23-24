class Csvfunction:
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
    
