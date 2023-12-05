from Csvfunction import Csvfunction

from pydantic import BaseModel

class Courier(BaseModel):
    name: str
    classification: float
    total: int

    def __str__(self):
        return [self.name, self.total, self._number]

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def set_total(self, total):
        self.total = total
    
    def set_classification(self, classification):
        self.classification = classification

    def classificate(self, rating):
        self.total += 1
        self.classification += rating
    
    def hash_to_courier(hash, key):
        for keys, values in hash.items():
            if keys == key:
                courier = Courier(key)
        return courier
    

class CourierCatalog(BaseModel):
    couriers: dict[str, Courier] = {}

    def add(self, c: Courier):
        self.couriers[c.name] = c

    def print(self):
        for name, courier in self.couriers.items():
            print(f"Name: {name}, Classification: {courier.classification}, Total: {courier.total}, Number: {courier._number}")

    def load(file_path):
        with open(file_path, mode="r", encoding="utf-8") as fp:
            return CourierCatalog.model_validate_json(fp.read())
    
    def save(self, file_path):
        with open(file_path, mode="w", encoding="utf-8") as fp:
            fp.write(self.model_dump_json())