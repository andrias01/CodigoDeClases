import time
import os
import sys
"""
Make a program that reads three floating point values: A, B and C. Then, calculate and show:
a) the area of the rectangled triangle that has base A and height C.
b) the area of the radius's circle C. (pi = 3.14159)
c) the area of the trapezium which has A and B by base, and C by height.
d) the area of ​​the square that has side B.
e) the area of the rectangle that has sides A and B.
3.0 4.0 5.2

TRIANGULO: 7.800
CIRCULO: 84.949
TRAPEZIO: 18.200
QUADRADO: 16.000
RETANGULO: 12.000
A = float(A)
A = float(A)
A = float(A)
"""
A,B,C = map(float,input().split())
pi = 3.14159
retangledArea=(A*C)/2
circleArea=pi*(C**2)
trapeziumArea=(A+B)*C/2
squareArea=B**2
retangleArea=A*B

print(f"TRIANGULO: {retangledArea:.3f}")
print(f"CIRCULO: {circleArea:.3f}")
print(f"TRAPEZIO: {trapeziumArea:.3f}")
print(f"QUADRADO: {squareArea:.3f}")
print(f"RETANGULO: {retangleArea:.3f}")




time.sleep(15)
