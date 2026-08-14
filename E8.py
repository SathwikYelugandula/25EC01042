import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


file_path = 'C:/Users/Sathwik Yelugandula/Documents/EDA/Electrical Data/MOSFET_ID_VDS.csv'
df = pd.read_csv(file_path)

plt.figure(figsize=(10, 6))

highest_vgs = df['V_GS (V)'].max()
gd_sat_val = None

for v_gs, group in df.groupby('V_GS (V)'):
    group = group.sort_values('V_DS (V)')
    v_ds = group['V_DS (V)'].values
    i_d = group['I_D (mA)'].values
    
  
    g_d = np.gradient(i_d, v_ds)
    
    plt.plot(v_ds, g_d, linewidth=1, label=f'$V_{{GS}}$ = {v_gs} V')
    
    
    if v_gs == highest_vgs:
        gd_sat_val = g_d[-1]  


ro_kohm = 1.0 / gd_sat_val if gd_sat_val else 0

print(f"Highest V_GS = {highest_vgs} V")
print(f"Output Conductance in saturation (g_d) = {gd_sat_val:.4f} mS")
print(f"Output Resistance (r_o = 1/g_d) = {ro_kohm:.2f} kΩ")


plt.title('MOSFET Differential Output Conductance ($g_d = dI_D/dV_{DS}$)', fontsize=8, fontweight='bold')
plt.xlabel('Drain-to-Source Voltage, $V_{DS}$ (V)', fontsize=12)
plt.ylabel('Conductance, $g_d$ (mS)', fontsize=12)
plt.legend(title='Gate-Source Voltage', loc='upper right')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

plt.savefig('e8_output_conductance.png', dpi=300)
plt.show()