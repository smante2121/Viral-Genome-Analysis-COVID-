# spike_mutation_plot.py
from utils_vcf import load_vcf
import matplotlib.pyplot as plt
import os

SPIKE_START = 21563
SPIKE_END = 25384

os.makedirs("plots", exist_ok=True)

df = load_vcf("variants_filtered.vcf")

spike = df[(df["POS"] >= SPIKE_START) & (df["POS"] <= SPIKE_END)]

plt.figure(figsize=(14,3))

plt.stem(spike["POS"], [1]*len(spike), basefmt=" ", linefmt="orange", markerfmt="o")

plt.title("Spike Region Mutations (Position Only)")
plt.xlabel("Genome Position (Spike Region)")
plt.yticks([])
plt.tight_layout()
plt.savefig("plots/spike_mutations.png", dpi=300)

print("Saved enhanced Spike mutation plot.")
