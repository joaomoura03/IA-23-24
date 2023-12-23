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


    def add(self, d: Delivered):
        