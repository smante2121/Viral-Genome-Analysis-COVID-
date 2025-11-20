# snp_indel_breakdown.py
from utils_vcf import load_vcf
import matplotlib.pyplot as plt
import os

os.makedirs("plots", exist_ok=True)

df = load_vcf("variants_filtered.vcf")

def classify(row):
    return "SNP" if len(row["REF"]) == 1 and len(row["ALT"]) == 1 else "Indel"

df["TYPE"] = df.apply(classify, axis=1)

counts = df["TYPE"].value_counts()
perc = counts / counts.sum() * 100

plt.figure(figsize=(6,4))
bars = plt.bar(counts.index, counts.values, color=["#1f77b4", "#ff7f0e"])
plt.title("SNP vs Indel Distribution")
plt.ylabel("Count")

for i, v in enumerate(counts.values):
    plt.text(i, v + 0.5, f"{v} ({perc.values[i]:.1f}%)", ha="center")

plt.tight_layout()
plt.savefig("plots/snp_vs_indel.png", dpi=300)

print("Saved enhanced SNP vs Indel plot.")
