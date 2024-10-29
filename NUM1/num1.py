import numpy as np
import matplotlib.pyplot as plt

a = 0.2
b = 0.6
h = np.logspace(-16, 0, 100)

def FunctionExample(x):
    return (np.sin(x**3))

def FunctionA(f, x, h):
    return ((f(x + h) - f(x)) / h)

def FunctionB(f, x, h):
    return ((f(x + h) - f(x - h)) / (2 * h))

def ActualDerivate(x):
    return (3 *(x**2)* np.cos(x**3))

def IteratingWithDifferentH(a_result, b_result, actual_result, h, point, function_name):
    for i in range(0, size):
        helper = h[i]
        a_result[i] = FunctionA(function_name, point, helper)
        b_result[i] = FunctionB(function_name, point, helper)
    return a_result, b_result

def Difference(a_result, b_result, actual_result):
    a_dif = abs(a_result - actual_result) # odejmowanie dziala dzieki elemsent-wise arytmetyce numpy
    b_dif = abs(b_result - actual_result)
    return a_dif, b_dif

def Console():
    print("""Uwaga: Po uruchomieniu programu rownoczesnie otworza sie dwa okienka zawierające wykresy (prawdopodobnie beda na siebie nalozone).""")

def FunctionExampleSec(x):
    return (x**3)

def ActualDerivateSec(x):
    return (3*(x**2))

Console()


size = len(h)
#wykres eksperymentalny

a_result_sec = np.zeros(size)
b_result_sec = np.zeros(size)
actual_result_sec = ActualDerivateSec(b)

a_result_sec, b_result_sec = IteratingWithDifferentH(a_result_sec, b_result_sec, actual_result_sec, h, b, FunctionExampleSec)
a_dif_sec, b_dif_sec = Difference(a_result_sec, b_result_sec, actual_result_sec)

a_result_32_sec = np.zeros(size, dtype=np.float32)
b_result_32_sec = np.zeros(size, dtype=np.float32)
actual_result_32_sec = ActualDerivateSec(np.float32(b))
h_32_sec = h.astype(np.float32)

a_result_32_sec, b_result_32_sec = IteratingWithDifferentH(a_result_32_sec, b_result_32_sec, actual_result_32_sec, h_32_sec, np.float32(b), FunctionExampleSec)
a_dif_float32_sec, b_dif_float32_sec = Difference(a_result_32_sec, b_result_32_sec, actual_result_32_sec)

plt.figure(1)
plt.plot(h, a_dif_float32_sec, color = 'green', label = "float; roznica w przod (1)") 
plt.plot(h, b_dif_float32_sec, color = 'black', label = "float; roznica centralna (2)")
plt.plot(h, a_dif_sec, color = 'blue', label = "double; roznica w przod (1)") 
plt.plot(h, b_dif_sec, color = 'gray', label = "double; roznica centralna (2)")
plt.xscale('log')
plt.yscale('log')
plt.xlabel("h")
plt.ylabel("| Dhf(x) - f '(x)|")
plt.title("Blad numerycznej rozniczki dla funkcji g(x) = x^3 w punkcie x = 0.6")
plt.grid(True)
plt.legend()

#sinus
a_result = np.zeros(size)
b_result = np.zeros(size)
actual_result = ActualDerivate(a)

a_result, b_result = IteratingWithDifferentH(a_result, b_result, actual_result, h, a, FunctionExample)
a_dif, b_dif = Difference(a_result, b_result, actual_result)

a_result_32 = np.zeros(size, dtype=np.float32)
b_result_32 = np.zeros(size, dtype=np.float32)
actual_result_32 = ActualDerivate(np.float32(a))
h_32 = h.astype(np.float32)

a_result_32, b_result_32 = IteratingWithDifferentH(a_result_32, b_result_32, actual_result_32, h_32, np.float32(a), FunctionExample)
a_dif_float32, b_dif_float32 = Difference(a_result_32, b_result_32, actual_result_32)

plt.figure(2)
plt.plot(h, a_dif, color = 'pink', label = "double; roznica w przod (1)") 
plt.plot(h, b_dif, color = 'purple', label = "double; roznica centralna (2)")

plt.plot(h, b_dif_float32, color = 'yellow', label = "float; roznica w przod (1)")
plt.plot(h, a_dif_float32, color = 'orange', label = "float; roznica centralna (2)") 
plt.xscale('log')
plt.yscale('log')
plt.xlabel("h")
plt.ylabel("| Dhf(x) - f '(x)|")
plt.title("Blad numerycznej rozniczki dla funkcji f(x) = sin(x^3) w punkcie x = 0.2")
plt.grid(True)


plt.legend()

plt.show()

