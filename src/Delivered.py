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
    client: str
    time_delivery: float
    classification: float
    classification_given: float


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
            print(f"ID: {id}, Courier: {delivered.courier}, Vehicle: {delivered.vehicle}, Weight: {delivered.weight}, Beginning: {delivered.begining}, End: {delivered.end}, Time User: {delivered.time_user},Client: {delivered.client}, Time Delivery: {delivered.time_delivery}, Classification: {delivered.classification}")

    
    def deliver(self, key: str, time_delivery: float, classification: float, delivered_delivery: Delivery, classification_given: float, name: float):
        if delivered_delivery:
            new_delivered = Delivered(
                id=delivered_delivery.id,
                courier=delivered_delivery.courier,
                vehicle=delivered_delivery.vehicle,
                weight=delivered_delivery.weight,
                begining=delivered_delivery.begining,
                end=delivered_delivery.end,
                time_user=delivered_delivery.time,
                client=name,
                time_delivery=time_delivery,
                classification=classification,
                classification_given=classification_given
            )

            self.delivered[key] = new_delivered
            return new_delivered
        else:
            return None
