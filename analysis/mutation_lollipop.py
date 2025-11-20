# mutation_lollipop.py
from utils_vcf import load_vcf
import matplotlib.pyplot as plt
import os

df = load_vcf("variants_filtered.vcf")
positions = df["POS"]

os.makedirs("plots", exist_ok=True)

plt.figure(figsize=(15,3))

# FIXED: removed deprecated use_line_collection argument
plt.stem(positions, [1]*len(positions), basefmt=" ")

plt.title("Genome-wide Mutation Lollipop Plot")
plt.xlabel("Genome Position")
plt.yticks([])
plt.tight_layout()
plt.savefig("plots/lollipop_plot.png", dpi=300)

print("Saved: lollipop_plot.png")
