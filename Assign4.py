from Flight import *
from Airport import *

# Creating dictionaries.
allAirports = {}
allFlights = {}

# Define code, city/origin, and country/destination.
CODE = 0
CITY = ORIGIN = 1
COUNTRY = DESTINATION = 2

def loadData(airportFile, flightFile):
    # Try to load data, if any error occurs return False. Otherwise, return True.
    try:
        file = open(airportFile, 'r')
        # Iterating through the lines in the file to remove any unneeded whitespace and to assigning them to dictionary keys and values.
        for a in file.readlines():
            a = a.split(",")
            airport = Airport(a[CODE].strip(), a[COUNTRY].strip(), a[CITY].strip())
            allAirports[airport.getCode()] = airport

        file.close()

        file = open(flightFile, 'r')
        # Iterating through the lines in the file to remove any unneeded whitespace and to split them into categories.
        for f in file.readlines():
            f = f.split(",")
            origin = f[ORIGIN].strip()
            destination = f[DESTINATION].strip()

            airports = allAirports.keys()
            # Raise type error if origin or destination not in airports.
            if origin not in airports or destination not in airports:
                raise TypeError
            # Remove any whitespace in the code section and create a flight format consisting of code, origin, and destination.
            flight = Flight(f[CODE].strip(), allAirports[origin], allAirports[destination])

            # Find airport code of origin.
            originAirportCode = flight.getOrigin().getCode()

            # Adding all necessary information into the allFlights dictionary.
            if originAirportCode not in allFlights.keys():
                allFlights[originAirportCode] = []

            allFlights[originAirportCode].append(flight)

        file.close()

        return True

    except:
        return False

def getAirportByCode(code):
    # If code is not in the allAirports dictionary keys return -1. Else, return allAirports[code].
    if code not in allAirports.keys():
        return -1
    return allAirports[code]

# Creating supporter function to find all airport flights.
def findAllAirportFlights(airports):
    # Create a result list.
    result = []

    # Add all the flights that leave that airport.
    for code in airports:
        if code in allFlights.keys():
            result = result + allFlights[code]

    # Add all the flights that arrive into the airport.
    for origin in allFlights.keys():
        for flight in allFlights[origin]:
            if flight.getDestination().getCode() in airports:
                result.append(flight)

    return result

def findAllCityFlights(city):
    # Create airports list.
    airports = []

    # Find all the airports in the selected city.
    for airport in allAirports.values():
        if city == airport.getCity():
            airports.append(airport.getCode())

    return findAllAirportFlights(airports)

def findAllCountryFlights(country):
    # Create airports list.
    airports = []

    # Find all the airports in the selected country.
    for airport in allAirports.values():
        if country == airport.getCountry():
            airports.append(airport.getCode())

    return findAllAirportFlights(airports)

# Creating a supporter function to find all flights which are the same as destAirport.
def findAllFlightsTo(origAirport, destAirport):
    # Create result list.
    result = []
    # Define code.
    code = origAirport.getCode()

    # Finding all flight destination codes that are the same as the destAirport code.
    for flight in allFlights[code]:
        if flight.getDestination().getCode() == destAirport.getCode():
            result.append(flight)

    return result

def findFlightBetween(origAirport, destAirport):
    # Direct flights from origin to destination.
    flights = findAllFlightsTo(origAirport, destAirport)
    # If direct flight is found return proper format of the flight. Else, continue.
    if len(flights):
        return "Direct Flight: %s to %s" % (flights[0].getOrigin().getCode(), flights[0].getDestination().getCode())

    # Create indirect list.
    indirect = []
    # Iterating through to find any indirect flights from origin to destination, if found they will be added to the indirect list.
    for origin in allFlights[origAirport.getCode()]:
        for flight in findAllFlightsTo(origin.getDestination(), destAirport):
            indirect.append(flight.getOrigin().getCode())

    # If no direct flights are found and an indirect flight was found return indirect. Else, return -1.
    if len(indirect):
        return set(indirect)

    return -1

def findReturnFlight(firstFlight):
    # Direct flights from destination to origin.
    flights = findAllFlightsTo(firstFlight.getDestination(), firstFlight.getOrigin())
    # If a return flight is found return flights[0], else return -1.
    if len(flights):
        return flights[0]

    return -1
