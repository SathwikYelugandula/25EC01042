import pandas as pd
import matplotlib.pyplot as plt

file_path = 'C:/Users/Sathwik Yelugandula/Documents/EDA/Electrical Data/MOSFET_ID_VDS.csv'
df = pd.read_csv(file_path)


fig, ax = plt.subplots(figsize=(8, 6), dpi=300)


for v_gs, group in df.groupby('V_GS (V)'):
    print("V_GS =", v_gs, "has", len(group), "points")


    group = group.sort_values('V_DS (V)')
    
    ax.plot(
        group['V_DS (V)'], 
        group['I_D (mA)'],
        linewidth=1, 
        label=f'$V_{{GS}}$ = {v_gs} V'
    )

ax.set_xlabel('V_GS, $V_{DS}$ (V)', fontsize=6)
ax.set_ylabel('ID, $I_D$ (mA)', fontsize=6)
ax.set_title('MOSFET Output Characteristics ($I_D$ vs $V_{DS}$)', fontweight='bold')
ax.legend(title='Gate Voltage')
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()

plt.savefig('e7_output_characteristics.png', dpi=300)
plt.show()