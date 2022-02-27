#try:
    #blok instrukcji
#except nazwa_błedu:
    #blok instrukcji po napotkaniu błedu
#else:
    #instrukcje bez błedu
liczba1 = input('Podaj pierwszą liczbę: ')
liczba2 = input('Podaj drugą liczbę: ')


try:
    liczba1 = int(liczba1)
    liczba2 = int(liczba2)
    wynik = liczba1/liczba2
    print('Wynik działania = ' + str(wynik))
except ZeroDivisionError:
    print('Nie można dzielić przez 0')
except ValueError:
    print('Nie wczytano liczby całkowitej')