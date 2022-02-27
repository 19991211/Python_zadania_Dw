#lista=[] przyjmie prawie wszystko
#słownik={}el postaci
# klucz: wartosc <---- element słownika
lista=[1,2,3]
slownik = {'klucz1':1, 'klucz2':2, 'klucz3':3}
print(slownik)
del slownik['klucz1'] #<----- usuwanie pierwszego klucza z słownika
print(slownik)
del lista[0] #<---- usuwanie pierwszego indexu listy
print(lista)
slownik.popitem()
slownik['klucz2'] = 'samochód' #<----- zmiana wartości klucza
print(slownik)
lista[1] = 'Opel' #zmiana wartosci
print(lista)



