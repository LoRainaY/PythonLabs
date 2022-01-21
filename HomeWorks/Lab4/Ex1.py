class Airline:
    __destination = 'London'  # статическое закрытое поле
    description = 'Destination: '

    def setDestination(self, destination):  # сеттер для поля объекта
        self.__destination = destination

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

    def __init__(self, flightNumber, aircraftType, departureTime, daysOfWeek):  # динамические поля
        self.flightNumber = flightNumber
        self.aircraftType = aircraftType
        self.departureTime = departureTime
        self.daysOfWeek = daysOfWeek


flight1 = Airline('AF 3535', 'Airbus', '12:40', 'MON, WED, FRI, SUN')
flight2 = Airline('R4 4625', 'Boeing', '10:10', 'MON, FRI, SUN')

flight1.setDestination('New York')  # вызов сеттера через экзямпляр класса (объект)
Airline.setDestination(flight2, 'Moscow')  # вызов сеттера через класс с обяз. указанием объекта

Airline.helloWorld(flight1)  # через класс с обяз. указанием объекта
flight2.helloWorld()  # способ 2 через объект напрямую

print(flight1.__dict__)  # вывод всех динамических полей
# print(flight1.__destination)  - ошибка, поле закрыто
print(flight1.getDestination())  # New York
print('\n')
print(flight2.getDestination())  # Moscow
print('\n')
print(flight1.getDestinationStatic(), flight2.getDestinationStatic(), Airline.getDestinationStatic())
# London London London, выводит одинаковое значение поля у все лбъектов
print('\n')
Airline.printDestination()  # Destination: London
