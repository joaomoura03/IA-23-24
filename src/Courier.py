class Courier:
    def __init__(self, name, vehicle, location):
        self._name = name
        self._vehicle = vehicle
        self._location = location
        self._classification = 0
        self._total = 0
        self._number = 0


    def __str__(self):
        return f"Name: {self._name}\nVehicle: {self._vehicle}\nLocation: {self._location}\nClassification: {self._classification}\nTotal: {self._total}\nNumber: {self._number}"
    
    def get_name(self):
        return self._name

    def get_vehicle(self):
        return self._vehicle

    def get_location(self):
        return self._location
    
    def set_name(self, name):
        self._name = name

    def set_vehicle(self, vehicle):
        self._vehicle = vehicle


    def set_location(self, location):
        self._location = location