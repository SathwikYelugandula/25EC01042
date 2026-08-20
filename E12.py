import numpy as np
import matplotlib.pyplot as plt


tox    = 10e-7    
NA     = 1e16      
QF     = 1e12        
W      = 4e-4        
L      = 0.18e-4        
phi_M  = 4.1             
mu_n   = 400               


q      = 1.602e-19   
eps0   = 8.854e-14     
eps_ox = 3.9 * eps0
eps_si = 11.7 * eps0
kT     = 0.0259          
ni     = 1.5e10           
chi_si = 4.05                
Eg     = 1.12                  


Cox      = eps_ox / tox                                  
phi_F    = kT * np.log(NA / ni)                            
phi_S    = chi_si + Eg / 2 + phi_F                           
phi_MS   = phi_M - phi_S                                       
Qdep_max = np.sqrt(2 * eps_si * q * NA * 2 * phi_F)             
Vfb      = phi_MS - (q * QF) / Cox                               
VT       = Vfb + 2 * phi_F + Qdep_max / Cox                          

kp = mu_n * Cox  
print(f"C_ox  = {Cox * 1e9:.4f} nF/cm^2")
print(f"phi_F = {phi_F:.4f} V")
print(f"V_FB  = {Vfb:.4f} V")
print(f"V_T   = {VT:.4f} V")
print(f"k'    = {kp * 1e6:.4f} uA/V^2")


lam   = 0.1    
theta = 0.1       
vmax  = 1e7          
Esat  = 2 * vmax / mu_n  

def id_level1(vgs, vds):
    vov = vgs - VT
    id_ = np.zeros_like(vds)
    if vov <= 0:
        return id_
    triode = vds < vov
    id_[triode] = kp * (W / L) * (vov * vds[triode] - vds[triode] ** 2 / 2) * (1 + lam * vds[triode])
    sat = ~triode
    id_[sat] = 0.5 * kp * (W / L) * vov ** 2 * (1 + lam * vds[sat])
    return id_

def id_level3(vgs, vds):
    vov = vgs - VT
    id_ = np.zeros_like(vds)
    if vov <= 0:
        return id_
    mu_eff = mu_n / (1 + theta * vov)    
    kp3 = mu_eff * Cox
    vdsat = vov / (1 + vov / (Esat * L))    
    id_dsat = kp3 * (W / L) * (vov * vdsat - vdsat ** 2 / 2)
    triode = vds < vdsat
    id_[triode] = kp3 * (W / L) * (vov * vds[triode] - vds[triode] ** 2 / 2)
    sat = ~triode
    id_[sat] = id_dsat * (1 + lam * (vds[sat] - vdsat))
    return id_

vds = np.linspace(0, 4, 400)
vgs_list = [1, 2, 3]

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

for vgs in vgs_list:
    id_mA = id_level1(vgs, vds) * 1e3  # A -> mA
    axes[0].plot(vds, id_mA, linewidth=2, label=f'$V_{{GS}}$ = {vgs} V')

for vgs in vgs_list:
    id_mA = id_level3(vgs, vds) * 1e3  # A -> mA
    axes[1].plot(vds, id_mA, linewidth=2, label=f'$V_{{GS}}$ = {vgs} V')

axes[0].set_title('SPICE Level 1', fontweight='bold')
axes[1].set_title('SPICE Level 3', fontweight='bold')
for a in axes:
    a.set_xlabel('$V_{DS}$ (V)')
    a.set_ylabel('$I_D$ (mA)')
    a.grid(True, linestyle='--', alpha=0.6)
    a.legend()

plt.tight_layout()
plt.show()
