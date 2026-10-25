#Stworzyć klasy z polami: Library, Employee, Book, Order
#Każda z klas ma mieć zaimplementowaną metodę __str__
#pola zdefinowane jako atrybuty ustawiane podczas tworzenia instancji klasy za pośrednictwem konstruktora
#Stworzyć 2 instancje klas Biblioteka, 5 Ksiązka, 3 Pracownicy, 3 Studenci oraz 2 zamówienia
#Wyświetlić oba zamówienia

from zad1 import Student, student1


class Library:
    def __init__(self, city, street, zip_code, open_hours:str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return (f'Biblioteka w {self.city} przy ul. {self.street}, kod pocztowy {self.zip_code},'
                f'godziny otwarcia {self.open_hours}, nr telefonu {self.phone}')

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self) -> str:
        return (f'Pracownik {self.first_name} {self.last_name}, zatrudniony {self.hire_date},'
                f'data urodzenia {self.birth_date}, adres zamieszkania: {self.zip_code} {self.city}, ul. {self.street},'
                f' numer telefonu: {self.phone}')

class Book:
    def __init__(self, library: Library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return (f'Książka w {self.library}, opublikowana {self.publication_date},'
                f'autorem jest {self.author_name} {self.author_surname}, ilość stron to {self.number_of_pages}')

class Order:
    def __init__(self, employee: Employee, student: Student, books:list[Book],order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        books_list_str = "\n".join([str(book) for book in self.books])
        return (
            f'Zamówienie z dnia {self.order_date}\n'
            f'Obsługujący: {self.employee}\n'
            f'Zamawiający: {self.student}\n'
            f'Zamówione książki: {books_list_str}\n'
        )

library1 = Library("Katowice","Mariacka", "44-200", "8-20", "225566")
library2 = Library("Warszawa","Katowicka", "00-121", "7-15", "237866")
book1 = Book(library1, publication_date="2021-09-01", author_name="Jan", author_surname="Kowalski", number_of_pages=300)
book2 = Book(library1, publication_date="1999-12-17", author_name="Katarzyna", author_surname="Nowak", number_of_pages=76)
book3 = Book(library2, publication_date="2003-05-12", author_name="Artur", author_surname="Baran", number_of_pages=156)
book4 = Book(library2, publication_date="2020-01-08", author_name="Magdalena", author_surname="Iksińska", number_of_pages=284)
book5 = Book(library2, publication_date="2025-10-10", author_name="Michał", author_surname="Kowal", number_of_pages=320)
employee1 = Employee("Agata", "Kowalska", "2020-10-10", "1975-05-24", "Łódź", "Złota", "15-134", "607889666")
employee2 = Employee("Jacek", "Laptop", "2021-12-17", "1976-05-24", "Warszawa", "Warszawska", "00-001", "55566677")
employee3 = Employee("Jerzy", "Monitor", "2019-02-02", "1977-05-24", "Katowice", "Polna", "42-890", "245376777")
order1 =  Order(employee = employee1, student = student1, books = [book1, book2, book3], order_date = "2021-09-01")
order2  = Order(employee = employee3, student = student1, books = [book4, book5], order_date = "2020-09-01")

print(order1)
print(order2)