# variant_summary.py
from utils_vcf import load_vcf
import pandas as pd
import os

os.makedirs("plots", exist_ok=True)

df = load_vcf("variants_filtered.vcf")

df.to_csv("variant_table.csv", index=False)

print("\n===== VARIANT SUMMARY =====")
print(f"Total Variants: {len(df)}")
print(f"Mean Depth: {df['DP'].mean():.1f}")
print(f"Median Depth: {df['DP'].median():.1f}")
print(f"Mean QUAL: {df['QUAL'].mean():.1f}")
print(f"Median QUAL: {df['QUAL'].median():.1f}")

print("\nSaved variant_table.csv")
