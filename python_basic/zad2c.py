#Utwórz funkcję, która otrzyma w parametrze listę 10 liczb (rekomendowane wykorzystanie funkcji range),
#a następnie wyświetli jedynie parzyste elementy.

def zwroc_parzyste(liczby):
    return [liczba for liczba in liczby if liczba %2 == 0]

lista_liczb = list(range(10))
print(zwroc_parzyste(lista_liczb))