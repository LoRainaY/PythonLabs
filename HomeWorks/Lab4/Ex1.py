class Airline:
    __destination = 'London'  # статическое закрытое поле
    description = 'Destination: '

    def __setattr__(self, destination, message):  # сеттер для поля объекта
        if destination is None:
            self.__destination = message

    def __str__(self):
        return self

    def getDestination(self):  # геттер для вывод значения поля
        return self.__destination

    def helloWorld(self):  # метод объекта
        print('Hello OOP programming!')

    @classmethod  # метод класса
    def printDestination(cls):
        print(f"{cls.description}{cls.__destination}")

    @staticmethod  # статический метод
    def getDestinationStatic():
        return Airline.__destination

    def __int__(self, daysOfWeek):
        self.daysOfWeek = daysOfWeek

    def __init__(self, flightNumber, aircraftType, departureTime, daysOfWeek):  # динамические поля
        self.flightNumber = flightNumber
        self.aircraftType = aircraftType
        self.departureTime = departureTime
        self.daysOfWeek = daysOfWeek


flight1 = Airline('AF 3535', 'Airbus', '12:40', 'MON, WED, FRI, SUN')
flight2 = Airline('R4 4625', 'Boeing', '10:10', 'MON, FRI, SUN')

flight1.__setattr__('New York', 'Unknown')  # вызов сеттера через экзямпляр класса (объект)
Airline.__setattr__(flight2, 'Moscow', 'Unknown')  # вызов сеттера через класс с обяз. указанием объекта

Airline.helloWorld(flight1)  # через класс с обяз. указанием объекта
flight2.helloWorld()  # способ 2 через объект напрямую

# print(flight1.__destination)  - ошибка, поле закрыто
print(flight1.getDestination())  # New York
print('\n')
print(flight2.getDestination())  # Moscow
print('\n')
# London London London, выводит одинаковое значение поля у всех бъектов
print('\n')
Airline.printDestination()  # Destination: London

print(str(flight1.getDestination().__add__(flight2.getDestination())))
# т.к. __destination статическая, то дважды его значение будет выведено

