# qual_depth_scatter.py
from utils_vcf import load_vcf
import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs("plots", exist_ok=True)

df = load_vcf("variants_filtered.vcf")

jitter = np.random.normal(0, 1, size=len(df))

plt.figure(figsize=(7,6))
plt.scatter(df["DP"] + jitter, df["QUAL"],
            s=40, alpha=0.6, color="purple")

# Trendline
z = np.polyfit(df["DP"], df["QUAL"], 1)
p = np.poly1d(z)
plt.plot(df["DP"], p(df["DP"]), color="black", linestyle="--", label="Trendline")

plt.title("QUAL vs Depth (with jitter + trendline)")
plt.xlabel("Depth (DP)")
plt.ylabel("Quality (QUAL)")
plt.legend()
plt.tight_layout()
plt.savefig("plots/qual_vs_dp.png", dpi=300)

print("Saved enhanced QUAL vs DP plot.")
