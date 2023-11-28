class Courier:
    def __init__(self, name):
        self._name = name
        self._classification = 0
        self._total = 0
        self._number = 0


    def __str__(self):
        return [self._name, self._classification, self._total, self._number]

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


    #Função que cria um estafeta
    def new_courier(hash, name):
        new_courier = Courier(name)
        hash[new_courier.get_name()] = new_courier.__str__()[1:]