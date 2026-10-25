# Stworzyć klasę Student, która posiada 2 parametry (name i marks) oraz jedną metodę is_passed, która zwraca wartość
# logiczną, pozytywną gdy średnia ocen jest > 50 w przeciwnym przypadku negatywną. Następnie należy stworzyć
# 2 przykładowe obiekty klasy, tak aby dla pierwszego obiektu metoda zwracała true , a dla drugiego false.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if not self.marks:
            return False

        average = sum(self.marks) / len(self.marks)
        return average >50

    def __str__(self) -> str:
        return f"{self.name}"

student1 = Student("Anna", [20, 30, 40])
print(f'Czy {student1.name} zdał(a) egzamin? {student1.is_passed()}')

student2 = Student("Adam", [80,90,100])
print(f'Czy {student2.name} zdał(a) egzamin? {student2.is_passed()}')