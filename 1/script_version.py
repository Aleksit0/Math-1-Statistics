#!usr/bin/env python

# PYTHON SCRIPT VERSION OF NOTEBOOK

import numpy as np
import panda as pd
import matplotlib.pyplot as plt

# LOADING OUR DATA
data_1 = pd.read_csv('M1S-1.csv')
data_1 = data_1.fillna(0)

# MAKING A DATAFRAME
df = pd.DataFrame(data = data_1)
df["Frequency (fi)"] = df["Frequency (fi)"].astype(float)

# DATASET & DATAFRAME FOR VISUELIZATION
data_1_mod = data_1-truncate(before = 0, after = 4, axis = "rows")
plotted_df = pd.DataFrame(data = data_1_mod)

# VISUELIZATION (LINE CHART)
plotted_df.plot(x = 'Value (Xi)', y = 'Frequency (fi)', style = '-o', figsize = (10, 8), grif = True)
plt.legend(["Value(grades)", "Frequency"])

# VISUELIZATION (HISTOGRAM)
plotted_df.plot.bar(x = 'Value (Xi)', y = 'Frequency (fi)', grid = True, color = ['None', 'yellow', 'orange', 'blue', 'green'], legend = False)
