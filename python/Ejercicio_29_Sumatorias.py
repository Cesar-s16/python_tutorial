import math

n = int(input("Ingrese el valor de n para todas las sumatorias: "))

# a) Sumatoria de 2^n
suma_a = 0
for i in range(n + 1):
    suma_a += 2**i
print(f"Resultado a): {suma_a}")

# b) Sumatoria 1 / (2^n)
suma_b = 0
for i in range(n + 1):
    suma_b += 1 / 2**i
print(f"Resultado b): {suma_b}")

# c) Sumatoria n! / (2n! + 1)
suma_c = 0
factorial_n = math.factorial(n)
for i in range(n + 1):
    suma_c += factorial_n / (2 * math.factorial(2 * i) + 1)
print(f"Resultado c): {suma_c}")

# d) Sumatoria 10/n
suma_d = 0
for i in range(1, n + 1):
    suma_d += 10 / i
print(f"Resultado d): {suma_d}")

# e) Sumatoria (n^2 + 3) / (4n - 5n^2)
suma_e = 0
for i in range(1, n + 1):
    suma_e += (i**2 + 3) / (4 * i - 5 * i**2)
print(f"Resultado e): {suma_e}")

# f) Sumatoria Raiz(n) / Raiz(n^3 + 1)
suma_f = 0
for i in range(1, n + 1):
    suma_f += math.sqrt(i) / math.sqrt(i**3 + 1)
print(f"Resultado f): {suma_f}")

# g) Sumatoria ((4n^3 + 5) * Sen(1/n)) / (n^2 * 3^n)
suma_g = 0
for i in range(1, n + 1):
    suma_g += ((4 * i**3 + 5) * math.sin(1 / i)) / (i**2 * 3**i)
print(f"Resultado g): {suma_g}")
