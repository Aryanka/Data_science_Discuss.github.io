# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import seaborn as sns

def plot_graph(df, col):
    col_mean = df[col].mean()
    col_median = df[col].median()
    col_mode = df[col].mode()
    
    fig, ax_hist = plt.subplots(figsize = (10,6)) #fig is outlay for figure object
    ax_hist = sns.distplot(df[col])

    ax_hist.axvline(col_mean, color = 'r', linestyle = '--', label = 'mean');
    ax_hist.axvline(col_median, color = 'b', linestyle = '--', label = 'median');
    ax_hist.axvline(col_mode[0], color = 'y', linestyle = '--', label = 'mode');

    plt.legend()
    plt.show()