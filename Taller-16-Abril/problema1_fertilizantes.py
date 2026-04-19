import pulp

# Crear el problema de maximizacion
problema = pulp.LpProblem("Mezcla_Fertilizantes", pulp.LpMaximize)

# Variables de decision
# x1 = toneladas de F1 producidas en la semana
# x2 = toneladas de F2 producidas en la semana
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)

# Funcion objetivo: Max Z = 180*x1 + 220*x2
problema += 180 * x1 + 220 * x2

# Restricciones de compuestos disponibles por semana
problema += 3 * x1 + 4 * x2 <= 120   # Compuesto A: 120 kg disponibles
problema += 2 * x1 + 1 * x2 <= 80    # Compuesto B: 80 kg disponibles
problema += 5 * x1 + 3 * x2 <= 150   # Compuesto C: 150 kg disponibles

# Resolver
problema.solve(pulp.PULP_CBC_CMD(msg=0))

print("=" * 45)
print("  PROBLEMA 1 - MEZCLA DE FERTILIZANTES")
print("=" * 45)
print(f"Estado: {pulp.LpStatus[problema.status]}")
print(f"\nVariables de decision:")
print(f"  x1 (F1 producido) = {pulp.value(x1):.2f} toneladas/semana")
print(f"  x2 (F2 producido) = {pulp.value(x2):.2f} toneladas/semana")
print(f"\nGanancia maxima = ${pulp.value(problema.objective):.2f}")

# Verificar restricciones con los valores obtenidos
v1, v2 = pulp.value(x1), pulp.value(x2)
print(f"\nVerificacion de restricciones:")
print(f"  Compuesto A: 3({v1:.1f}) + 4({v2:.1f}) = {3*v1 + 4*v2:.1f} <= 120")
print(f"  Compuesto B: 2({v1:.1f}) + 1({v2:.1f}) = {2*v1 + 1*v2:.1f} <= 80")
print(f"  Compuesto C: 5({v1:.1f}) + 3({v2:.1f}) = {5*v1 + 3*v2:.1f} <= 150")
