#Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5 dowolnych liczb, każdy jej element pomnoży przez 2,
# a na końcu ją zwróci. Zadanie należy wykonać w 2 wersjach:
#Wykorzystując listę składaną.

def mnozenie_liczb_lista(liczby):
    return [liczba *2 for liczba in liczby]

lista_liczb = [2, 3, 5, 10, 15]
print(mnozenie_liczb_lista(lista_liczb))
