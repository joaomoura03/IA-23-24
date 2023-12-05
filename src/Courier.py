from Csvfunction import Csvfunction

from pydantic import BaseModel

class Courier(BaseModel):
    def __init__(self, name, classification, total):
        self._name = name
        self._classification = classification
        self._total = total


    def __str__(self):
        return [self._name, self._total, self._number]

    def get_name(self):
        return self._name
    
    def get_location(self):
        return self._location
    
    
    def set_name(self, name):
        self._name = name

    def set_location(self, location):
        self._location = location

    def set_total(self, total):
        self._total = total
    
    def set_classification(self, classification):
        self._classification = classification

    def classificate(self, rating):
        self._total += 1
        self._classification += rating
    
    def hash_to_courier(hash, key):
        for keys, values in hash.items():
            if keys == key:
                courier = Courier(key)
        return courier
    

class CourierCatalog(BaseModel):
    couriers: dict[str, Courier] = {}

    # def __init__(self,path):
    #     self.load(path)

    def add(self, *, c: Courier):
        self.courier[c._name] = c

    def print(self):
        for name, courier in self.courier.items():
            print(f"Name: {name}, Classification: {courier._classification}, Total: {courier._total}, Number: {courier._number}")

    def create_courier(self, name, classification, total):
        c = Courier(name, classification, total)
        self.couriers[name] = c

    def load(self, file_path):
        with open(file_path, mode="r", encoding="utf-8") as fp:
            self.couriers = CourierCatalog.model_dump_json(fp.read)
    
    def save(self, file_path):
        with open(file_path, mode="w", encoding="utf-8") as fp:
            fp.write(self.couriers.model_dump_json())