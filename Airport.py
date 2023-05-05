class Airport:
    # Initialize variables.
    def __init__(self, code, city, country):
        self._code = code
        self._city = city
        self._country = country

    # Create object representation return.
    def __repr__(self):
        return "%s (%s, %s)" % (self._code, self._city, self._country)

    # Create getter functions.
    def getCode(self):
        return self._code
    def getCity(self):
        return self._city
    def getCountry(self):
        return self._country

    # Create setter functions.
    def setCity(self, city):
        self._city = city
    def setCountry(self, country):
        self._country = country
