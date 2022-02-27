#Funkcje warunkowe
#if warunek1: Instrukcja lub blok instrukcji dla warunek 1
#elif warunek2: Instrukcja lub blok instrukcji
#elif warunek n: instrukcja lub blok instrukcji
#else: instrukcje gdy warunki nie spełnione
#x==y
# x!=y
# x>y
# x<t
# x>=y
# x<=y
a = 7
b = 5
if a > b:
    print('liczba a jest większa od liczby b')
elif a < b:
    print('liczba a jest mniejsza od b')
else:
    print('liczby sa równe')