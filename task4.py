
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import*
x1 = float(input("Введите х первой точки: "))
y1 = float(input("Введите у первой точки: "))
x2 = float(input("Введите х второй точки: "))
y2 = float(input("Введите y второй точки: "))

dist = sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

print("Расстояние между точками :",round(dist,2))
