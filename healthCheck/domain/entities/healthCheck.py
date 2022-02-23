class HealthCheckEntity:
    def __init__(self, timestamp=None):
        self._timestamp = timestamp

    @property
    def timestamp(self):
        return self._timestamp

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
