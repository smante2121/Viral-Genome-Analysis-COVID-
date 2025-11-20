# utils_vcf.py
import pandas as pd
import os
import re

def load_vcf(vcf_path):
    rows = []
    with open(vcf_path, 'r') as f:
        for line in f:
            if line.startswith("#"):
                continue
            
            fields = line.strip().split('\t')
            chrom, pos, id_, ref, alt, qual, flt, info = fields[:8]

            dp = None
            af = None

            # extract DP and AF from INFO field
            if "DP=" in info:
                dp = re.search(r"DP=(\d+)", info)
                dp = int(dp.group(1)) if dp else None

            if "AF=" in info:
                af = re.search(r"AF=([\d\.]+)", info)
                af = float(af.group(1)) if af else None

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
