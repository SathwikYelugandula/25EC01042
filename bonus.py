import numpy as np
import matplotlib.pyplot as plt

IS = 1e-12       
Vt = 0.02585        
n_list = [1.0, 1.5, 2.0]

vd = np.arange(0, 0.8 + 1e-9, 0.01)  

diode_data = {}
for n in n_list:
    id_ = IS * (np.exp(vd / (n * Vt)) - 1)
    diode_data[n] = id_

plt.figure(1, figsize=(8, 6))
for n in n_list:
    plt.plot(vd, diode_data[n] * 1e3, linewidth=2, label=f'$n$ = {n}')

plt.title('Diode $I_D$-$V_D$ Characteristics (Linear Scale)', fontsize=14, fontweight='bold')
plt.xlabel('Diode Voltage, $V_D$ (V)', fontsize=12)
plt.ylabel('Diode Current, $I_D$ (mA)', fontsize=12)
plt.legend(title='Ideality factor')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()


plt.figure(2, figsize=(8, 6))
for n in n_list:
    plt.semilogy(vd, diode_data[n], linewidth=2, label=f'$n$ = {n}')

plt.title('Diode $I_D$-$V_D$ Characteristics (Log Scale)', fontsize=14, fontweight='bold')
plt.xlabel('Diode Voltage, $V_D$ (V)', fontsize=12)
plt.ylabel('Diode Current, $I_D$ (A)', fontsize=12)
plt.legend(title='Ideality factor')
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.tight_layout()


plt.figure(3, figsize=(8, 6))
for n in n_list:
    gd = np.gradient(diode_data[n], vd)
    plt.semilogy(vd, gd, linewidth=2, label=f'$n$ = {n}')

plt.title('Diode Small-Signal Conductance $g_d = dI_D/dV_D$', fontsize=14, fontweight='bold')
plt.xlabel('Diode Voltage, $V_D$ (V)', fontsize=12)
plt.ylabel('Conductance, $g_d$ (S)', fontsize=12)
plt.legend(title='Ideality factor')
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
