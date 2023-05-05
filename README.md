# Flight-Search-System
This project is a flight search system that allows users to find flights between airports based on origin, destination, city, or country. The system uses Python classes to create Airport and Flight objects and dictionaries to store all airports and flights. The data is loaded from text files, and the user can search for flights using various functions.

## Skills Learned
- Object-oriented programming in Python
- Class creation and object representation
- File input/output operations
- Dictionary data structures and manipulation
- Error handling and exception raising

## Usage
- Load data from text files using the '**loadData()**' function
- Find all flights leaving or arriving at a specific airport using the '**findAllAirportFlights()**' function
- Find all flights departing from or arriving in a specific city or country using the '**findAllCityFlights()**' and '**findAllCountryFlights()**' functions, respectively
- Find flights between two airports using the '**findFlightBetween()**' function
- Find the return flight for a given flight using the '**findReturnFlight()**' function

## Constants
- '**CODE**': integer representing the airport code in the input text file
- '**CITY**': integer representing the airport city in the input text file
- '**COUNTRY**': integer representing the airport country in the input text file

## Functions
- '**loadData(airportFile, flightFile)**': loads airport and flight data from text files
- '**getAirportByCode(code)**': returns the Airport object for a given airport code
- '**findAllAirportFlights(airports)**': returns a list of all flights departing from or arriving at a list of airports
- '**findAllCityFlights(city)**': returns a list of all flights departing from or arriving in a specific city
- '**findAllCountryFlights(country)**': returns a list of all flights departing from or arriving in a specific country
- '**findFlightBetween(origAirport, destAirport)**': returns a set of all flights between two airports
- '**findReturnFlight(firstFlight)**': returns the return flight for a given Flight object

## Limitations
- The program doesn't handle errors or exceptions gracefully. It simply returns an error message or -1 when an error occurs.
- The program doesn't provide any user interface or graphical output. It can only be used by calling its functions directly from Python code.

## Possible Improvements
- Add support for connecting flights
- Create a user interface for easier search and input
- Implement a database system to store and manage data more efficiently

## Conclusion
This project demonstrates the use of object-oriented programming, data structures, and error handling in a flight search system. It allowed me to practice my Python skills and learn more about handling large datasets and creating efficient search algorithms.
