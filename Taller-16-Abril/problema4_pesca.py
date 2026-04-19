# Problema 4 - Modelo logistico de pesca
# P(n+1) = Pn + r*Pn*(1 - Pn/K) - H
# Se simula por anos y se grafican los equilibrios

import numpy as np
import matplotlib.pyplot as plt

# Parametros
r = 0.4    # tasa de crecimiento intrinseca
K = 1000   # capacidad maxima de la laguna
H = 80     # cuota de pesca anual
P0 = 400   # poblacion inicial

# Puntos de equilibrio (calculados a mano con formula cuadratica)
# Se obtienen de: r*P*(1 - P/K) - H = 0
# -0.0004*P^2 + 0.4*P - 80 = 0  =>  usando formula cuadratica
discriminante = (r * K)**2 - 4 * (r / K) * H * K
P_eq1 = (r * K + np.sqrt(discriminante)) / (2 * r / K * K)
P_eq2 = (r * K - np.sqrt(discriminante)) / (2 * r / K * K)

# Forma directa de la formula cuadratica: a=-r/K, b=r, c=-H
a = -r / K
b = r
c = -H
disc = b**2 - 4 * a * c
P_eq_alto = (-b - np.sqrt(disc)) / (2 * a)   # equilibrio estable  ~723.6
P_eq_bajo  = (-b + np.sqrt(disc)) / (2 * a)   # equilibrio inestable ~276.4

print("=" * 50)
print("  PROBLEMA 4 - MODELO LOGISTICO DE PESCA")
print("=" * 50)
print(f"\nParametros: r={r}, K={K}, H={H}, P0={P0}")

# Verificacion manual de P1 y P2
P1 = P0 + r * P0 * (1 - P0 / K) - H
P2 = P1 + r * P1 * (1 - P1 / K) - H
print(f"\nCalculo manual:")
print(f"  P1 = {P0} + 0.4({P0})(1 - {P0}/1000) - 80 = {P1:.2f} peces")
print(f"  P2 = {P1:.2f} + 0.4({P1:.2f})(1 - {P1:.2f}/1000) - 80 = {P2:.2f} peces")

print(f"\nPuntos de equilibrio (P_n+1 = P_n):")
print(f"  P* alto  = {P_eq_alto:.1f} peces  (estable)")
print(f"  P* bajo  = {P_eq_bajo:.1f} peces  (inestable)")

# Simulacion de poblacion a lo largo de los anos
anos = 80
poblacion_sobre = []   # empieza sobre el equilibrio inestable (P0=400)
poblacion_bajo  = []   # empieza debajo del equilibrio inestable (P0=200)

P_s = 400
P_b = 200
for n in range(anos):
    poblacion_sobre.append(P_s)
    poblacion_bajo.append(P_b)
    P_s = P_s + r * P_s * (1 - P_s / K) - H
    P_b_next = P_b + r * P_b * (1 - P_b / K) - H
    P_b = max(P_b_next, 0)   # no puede ser negativa

t = range(anos)

# Grafica
plt.figure(figsize=(10, 5))
plt.plot(t, poblacion_sobre, color='steelblue', linewidth=2,
         label=f'P0 = 400 (sobre equilibrio inestable)')
plt.plot(t, poblacion_bajo, color='tomato', linewidth=2,
         label=f'P0 = 200 (bajo equilibrio inestable)')
plt.axhline(y=P_eq_alto, color='green', linestyle='--', linewidth=1.2,
            label=f'Equilibrio estable: P* = {P_eq_alto:.0f}')
plt.axhline(y=P_eq_bajo, color='orange', linestyle='--', linewidth=1.2,
            label=f'Equilibrio inestable: P* = {P_eq_bajo:.0f}')
plt.xlabel('Ano (n)')
plt.ylabel('Poblacion de peces')
plt.title('Modelo Logistico de Pesca con Cosecha\n'
          r'$P_{n+1} = P_n + r \cdot P_n(1 - P_n/K) - H$')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('grafica_pesca.png', dpi=150)
plt.show()
print("\nGrafica guardada como 'grafica_pesca.png'")
