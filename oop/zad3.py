#Stworzyć klasy property, House dziedziczące po property, Flat dziedziczące po Property
#każda klasa ma zaimplementowaną metodę __str__
#pola w klasie zdefiniowane jako atrybuty za pośr. konstruktora
#stworzyć i wyświetlić jeden obiekt House i Flat

class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self) -> str:
        return (f"Nieruchomość o powierzchni {self.area}, liczba pokoi {self.rooms},"
                f"cena wynosi {self.price} złotych. Adres nieruchomości to {self.address}")

class House(Property):
    def __init__(self, area, rooms: int, price, address, plot:int):
        super().__init__(area,rooms, price, address)
        self.plot = plot

    def __str__(self) -> str:
        base_info = super().__str__()
        return (f'{base_info} Powierzchnia działki wynosi {self.plot} m^2.')

class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area,rooms, price, address)
        self.floor = floor

    def __str__(self) -> str:
        base_info = super().__str__()
        return (f'{base_info} Mieszkanie znajduje się na {self.floor} piętrze.')

house1 = House (area = 100, rooms = 5, price = 2000000, address = 'Warszawa, Polna 17', plot = 800)
flat1 = Flat (area = 70, rooms = 3, price = 700000, address = 'Katowice, Mariacka 34/3', floor = 2 )
print(house1)
print(flat1)
