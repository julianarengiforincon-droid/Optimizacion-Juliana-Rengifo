# Condiciones iniciales (semana 0)
S = 200   # sillas en la semana 0
M = 80    # mesas en la semana 0

semanas_a_calcular = 10

print("=" * 50)
print("  PROBLEMA 2 - PRODUCCION SEMANAL DE FABRICA")
print("=" * 50)
print(f"\nCondicion inicial: S0 = {S} sillas, M0 = {M} mesas")
print(f"\n{'Semana':<10} {'Sillas (Sn)':<18} {'Mesas (Mn)':<15}")
print("-" * 43)
print(f"{'0':<10} {S:<18.1f} {M:<15.1f}")

for n in range(1, semanas_a_calcular + 1):
    S_siguiente = 0.6 * S + 0.2 * M + 40
    M_siguiente = 0.1 * S + 0.5 * M + 20
    S = S_siguiente
    M = M_siguiente
    print(f"{n:<10} {S:<18.1f} {M:<15.1f}")

# Verificacion manual de semanas 1 y 2 
print("\n--- Verificacion semanas 1 y 2 (calculo manual) ---")
S0, M0 = 200, 80
S1 = 0.6 * S0 + 0.2 * M0 + 40
M1 = 0.1 * S0 + 0.5 * M0 + 20
print(f"Semana 1: S1 = 0.6(200) + 0.2(80) + 40 = {S1} sillas")
print(f"Semana 1: M1 = 0.1(200) + 0.5(80) + 20 = {M1} mesas")

S2 = 0.6 * S1 + 0.2 * M1 + 40
M2 = 0.1 * S1 + 0.5 * M1 + 20
print(f"Semana 2: S2 = 0.6({S1}) + 0.2({M1}) + 40 = {S2} sillas")
print(f"Semana 2: M2 = 0.1({S1}) + 0.5({M1}) + 20 = {M2} mesas")

# Punto de equilibrio: Sn+1 
# El sistema tiende a estabilizarse cuando la produccion no cambia entre semanas
print("\n--- Punto de equilibrio (tendencia a largo plazo) ---")
print("Se plantea: S = 0.6S + 0.2M + 40  =>  0.4S - 0.2M = 40")
print("            M = 0.1S + 0.5M + 20  =>  -0.1S + 0.5M = 20")
import numpy as np
A = np.array([[0.4, -0.2], [-0.1, 0.5]])
b = np.array([40, 20])
equilibrio = np.linalg.solve(A, b)
print(f"Equilibrio: S* = {equilibrio[0]:.1f} sillas, M* = {equilibrio[1]:.1f} mesas")
