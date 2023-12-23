from Delivery import Delivery, DeliveryCatalog
from pydantic import BaseModel


class Delivered(BaseModel):
    id: int
    courier: str
    vehicle: str
    weight: int
    begining: str = 'Central'
    end: str
    time_user: int
    time_delivery: float
    classification: float


class DeliveredCatalog(BaseModel):
    delivered: dict[str, Delivered] = {}

    def load(file_path):
        with open(file_path, mode="r", encoding="utf-8") as fp:
            return DeliveredCatalog.model_validate_json(fp.read())
        
    
    def save(self, file_path):
        with open(file_path, mode="w", encoding="utf-8") as fp:
            fp.write(self.model_dump_json())

    
    def print(self):
        for id, delivered in self.delivered.items():
            print(f"ID: {id}, Courier: {delivered.courier}, Vehicle: {delivered.vehicle}, 
                  Weight: {delivered.weight}, Beginning: {delivered.begining}, End: {delivered.end}, 
                  Time User: {delivered.time_user}, Time Delivery: {delivered.time_delivery}, 
                  Classification: {delivered.classification}")