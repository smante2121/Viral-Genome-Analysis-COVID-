# variant_summary.py
from utils_vcf import load_vcf
import os

vcf = "variants_filtered.vcf"
df = load_vcf(vcf)

summary = {
    "Total Variants": len(df),
    "Mean Depth": df["DP"].mean(),
    "Median Depth": df["DP"].median(),
    "Mean QUAL": df["QUAL"].mean(),
    "Median QUAL": df["QUAL"].median(),
}

print("\nVARIANT SUMMARY")
for k,v in summary.items():
    print(f"{k}: {v}")

df.to_csv("variant_table.csv", index=False)
print("\nSaved: variant_table.csv")
