#pętla while
#while warunek:
# instrukcja lub blok instrukcji
#else:
#   instrukcja po zakończeniu działania pętli


# z = 0
# while z != 11:
#     print(z)
#     z += 1
# else:
#     print('wyświetlono ' + str(z) + ' liczb')

lista = [4,6,2,3,5,9,1]
liczba = input('podaj liczbe: ')
licznik = 0
while licznik != len(lista):
    if int(liczba) - lista[licznik] == 0:
        print(liczba + '- ' + str(lista[licznik]) + ' = 0')
        break
    else:
        licznik += 1

