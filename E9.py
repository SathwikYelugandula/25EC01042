import pandas as pd, numpy as np, matplotlib.pyplot as plt

dft = pd.read_csv('C:/Users/Sathwik Yelugandula/Documents/EDA/Electrical Data/MOSFET_ID_VGS.csv') 

fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))

for v_ds, g in dft.groupby('V_DS (V)'):
    g = g.sort_values('V_GS (V)')
    vgs = g['V_GS (V)'].values
    id_ = g['I_D (mA)'].values
    gm = np.gradient(id_, vgs)

    ax[0].plot(vgs, id_, linewidth=2, label=f'$V_{{DS}}$ = {v_ds} V')
    ax[1].plot(vgs, gm, linewidth=2, label=f'$V_{{DS}}$ = {v_ds} V')

    # mark the peak g_m for this V_DS curve
    i_peak = np.argmax(gm)
    ax[1].plot(vgs[i_peak], gm[i_peak], 'k*', markersize=12)
    ax[1].annotate(f'peak: $V_{{GS}}$={vgs[i_peak]:.2f} V',
                    (vgs[i_peak], gm[i_peak]),
                    textcoords="offset points", xytext=(5, 8), fontsize=8)

ax[0].set_title('Transfer characteristics', fontweight='bold')
ax[0].set_xlabel('$V_{GS}$ (V)'); ax[0].set_ylabel('$I_D$ (mA)')
ax[1].set_title('Transconductance $g_m = dI_D/dV_{GS}$', fontweight='bold')
ax[1].set_xlabel('$V_{GS}$ (V)'); ax[1].set_ylabel('$g_m$ (mS)')

for a in ax:
    a.grid(True, linestyle='--', alpha=0.6)
    a.legend(fontsize=9)

plt.tight_layout()
plt.savefig('gm_transfer.png', dpi=300)
plt.show()
