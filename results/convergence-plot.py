#!/usr/bin/env python3

"""
Generates a plot over the convergence of each generator type and seed
initialization.
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import pandas as pd

LAYER_1_PATHS = [
    './1-layer-generator/seed-0/logs/train_test.csv', 
    './1-layer-generator/seed-1/logs/train_test.csv'
]

LAYER_3_PATHS = [
    './3-layer-generator/seed-0/logs/train_test.csv', 
    './3-layer-generator/seed-1/logs/train_test.csv'
]

LAYER_5_PATHS = [
    './5-layer-generator/seed-0/logs/train_test.csv', 
    './5-layer-generator/seed-1/logs/train_test.csv'
]

def read_csv(path):
    csv = pd.read_csv(path)

    x = csv['global_step']
    y = csv['EVALUATE/test_acc']

    return x, y

def main():
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 5))

    for idx, path in enumerate(LAYER_1_PATHS):
        x, y = read_csv(path)
        ax1.plot(x, y, label=f"Seed {idx}")

    for idx, path in enumerate(LAYER_3_PATHS):
        x, y = read_csv(path)
        ax2.plot(x, y, label=f"Seed {idx}")

    for idx, path in enumerate(LAYER_5_PATHS):
        x, y = read_csv(path)
        ax3.plot(x, y, label=f"Seed {idx}")

    ax1.set_title("1 layer generator")
    ax2.set_title("3 layer generator")
    ax3.set_title("5 layer generator")

    for ax in (ax1, ax2, ax3):
        ax.set_xticks(np.arange(0, 80001, 10000))
        ax.set_xlim(0, 80000)
        ax.set_ylim(0, 85)
        ax.grid(True, linestyle='-.')
        ax.legend(loc=4)

        # Format x ticks
        f = mtick.ScalarFormatter(useOffset=False, useMathText=True)
        g = lambda x, _ : "${}$".format(f._formatSciNotation('%1e' % x))
        ax.xaxis.set_major_formatter(mtick.FuncFormatter(g))

        # Format y ticks
        ax.yaxis.set_major_formatter(mtick.PercentFormatter())

        ax.set_xlabel("Number of training batches")
        ax.set_ylabel("Test accuracy")

    plt.show()

if __name__ == "__main__":
    main()
