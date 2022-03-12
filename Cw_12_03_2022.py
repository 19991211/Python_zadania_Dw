# #Przykład 1
# a = []
# for x in range (10):
#     a.append(x**2)
# print(a)
# b = []
# for y in range (6):
#     b.append(3**y)
# print(b)
# c = []
# for z in a:
#     if z % 2 ==1:
#         c.append(z)
# print(c)
#
#
#
# #Przykład 1 z python comprehension
# a = [x**2 for x in range(10)]
# b = [3**i for i in range(6)]
# c = [x for x in a if x % 2==1]
# print(a)
# print(b)
# print(c)

#przykład 2
#wersja z pętlą
# liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista = []
# for i in liczby:
#     if i % 2 == 0:
#         lista.append(i)
# print("Liczby parzyste uzyskane z wykorzystaniem pętli")
# print(lista)
# print()
#zad 1
# a =[1-x for x in range(1,10)]
# print(a)
# b = [4**i for i in range(7)]
# print(b)
# c = [x for x in a if x // 2]
# print(c)
#zad 2
lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = [i for i in lista if i % 2 == 0 ]
print (lista)
print(lista2)
