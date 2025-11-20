# spike_mutation_plot.py
from utils_vcf import load_vcf
import matplotlib.pyplot as plt
import os

# Spike protein region in NC_045512.2
SPIKE_START = 21563
SPIKE_END = 25384

df = load_vcf("variants_filtered.vcf")

# Filter to spike gene only
spike = df[(df["POS"] >= SPIKE_START) & (df["POS"] <= SPIKE_END)]

os.makedirs("plots", exist_ok=True)

plt.figure(figsize=(12,3))

# FIXED: removed deprecated use_line_collection argument
plt.stem(spike["POS"], [1] * len(spike), basefmt=" ")

plt.title("Spike Protein Mutation Plot")
plt.xlabel("Genome Position (S gene region)")
plt.yticks([])
plt.tight_layout()
plt.savefig("plots/spike_mutations.png", dpi=300)

print("Saved: spike_mutations.png")
