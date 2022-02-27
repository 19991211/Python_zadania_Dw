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
# a = 7
# b = 5
# if a > b:
#     print('liczba a jest większa od liczby b')
# elif a < b:
#     print('liczba a jest mniejsza od b')
# else:
#    print('liczby sa równe')
a = input("Podaj liczbe a: ")
b = input("podaj liczbe b: ")
c = input("Podaj liczbe c: ")
d = input("podaj liczbe d: ")
#     print(a)
#     print(type(a))
#      a = int(a)
#     print(type(a))
a = int(a)
b = int(b)
c = int(c)
d = int(d)
if ( a > b ) & ( c > d ):
    print('liczba a jest wieksza od liczby b i liczba c jest wieksza od liczby d')
else:
    print('liczba a jest mniejsza niz liczba b lub liczba c jest mniejsza od liczby d')
