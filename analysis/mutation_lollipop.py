# mutation_lollipop.py
from utils_vcf import load_vcf
import matplotlib.pyplot as plt
import os

os.makedirs("plots", exist_ok=True)

df = load_vcf("variants_filtered.vcf")

plt.figure(figsize=(18,4))

plt.stem(df["POS"], [1]*len(df), basefmt=" ", linefmt="purple", markerfmt="o")

plt.title("Genome-wide Mutation Map")
plt.xlabel("Genome Position")
plt.yticks([])
plt.tight_layout()
plt.savefig("plots/lollipop_plot.png", dpi=300)

print("Saved enhanced genome-wide lollipop plot.")
