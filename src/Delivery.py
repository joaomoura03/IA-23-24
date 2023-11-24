class Delivery:

    def __init__(self, id, weight, begining, end, time):
        self._id = id
        self._weight = weight
        self._begining = begining
        self._end = end
        self._time = time

    def get_id(self):
        return self._id

    def get_weight(self):
        return self._weight

    def get_begining(self):
        return self._begining

    def get_end(self):
        return self._end

    def get_time(self):
        return self._time
    
    def set_id(self, id):
        self._id = id

    def set_weight(self, weight):
        self._weight = weight

    def set_begining(self, begining):
        self._begining = begining

    def set_end(self, end):
        self._end = end

    def set_time(self, time):
        self._time = time