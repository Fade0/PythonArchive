zmienna1 = "Python 2023"
zmienna2 = zmienna1
zmienna3 = zmienna1

if (zmienna1 == zmienna2):
    print(zmienna1 == zmienna2)
else:
    print(False)

if (zmienna2 == zmienna3):
    print(zmienna2 == zmienna3)
else:
    print(False)

print(type(zmienna1) , hex(id(zmienna1)))
print(type(zmienna2) , hex(id(zmienna2)))
print(type(zmienna3) , hex(id(zmienna3)))

zmienna3 = "Java 11"
print("-------")

if (zmienna1 == zmienna2):
    print(zmienna1 == zmienna2)
else:
    print(False)

if (zmienna2 == zmienna3):
    print(zmienna2 == zmienna3)
else:
    print(False)

print(type(zmienna1) , hex(id(zmienna1)))
print(type(zmienna2) , hex(id(zmienna2)))
print(type(zmienna3) , hex(id(zmienna3)))