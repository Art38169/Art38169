import math
import sympy

x = sympy.symbols('x')
sympy.init_printing(use_unicode=True)

def dif(f):
    dif_f = sympy.diff(f , x)
    return dif_f

   
def gradient(f, x_0, a = 0.1, p = 1000):
    i = 0
    while i < p:
        grad = dif(f).replace(x, x_0)
        x_0 -= a * grad
        i += 1
    return x_0

print(gradient(x ** 4 + x + 1, 0))
   

