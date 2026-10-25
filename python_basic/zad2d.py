#Utwórz funkcję, która otrzyma w parametrze listę 10 liczb (rekomendowane wykorzystanie funkcji range),
# a następnie wyświetli co drugi element.

def co_drugi (liczby):
    return [liczba for liczba in liczby[::2]]

lista_liczb = list(range(1, 11))
print(co_drugi(lista_liczb))