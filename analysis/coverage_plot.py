# coverage_plot.py
import pandas as pd
import matplotlib.pyplot as plt
import os

depth_file = "depth.txt"
outdir = "plots"
os.makedirs(outdir, exist_ok=True)

df = pd.read_csv(depth_file, sep="\t", header=None, names=["chrom", "pos", "depth"])

plt.figure(figsize=(14,5))
plt.plot(df["pos"], df["depth"], linewidth=0.7)
plt.title("Coverage Across SARS-CoV-2 Genome")
plt.xlabel("Genome Position")
plt.ylabel("Depth")
plt.tight_layout()
plt.savefig(f"{outdir}/coverage_plot.png", dpi=300)

plt.figure(figsize=(7,5))
plt.hist(df["depth"], bins=50)
plt.title("Coverage Depth Distribution")
plt.xlabel("Depth")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(f"{outdir}/coverage_histogram.png", dpi=300)

print("Saved: coverage_plot.png, coverage_histogram.png")
