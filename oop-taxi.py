
class Taxi:
    ''' This class describes how a taxi may look like '''
    def __init__ (self, driverName, onDuty, cities):
        self.dname = driverName
        self.oduty = onDuty
        self.cities = cities
        self.__numPassengers = 0
    def changeDriverName(self, driverName):
        self.dname = driverName
    def pickupPassengers(self, numPassengers):
        self.__numPassengers += numPassengers
    def dropOffPassenger(self):
        self.__numPassengers += -1 


ourFirstTaxi = Taxi("Aleks", True, ['Lund', 'Malmo'])
print (ourFirstTaxi.cities)

ourFirstTaxi.changeDriverName("Hamed")
print (ourFirstTaxi.dname)

ourFirstTaxi.pickupPassengers(3)
#print(ourFirstTaxi.numPassengers)

ourFirstTaxi.dropOffPassenger()
ourFirstTaxi.dropOffPassenger()
#print(ourFirstTaxi.numPassengers)

ourFirstTaxi.__numPassengers = 100


# Do this scenario
## Taxi picks up three passengers
## print current number of passengers
## Taxi drops two passengers
## print current number of passengers



