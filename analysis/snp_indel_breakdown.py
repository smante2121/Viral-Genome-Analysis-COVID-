# snp_indel_breakdown.py
from utils_vcf import load_vcf
import matplotlib.pyplot as plt
import os

df = load_vcf("variants_filtered.vcf")

def type_of_variant(row):
    if len(row["REF"]) == 1 and len(row["ALT"]) == 1:
        return "SNP"
    else:
        return "Indel"

df["TYPE"] = df.apply(type_of_variant, axis=1)

counts = df["TYPE"].value_counts()
print(counts)

os.makedirs("plots", exist_ok=True)
plt.figure(figsize=(6,5))
counts.plot(kind="bar", color=["#4472C4", "#ED7D31"])
plt.title("SNP vs Indel Count")
plt.xlabel("")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("plots/snp_vs_indel.png", dpi=300)

print("Saved: snp_vs_indel.png")
