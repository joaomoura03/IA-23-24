import random
from pydantic import BaseModel

BASE_PRICE = 25
CONSUME_CAR_BY_METER = 0.000068
CONSUME_BIKE_BY_METER = 0.000034
PRICE_GASOLINE = 1.704

class Delivery(BaseModel):
    id: int
    courier: str
    vehicle: str
    weight: int
    begining: str = 'Central'
    end: str
    time: int
    client: str

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
    def new_delivery(id: int, cc, weight, end, time, client):
        list_of_couriers = list(cc.couriers.keys())

        if weight <= 5:
            vehicle = "Bicicleta"
        elif 5 < weight <= 20:
            vehicle = "Mota"
        elif 20 < weight <= 100:
            vehicle = "Carro"
        return Delivery(
            id=id,
            courier=random.choice(list_of_couriers),
            vehicle=vehicle,
            weight=weight,
            end=end,
            time=time,
            client=client
        )


class DeliveryCatalog(BaseModel):
    deliveries: dict[str, Delivery] = {}

    def print(self):
        for _id, delivery in self.deliveries.items():
            print(f"ID: {_id}, Courier: {delivery.courier}, Vehicle: {delivery.vehicle}, Weight: {delivery.weight}, Beginning: {delivery.begining}, End: {delivery.end}, Time: {delivery.time}, Client: {delivery.client}")


    def create_delivery(self, cc, weight, end, time, client):
        keys = list(self.deliveries.keys())
        if len(keys) == 0:
            id = "1"
        else:
            id = str(int(keys[-1]) + 1)
        self.deliveries[id] = Delivery.new_delivery(id, cc, weight, end, time, client)


    def load(file_path):
        with open(file_path, mode="r", encoding="utf-8") as fp:
            return DeliveryCatalog.model_validate_json(fp.read())


    def save(self, file_path):
        with open(file_path, mode="w", encoding="utf-8") as fp:
            fp.write(self.model_dump_json())


    #Função que procura qual é o nodo onde começa a entrega
    def start_d(self, key):
        return self.deliveries[str(key)].begining


    #Função que procura qual é o nodo onde acaba a entrega
    def end_d(self, key):
        return self.deliveries[str(key)].end
    

    #Função que calcula quanto tempo demorou a entrega a ser feita
    def time_of_travel(self, key, distance):
        if self.deliveries[str(key)].vehicle == 'Bicicleta':
            final_time = (distance/(10 - 0.6 * float(self.deliveries[str(key)].weight)))*60
        elif self.deliveries[str(key)].vehicle == 'Mota':
            final_time = (distance/(35 - 0.5 * float(self.deliveries[str(key)].weight)))*60
        elif self.deliveries[str(key)].vehicle == 'Carro':
            final_time = (distance/(50 - 0.1 * float(self.deliveries[str(key)].weight)))*60
        return final_time
    

    #Função que verifica se o estafeta fez a entrega a tempo
    def check_time(self, key, time):
        if float(self.deliveries[str(key)].time) >= time:
            print("\nO estafeta fez a entrega a tempo")
            return True
        else:
            print("\nO estafeta não fez a entrega a tempo")
            print("O estafeta terá uma dedução automática no seu ranking")
            return False
        

    def check_vehicle(self, key):
        return self.deliveries[str(key)].vehicle
    

    def remove_delivery(self, key):
        del self.deliveries[str(key)]


    def get_courier_c(self, key):
        return self.deliveries[str(key)].courier
    

    def get_client_c(self, key):
        return self.deliveries[str(key)].client
    

    def remove_and_get(self, key) -> Delivery:
        return self.deliveries.pop(key, None)
    

    def make_more_deliveries(self, key):
        new_keys = []
        new_keys.append(key)
        if self.deliveries[key].vehicle == "Bicicleta":
            weight_original = self.deliveries[key].weight
            if weight_original < 5:
                for key_new_delivery, delivery in self.deliveries.items():
                    if delivery.vehicle == "Bicicleta" and delivery.weight + weight_original <= 5 and key != key_new_delivery:
                        weight_original = weight_original + delivery.weight
                        new_keys.append(key_new_delivery)

        elif self.deliveries[key].vehicle == "Mota":
            weight_original = self.deliveries[key].weight
            if weight_original < 20:
                for key_new_delivery, delivery in self.deliveries.items():
                    if delivery.vehicle == "Mota" and delivery.weight + weight_original <= 20 and key != key_new_delivery:
                        weight_original = weight_original + delivery.weight
                        new_keys.append(key_new_delivery)

        elif self.deliveries[key].vehicle == "Carro":
            weight_original = self.deliveries[key].weight
            if weight_original < 100:
                for key_new_delivery, delivery in self.deliveries.items():
                    if delivery.vehicle == "Carro" and delivery.weight + weight_original <= 100 and key != key_new_delivery:
                        weight_original = weight_original + delivery.weight
                        new_keys.append(key_new_delivery)
        
        new_keys_int = sorted(list(map(int,(list(set(new_keys))))))
        print(f"\nO estafeta vai fazer estas encomendas {new_keys_int}")
        new_keys_str = list(map(str,new_keys_int))
        return new_keys_str


    def change_start(self, key, new_start):
        self.deliveries[str(key)].begining = new_start

    
    def change_courier(self, key, new_courier):
        self.deliveries[str(key)].courier = new_courier


    def next_list(self, list):
        for i in list:
            if int(i) < int(len(list)):
                return list[i+1]
            
        
    def price_delivery(self, key, distance):
        if self.deliveries[str(key)].vehicle == "Bicicleta":
            price = BASE_PRICE + 0.2 * distance
        elif self.deliveries[str(key)].vehicle == "Mota":
            price = BASE_PRICE + (distance * CONSUME_BIKE_BY_METER) * PRICE_GASOLINE
        elif self.deliveries[str(key)].vehicle == "Carro":
            price = BASE_PRICE + (distance * CONSUME_CAR_BY_METER) * PRICE_GASOLINE
        print(f"A viagem custou {price}$")
        return price
    

    def co2_emission(distance, vehicle):
        if vehicle == "Carro":
            gasol = distance/14
            co2_carro = gasol*2.3
            return co2_carro
        elif vehicle == "Mota":
            gasol = distance/25
            co2_mota = gasol*0.1
            return co2_mota
        elif vehicle == "Bicicleta":
            co2_bicicleta = distance*0.001
            return co2_bicicleta