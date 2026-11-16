x = float(input("ingrese valor 1: "))
y = float(input("ingrese el valor 2: "))
z = float(input("ingrese el valor 3: "))

if x < y < z:
    print("de menor a mayor: ", x, y, z)
elif x < z < y:
    print("de menor a mayor: ", x, z, y)
elif y < x < z:
    print("de menor a mayor: ", y, x, z)
elif y < z < x:
    print("de menor a mayor: ", y, z, x)
elif z < y < x:
    print("de menor a mayor: ", z, y, x)
elif z < x < y:
    print("de menor a mayor: ", z, x, y)
elif x == z or x == y or y == z:
    print("hay 2 o mas numeros repetidos")
