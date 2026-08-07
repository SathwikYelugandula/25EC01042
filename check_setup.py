import sys
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
print("Python version :", sys.version.split()[0])
print("numpy version :", np.__version__ )
print("pandas version :", pd.__version__ )
print("matplotlib:", matplotlib.__version__)
print("roll no: 25EC01042")
print("hello world")
# a one-line smoke test of the plotting back-end
plt.plot([0, 1, 2, 3], [0, 1, 4, 9], marker="o")
plt.title("If you can see this window, the setup works")
plt.xlabel("x"); plt.ylabel("x squared")
plt.grid(True)
plt.show()
