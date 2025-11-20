# qual_depth_scatter.py
from utils_vcf import load_vcf
import matplotlib.pyplot as plt
import os

df = load_vcf("variants_filtered.vcf")

os.makedirs("plots", exist_ok=True)

plt.figure(figsize=(7,5))
plt.scatter(df["DP"], df["QUAL"], s=20, alpha=0.7)
plt.xlabel("Depth (DP)")
plt.ylabel("Quality (QUAL)")
plt.title("QUAL vs DP")
plt.tight_layout()
plt.savefig("plots/qual_vs_dp.png", dpi=300)

print("Saved: qual_vs_dp.png")
