# Problema 3 - Epidemia en una ciudad (modelo SIS)
# dI/dt = beta*(10000 - I)*I - gamma*I
# Se simula con scipy.integrate.odeint

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parametros del modelo
N = 10000       # poblacion total de la ciudad (constante)
beta = 0.00003  # tasa de contagio por dia
gamma = 0.1     # tasa de recuperacion por dia

# Condicion inicial: I(0) = 50 personas infectadas
I0 = 50

# Tiempo de simulacion (dias)
t = np.linspace(0, 200, 1000)

# Ecuacion diferencial del modelo SIS
def modelo_SIS(I, t, beta, gamma, N):
    dIdt = beta * (N - I) * I - gamma * I
    return dIdt

# Resolver la EDO
solucion = odeint(modelo_SIS, I0, t, args=(beta, gamma, N))
I = solucion[:, 0]

# Puntos de equilibrio (igualando dI/dt = 0):
# Caso 1: I = 0
# Caso 2: beta*(10000 - I) - gamma = 0  =>  I2 = 10000 - gamma/beta
I_eq1 = 0
I_eq2 = N - gamma / beta
print("=" * 50)
print("  PROBLEMA 3 - EPIDEMIA EN UNA CIUDAD (SIS)")
print("=" * 50)
print(f"\nParametros:")
print(f"  N  = {N} habitantes")
print(f"  beta  = {beta}")
print(f"  gamma = {gamma}")
print(f"  I(0)  = {I0} personas infectadas")

print(f"\nPuntos de equilibrio (dI/dt = 0):")
print(f"  Equilibrio 1: I* = {I_eq1}  (enfermedad desaparece)")
print(f"  Equilibrio 2: I* = {I_eq2:.2f} personas infectadas")
print(f"  -> El sistema tiende hacia I* = {I_eq2:.2f} infectados")

print(f"\nValor final simulado (t=200 dias): I = {I[-1]:.2f} personas")

# Grafica de la curva de contagios
plt.figure(figsize=(9, 5))
plt.plot(t, I, color='crimson', linewidth=2, label='Infectados I(t)')
plt.axhline(y=I_eq2, color='gray', linestyle='--', linewidth=1.2,
            label=f'Equilibrio estable: I* = {I_eq2:.0f}')
plt.axhline(y=0, color='black', linestyle='--', linewidth=0.8,
            label='Equilibrio inestable: I* = 0')
plt.xlabel('Tiempo (dias)')
plt.ylabel('Numero de infectados I(t)')
plt.title('Modelo SIS - Propagacion de epidemia\n'
          r'$\frac{dI}{dt} = \beta(10000-I)\cdot I - \gamma I$')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('grafica_epidemia.png', dpi=150)
plt.show()
print("\nGrafica guardada como 'grafica_epidemia.png'")
