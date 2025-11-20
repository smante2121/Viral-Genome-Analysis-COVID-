#!/usr/bin/env python3
import os
import subprocess
import sys

# ---------------------------
# CONFIG
# ---------------------------
ANALYSIS_DIR = "analysis"
PLOTS_DIR = "plots"

SCRIPTS = [
    "coverage_plot.py",
    "variant_summary.py",
    "qual_depth_scatter.py",
    "snp_indel_breakdown.py",
    "mutation_lollipop.py",
    "spike_mutation_plot.py"
]

# ---------------------------
# UTILITY FUNCTIONS
# ---------------------------

def run_script(script_path):
    """Run a python script and stream its output."""
    print(f"\n▶ Running {script_path} ...")

    result = subprocess.run(
        [sys.executable, script_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Print results
    if result.stdout:
        print(result.stdout)

    # Error handling
    if result.stderr:
        print(f"⚠️  Error running {script_path}:")
        print(result.stderr)
        return False

    print(f"✔ Finished {script_path}")
    return True


# ---------------------------
# MAIN EXECUTION LOGIC
# ---------------------------

def main():
    print("=======================================")
    print("   SARS-CoV-2 VARIANT ANALYSIS PIPELINE")
    print("=======================================")

    # Ensure plots folder exists
    if not os.path.exists(PLOTS_DIR):
        os.makedirs(PLOTS_DIR)
        print(f"Created folder: {PLOTS_DIR}")

    # Run each analysis script
    for script in SCRIPTS:
        script_path = os.path.join(ANALYSIS_DIR, script)

        if not os.path.exists(script_path):
            print(f"❌ Missing script: {script_path}")
            continue

        success = run_script(script_path)
        if not success:
            print(f"❌ Stopping pipeline due to error in {script}")
            return

    print("\n=======================================")
    print("   All analysis scripts executed!")
    print("   Plots saved to: plots/")
    print("=======================================")


if __name__ == "__main__":
    main()
