#Przykład 1
a = []
for x in range (10):
    a.append(x**2)
print(a)
b = []
for y in range (6):
    b.append(3**y)
print(b)
c = []
for z in a:
    if z % 2 ==1:
        c.append(z)
print(c)



#Przykład 1 z python comprehension
a = [x**2 for x in range(10)]
b = [3**i for i in range(6)]
c = [x for x in a if x % 2==1]
print(a)
print(b)
print(c)

#przykład 2