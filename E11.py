# =====================================================================
# E11. Diode I-V characteristics at different ambient temperatures.
# =====================================================================
import pandas as pd
import matplotlib.pyplot as plt
import sys

FILE_PATH = 'C:/Users/Sathwik Yelugandula/Documents/EDA/Electrical Data/Diode_IV_Temperature.csv'
TEMP_COL = 'T (C)'
V_COL = 'V (V)'
I_COL = 'I (mA)'

try:
    df = pd.read_csv(FILE_PATH)
except FileNotFoundError:
    sys.exit(f"ERROR: could not find '{FILE_PATH}'. Put the CSV in the same "
              f"folder as this script, or edit FILE_PATH to the correct path.")

print("Columns found in file:", list(df.columns))

missing = [c for c in (TEMP_COL, V_COL, I_COL) if c not in df.columns]
if missing:
    sys.exit(f"ERROR: column(s) {missing} not found. Your file's actual "
              f"columns are: {list(df.columns)}. Update TEMP_COL/V_COL/I_COL "
              f"above to match exactly (including spaces/units).")

plt.figure(figsize=(8, 6))

for temp, group in df.groupby(TEMP_COL):
    group = group.sort_values(V_COL)
    plt.plot(group[V_COL], group[I_COL], marker='o', linewidth=2,
              label=f'T = {temp} C')

plt.title('Diode I-V Characteristics at Different Temperatures', fontsize=14, fontweight='bold')
plt.xlabel('Voltage, V (V)', fontsize=12)
plt.ylabel('Current, I (mA)', fontsize=12)
plt.legend(title='Temperature')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('diode_iv.png', dpi=350)
plt.show()
