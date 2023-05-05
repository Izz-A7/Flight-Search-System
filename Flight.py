from Airport import *

class Flight:
    # Initialize variables if origin and destination are Airport objects, else raise a type error.
    def __init__(self, flightNo, origin, destination):
        if isinstance(origin, Airport) and isinstance(destination, Airport):
            self._flightNo = flightNo
            self._origin = origin
            self._destination = destination
        else:
            raise TypeError("The origin and destination must be Airport objects")

    # Create object representation return.
    def __repr__(self):
        flightType = "International"
        if self.isDomesticFlight():
            flightType = "Domestic"

        return "Flight: %s from %s to %s {%s}" % (self._flightNo, self._origin.getCity(), self._destination.getCity(), flightType)

    # Create equality function to compare two objects.
    def __eq__(self, other):
        if isinstance(other, Flight) and \
                self._origin == other.getOrigin() and \
                self._destination == other.getDestination():
            return True
        return False

    # Create getter functions.
    def getFlightNumber(self):
        return self._flightNo
    def getOrigin(self):
        return self._origin
    def getDestination(self):
        return self._destination

    # Create domestic flight function.
    def isDomesticFlight(self):
        # Creating a boolean to return True if the origin country and destination country are the same, else False.
        if self._origin.getCountry() == self._destination.getCountry():
            return True
        else:
            return False

    # Create setter functions.
    def setCity(self, origin):
        self._origin = origin
    def setCountry(self, destination):
        self._destination = destination
