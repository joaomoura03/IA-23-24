import random
import csv

from Csvfunction import Csvfunction
from pydantic import BaseModel


class Delivery(BaseModel):
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
    def new_delivery(id: int, cc, weight, end, time):
        list_of_couriers = list(cc.keys())[1:]

        if weight <= 5:
            vehicle = "Bicicleta"
        elif 5 < weight <= 20:
            vehicle = "Mota"
        elif 20 < weight <= 100:
            vehicle = "Carro"
        # courier nao tem que estar disponivel? de resto ta
        return Delivery(id, random.choice(list_of_couriers), vehicle, weight, end, time)

    def hash_to_delivery(dc, key):
        for keys, values in dc.items():
            if keys == key:
                delivery = Delivery(keys, values[0], values[1], values[2], values[4], values[5])
        return delivery
    

    #Função que procura qual é o nodo onde começa a entrega
    def search_start(dc, key):
        delivery = Delivery.hash_to_delivery(dc, key)
        return delivery.get_begining()
    

    #Função que procura qual é o nodo onde acaba a entrega
    def search_end(dc, key):
        delivery = Delivery.hash_to_delivery(dc, key)
        return delivery.get_end()


    #Função que calcula quanto tempo demorou a entrega a ser feita
    def time_of_travel(dc, key, distance):
        delivery = Delivery.hash_to_delivery(dc, key)
        if delivery.get_vehicle() == 'Bicicleta':
            final_time = (distance/(10 - 0.6 * float(dc.get(key)[2])))*60
        elif delivery.get_vehicle() == 'Mota':
            final_time = (distance/(35 - 0.5 * float(dc.get(key)[2])))*60
        elif delivery.get_vehicle() == 'Carro':
            final_time = (distance/(50 - 0.1 * float(dc.get(key)[2])))*60
        return final_time
    

    def check_vehicle(dc, key):
        return dc.get(key)[1]
    
    
    #Função que verifica se o estafeta fez a entrega a tempo
    def check_time(dc, key, time):
        if float(dc.get(key)[5]) >= time:
            print("\nO estafeta fez a entrega a tempo")
            return True
        else:
            print("\nO estafeta não fez a entrega a tempo")
            print("O estafeta terá uma dedução automática no seu ranking")
            return False
    

class DeliveryCatalog(BaseModel):
    deliveries: dict[int, Delivery] = {}
    
    # def __init__(self, path):
    #     self.load(path)

    def add(self, *, d: Delivery):
        self.deliveries[d._id] = d

    def load(self, file_path):
        with open(file_path, 'r') as csv_file:
            reader_csv = csv.DictReader(csv_file)
            for row in reader_csv:
                delivery = Delivery (                    
                id=int(row['Id']),
                courier=row['Estafeta'],
                vehicle=row['Transporte'],
                weight=int(row['Peso']),
                end=row['Fim'],
                time=int(row['Tempo Limite']))
                self.add(delivery)

    def print(self):
        # for _id, delivery in self.deliveries.items():
        #     print(f"ID: {_id}, Courier: {delivery._courier}, Vehicle: {delivery._vehicle}, Weight: {delivery._weight}, Beginning: {delivery._begining}, End: {delivery._end}, Time: {delivery._time}")
        print(self.deliveries)

    def create_delivery(self, cc, weight, end, time):
        id = list(self.deliveries.keys())[-1] + 1
        self.deliveries[id] = Delivery.new_delivery(id, cc, weight, end, time)

    def load(self, file_path):
        with open(file_path, mode="r", encoding="utf-8") as fp:
            self.couriers = DeliveryCatalog.model_dump_json(fp.read)

    def save(self, file_path):
        with open(file_path, mode="w", encoding="utf-8") as fp:
            fp.write(self.deliveries.model_dump_json())