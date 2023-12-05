import random
import csv

from Csvfunction import Csvfunction
from pydantic import BaseModel


class Delivery(BaseModel):
    id: int
    courier: str
    vehicle: str
    weight: int
    begining: str = 'Central'
    end: str
    time: int

    def __str__(self):
        return[self.id, self.courier, self.vehicle, self.weight, self.begining, self.end, self.time]

    def get_id(self):
        return self.id
    
    def get_courier(self):
        return self.courier
    
    def get_vehicle(self):
        return self.vehicle

    def get_weight(self):
        return self.weight

    def get_begining(self):
        return self.begining

    def get_end(self):
        return self.end

    def get_time(self):
        return self.time
    
    def set_id(self, id):
        self.id = id

    def set_courier(self, courier):
        self.courier = courier

    def set_vehicle(self, vehicle):
        self.vehicle = vehicle

    def set_weight(self, weight):
        self.weight = weight

    def set_begining(self, begining):
        self.begining = begining

    def set_end(self, end):
        self.end = end

    def set_time(self, time):
        self.time = time


    #Função que cria uma encomenda
    def new_delivery(id: int, cc, weight, end, time):
        list_of_couriers = list(cc.couriers.keys())

        if weight <= 5:
            vehicle = "Bicicleta"
        elif 5 < weight <= 20:
            vehicle = "Mota"
        elif 20 < weight <= 100:
            vehicle = "Carro"
        # courier nao tem que estar disponivel? de resto ta
        return Delivery(
            id=id,
            courier=random.choice(list_of_couriers),
            vehicle=vehicle,
            weight=weight,
            end=end,
            time=time
        )

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

    def add(self, *, d: Delivery):
        self.deliveries[d.id] = d

    def print(self):
        # for _id, delivery in self.deliveries.items():
        #     print(f"ID: {_id}, Courier: {delivery.courier}, Vehicle: {delivery.vehicle}, Weight: {delivery.weight}, Beginning: {delivery.begining}, End: {delivery.end}, Time: {delivery.time}")
        print(self.deliveries)

    def create_delivery(self, cc, weight, end, time):
        keys = list(self.deliveries.keys())
        if len(keys) == 0:
            id = 1
        else:
            id = keys[-1] + 1
        self.deliveries[id] = Delivery.new_delivery(id, cc, weight, end, time)

    def load(file_path):
        with open(file_path, mode="r", encoding="utf-8") as fp:
            return DeliveryCatalog.model_validate_json(fp.read())

    def save(self, file_path):
        with open(file_path, mode="w", encoding="utf-8") as fp:
            fp.write(self.model_dump_json())