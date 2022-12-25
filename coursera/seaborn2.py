import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_theme()

np.random.seed(1234)

v1 = pd.Series(np.random.normal(0, 10, 1000), name="v1", dtype=float)
v2 = pd.Series(2 * v1 + np.random.normal(60, 15, 1000), name="v2", dtype=float)

sns.jointplot(data={"v1": v1, "v2": v2}, x="v1", y="v2", alpha=0.4, kind="hex")


plt.show()