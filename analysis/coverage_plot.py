# coverage_plot.py
import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("plots", exist_ok=True)

df = pd.read_csv("depth.txt", sep="\t", header=None, names=["chrom", "pos", "depth"])
df["smooth"] = df["depth"].rolling(window=200, center=True, min_periods=1).mean()

# Smoothed coverage plot
plt.figure(figsize=(16,5))
plt.plot(df["pos"], df["smooth"], linewidth=0.8, color="steelblue")
plt.title("Genome-wide Coverage (Smoothed)")
plt.xlabel("Genome Position")
plt.ylabel("Depth (Smoothed)")
plt.tight_layout()
plt.savefig("plots/coverage_plot.png", dpi=300)

# Histogram (log scale)
plt.figure(figsize=(7,5))
plt.hist(df["depth"], bins=80, log=True, color="steelblue")
plt.axvline(df["depth"].median(), color="red", linestyle="--",
            label=f"Median = {df['depth'].median():.0f}")
plt.title("Coverage Depth Distribution (log-scale)")
plt.xlabel("Depth")
plt.ylabel("Count (log scale)")
plt.legend()
plt.tight_layout()
plt.savefig("plots/coverage_histogram.png", dpi=300)

print("Saved enhanced coverage plots.")
