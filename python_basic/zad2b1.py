
#2. Utwórz funkcję, która **otrzyma w parametrze** listę zawierającą 5 dowolnych liczb, każdy jej element pomnoży przez 2,
# a na końcu ją **zwróci.** Zadanie należy wykonać w 2 wersjach:
# i. Wykorzystując pętle `for`.

def mnozenie_liczb(liczby):
    wynik = []
    for liczba in liczby:
        wynik.append(liczba*2)
    return wynik

lista_liczb = [1,2,3,4,5,6]
print(mnozenie_liczb(lista_liczb))