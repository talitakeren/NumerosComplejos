# Operaciones con números complejos

# Suma de números complejos
def suma_complejos(c1, c2):
    return c1 + c2

# Resta de números complejos
def resta_complejos(c1, c2):
    return c1 - c2

# Multiplicación de números complejos
def multiplicacion_complejos(c1, c2):
    return c1 * c2

# División de números complejos
def division_complejos(c1, c2):
    try:
        return c1 / c2
    except ZeroDivisionError:
        return "No se puede dividir por cero"

# Ejemplo de uso
c1 = complex(3, 2)
c2 = complex(1, 7)

print(f"Suma: {suma_complejos(c1, c2)}")
print(f"Resta: {resta_complejos(c1, c2)}")
print(f"Multiplicación: {multiplicacion_complejos(c1, c2)}")
print(f"División: {division_complejos(c1, c2)}")