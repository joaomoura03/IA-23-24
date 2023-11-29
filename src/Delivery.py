import random


class Delivery:
    def __init__(self, id, courier, vehicle, weight, end, time):
        self._id = id
        self._courier = courier
        self._vehicle = vehicle
        self._weight = weight
        self._begining = 'Central'
        self._end = end
        self._time = time

    def __str__(self):
        return[self._id, self._courier, self._vehicle, self._weight, self._end, self._time]

    def get_id(self):
        return self._id

    def get_weight(self):
        return self._weight

    def get_begining(self):
        return self._begining

    def get_end(self):
        return self._end

    def get_time(self):
        return self._time
    
    def set_id(self, id):
        self._id = id

    def set_weight(self, weight):
        self._weight = weight

    def set_begining(self, begining):
        self._begining = begining

    def set_end(self, end):
        self._end = end

    def set_time(self, time):
        self._time = time


    #Função que cria uma encomenda
    def create_delivery(hash_delivery, hash_ranking, weight, end, time):
        list_of_couriers = list(hash_ranking.keys())
        last_key = list(hash_delivery.keys())[-1]

        if weight <= 5:
            new_delivery = Delivery(int(last_key) + 1, random.choice(list_of_couriers), 'Bicicleta', weight, end, time)

        elif 5 < weight <= 20:
            new_delivery = Delivery(int(last_key) + 1, random.choice(list_of_couriers), 'Mota', weight, end, time)

        elif 20 < weight <= 100:
            new_delivery = Delivery(int(last_key) + 1, random.choice(list_of_couriers), 'Carro', weight, end, time)

        hash_delivery[new_delivery.get_id()] = new_delivery.__str__()[1:]

    
    #Função que procura qual é o nodo onde começa a entrega
    def search_start(hash_delivery, key):
        return hash_delivery[key].get_begining()
