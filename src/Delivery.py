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
        return[self._id, self._courier, self._vehicle, self._weight, self._begining, self._end, self._time]

    def get_id(self):
        return self._id
    
    def get_courier(self):
        return self._courier
    
    def get_vehicle(self):
        return self._vehicle

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

    def set_courier(self, courier):
        self._courier = courier

    def set_vehicle(self, vehicle):
        self._vehicle = vehicle

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
        list_of_couriers = list(hash_ranking.keys())[1:]
        last_key = list(hash_delivery.keys())[-1]

        if weight <= 5:
            new_delivery = Delivery(int(last_key) + 1, random.choice(list_of_couriers), 'Bicicleta', weight, end, time)

        elif 5 < weight <= 20:
            new_delivery = Delivery(int(last_key) + 1, random.choice(list_of_couriers), 'Mota', weight, end, time)

        elif 20 < weight <= 100:
            new_delivery = Delivery(int(last_key) + 1, random.choice(list_of_couriers), 'Carro', weight, end, time)

        hash_delivery[new_delivery.get_id()] = new_delivery.__str__()[1:]


    def hash_to_delivery(hash_delivery, key):
        for keys, values in hash_delivery.items():
            if keys == key:
                delivery = Delivery(keys, values[0], values[1], values[2], values[4], values[5])
        return delivery
    

    #Função que procura qual é o nodo onde começa a entrega
    def search_start(hash_delivery, key):
        delivery = Delivery.hash_to_delivery(hash_delivery, key)
        return delivery.get_begining()
    

    #Função que procura qual é o nodo onde acaba a entrega
    def search_end(hash_delivery, key):
        delivery = Delivery.hash_to_delivery(hash_delivery, key)
        return delivery.get_end()


    #Função que calcula quanto tempo demorou a entrega a ser feita
    def time_of_travel(hash_delivery, key, distance):
        delivery = Delivery.hash_to_delivery(hash_delivery, key)
        if delivery.get_vehicle() == 'Bicicleta':
            final_time = (distance/(10 - 0.6 * float(hash_delivery.get(key)[2])))*60
        elif delivery.get_vehicle() == 'Mota':
            final_time = (distance/(35 - 0.5 * float(hash_delivery.get(key)[2])))*60
        elif delivery.get_vehicle() == 'Carro':
            final_time = (distance/(50 - 0.1 * float(hash_delivery.get(key)[2])))*60
        return final_time