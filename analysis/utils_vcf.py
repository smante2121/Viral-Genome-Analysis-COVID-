# utils_vcf.py
import pandas as pd
import re

def load_vcf(vcf_path):
    rows = []
    with open(vcf_path, "r") as f:
        for line in f:
            if line.startswith("#"):
                continue

            fields = line.strip().split("\t")
            chrom, pos, vid, ref, alt, qual, flt, info = fields[:8]

            dp = None
            af = None

            if "DP=" in info:
                dp_match = re.search(r"DP=(\d+)", info)
                dp = int(dp_match.group(1)) if dp_match else None

            if "AF=" in info:
                af_match = re.search(r"AF=([\d.]+)", info)
                af = float(af_match.group(1)) if af_match else None

            rows.append({
                "CHROM": chrom,
                "POS": int(pos),
                "REF": ref,
                "ALT": alt,
                "QUAL": float(qual),
                "DP": dp,
                "AF": af
            })

    return pd.DataFrame(rows)
