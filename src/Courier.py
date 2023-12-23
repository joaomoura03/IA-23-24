from pydantic import BaseModel

class Courier(BaseModel):
    name: str
    number: float
    total: float
    classification: float

    def __str__(self):
        return [self.name, self.total, self.total]

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
    

class CourierCatalog(BaseModel):
    couriers: dict[str, Courier] = {}


    def add(self, c: Courier):
        self.couriers[c.name] = c


    def print(self):
        for name, courier in self.couriers.items():
            print(f"Name: {name}, Classification: {courier.classification}, Total: {courier.total}, Number: {courier.total}")


    def load(file_path):
        with open(file_path, mode="r", encoding="utf-8") as fp:
            return CourierCatalog.model_validate_json(fp.read())
    

    def save(self, file_path):
        with open(file_path, mode="w", encoding="utf-8") as fp:
            fp.write(self.model_dump_json())


    def get_courier_by_name(self, name):
        return self.couriers.get(name, None)
    
    
    def rank_courier(self, rank_deduction, stars, name):
        new_number = self.couriers[name].number + float(stars) - rank_deduction
        new_total = self.couriers[name].total + 1.0
        new_classification = new_number/new_total

        courier = self.get_courier_by_name(name)

        courier.number = new_number
        courier.total = new_total
        courier.classification = new_classification
        self.couriers[name] = courier