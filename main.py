#!/usr/bin/env python3
import os
import subprocess
import sys

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

def run_script(script_path):
    """Run a single analysis script and stream its output."""
    print(f"\n▶ Running {script_path} ...")

    result = subprocess.run(
        [sys.executable, script_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Stdout
    if result.stdout.strip():
        print(result.stdout)

    # Stderr handling
    if result.stderr.strip():
        print(f"⚠️ Error in {script_path}:")
        print(result.stderr)
        return False

    print(f"✔ Finished {script_path}")
    return True


def check_dependencies():
    """Warn user if key Python modules are missing."""
    print("\n🔍 Checking dependencies...")

    required = ["pandas", "matplotlib", "numpy", "Bio"]
    missing = []

    for pkg in required:
        try:
            __import__(pkg)
        except ImportError:
            missing.append(pkg)

    if missing:
        print("\n❌ Missing required packages:")
        for m in missing:
            print(f"   - {m}")
        print("\nInstall them with:")
        print("   pip install " + " ".join(missing))
        sys.exit(1)
    else:
        print("✔ All dependencies found.")


def main():
    print("=======================================")
    print("  SARS-CoV-2 VARIANT ANALYSIS PIPELINE")
    print("=======================================\n")

    # Check dependencies
    check_dependencies()

    # Ensure plots folder exists
    if not os.path.exists(PLOTS_DIR):
        os.makedirs(PLOTS_DIR)
        print(f"Created folder: {PLOTS_DIR}")

    # Run analysis scripts in order
    for script in SCRIPTS:
        script_path = os.path.join(ANALYSIS_DIR, script)

        if not os.path.exists(script_path):
            print(f"❌ Missing script: {script_path}")
            continue

        success = run_script(script_path)
        if not success:
            print(f"\n❌ Pipeline stopped due to error in {script}")
            return

    print("\n=======================================")
    print("  ALL ANALYSIS COMPLETED SUCCESSFULLY!")
    print(f"  Plots saved in: {PLOTS_DIR}/")
    print("  Annotated variants saved in: variant_table_annotated.csv")
    print("=======================================\n")


if __name__ == "__main__":
    main()
