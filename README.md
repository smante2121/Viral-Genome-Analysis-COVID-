# 🧬 Viral Genome Analysis Pipeline (SARS-CoV-2)

This repository contains a complete end-to-end SARS-CoV-2 variant-calling pipeline following the workflow taught in class. It covers downloading reference data, processing raw FASTQ reads, alignment, variant calling, filtering, and generating visual summaries of the results.

All steps use standard bioinformatics tools: **SRA Toolkit, Bowtie2, Samtools, and BCFtools**, along with **Python** for visualization.

---

## 📥 1. Downloading the Reference Genome (FASTA)

**Source:**  
https://www.ncbi.nlm.nih.gov/nuccore/NC_045512.2

**Steps:**
1. Click **FASTA** in the top-left corner.  
2. In the top-right **Send To** dropdown:  
   - Destination: `File`  
   - Format: `FASTA`  
   - Record: `Full record`  
3. Save the file (e.g., `sequence.fasta`)  

**Move file into the project folder:**
```bash
cd /Users/sophiamantegari/ViralGenomeAnalysis
mv ~/Downloads/sequence.fasta ./sarscov2_reference.fasta
```

**Check the first few lines:**
```bash
head sarscov2_reference.fasta
```

You should see:
```
>NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome
ATTAAAGGTTTATACCTTCCCAGGT...
```

**Verify genome length:**
```bash
grep -v '^>' sarscov2_reference.fasta | tr -d '\n' | wc -c
```

Expected length:
```
29903
```

---

## 📥 2. Downloading FASTQ Reads (SRA)

**Sample Used:**  
https://www.ncbi.nlm.nih.gov/sra/?term=SRR14522714

### Install SRA Toolkit (if needed)
Check installation:
```bash
which fasterq-dump
```

If missing:
```bash
curl --output sratoolkit.tar.gz https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-mac64.tar.gz
tar -vxzf sratoolkit.tar.gz
echo 'export PATH=/Users/sophiamantegari/ViralGenomeAnalysis/sratoolkit.3.2.1-mac-x86_64/bin:$PATH' >> ~/.zshrc
source ~/.zshrc
```

### Download FASTQ files:
```bash
fasterq-dump SRR14522714
```

**Output:**
```
SRR14522714_1.fastq
SRR14522714_2.fastq
```

### Run FastQC
```bash
brew install fastqc
fastqc SRR14522714_1.fastq SRR14522714_2.fastq
rm *_fastqc.zip
```

---

## 🏗 3. Build Bowtie2 Index

```bash
which bowtie2
bowtie2-build sarscov2_reference.fasta sarscov2_reference
```

**Index files created:**
- sarscov2_reference.1.bt2  
- sarscov2_reference.2.bt2  
- sarscov2_reference.3.bt2  
- sarscov2_reference.4.bt2  
- sarscov2_reference.rev.1.bt2  
- sarscov2_reference.rev.2.bt2  

---

## 🎯 4. Align Paired-End Reads

```bash
bowtie2 -x sarscov2_reference  -1 SRR14522714_1.fastq  -2 SRR14522714_2.fastq  -S aligned.sam
```

**Output Summary:**
```
82.95% overall alignment rate
```

---

## 🔄 5. Convert SAM → BAM → Sorted BAM

```bash
samtools view -S -b aligned.sam > aligned.bam
samtools sort aligned.bam -o aligned.sorted.bam
samtools index aligned.sorted.bam
```

---

## 📊 6. Coverage Analysis

```bash
samtools depth aligned.sorted.bam > depth.txt
```

Used later for Python visualization.

---

## 🧬 7. Variant Calling with BCFtools

### Pileup
```bash
bcftools mpileup -f sarscov2_reference.fasta aligned.sorted.bam -Ob -o raw.bcf
```

### Call variants
```bash
bcftools call -mv -Ob -o variants_raw.bcf raw.bcf
bcftools view variants_raw.bcf > variants_raw.vcf
```

---

## 🎚 8. Variant Filtering

```bash
bcftools filter -i 'DP>=10 && QUAL>=30' variants_raw.vcf > variants_filtered.vcf
```

This produces the final high-confidence variant file.

---

## 📈 9. Plot Descriptions

### **1. Coverage Plot (Smoothed Genome-Wide Depth)**
Shows sequencing depth across the viral genome. High depth = high confidence in variant calls.

### **2. Coverage Depth Histogram (Log-Scale)**
Shows overall depth distribution across all positions. Median marked with a red line.

### **3. QUAL vs Depth Scatter Plot**
Each point is a variant. Higher depth tends to produce higher quality scores.

### **4. SNP vs Indel Bar Plot**
Breaks down variant types. SARS-CoV-2 is typically SNP-heavy.

### **5. Genome-Wide Lollipop Plot**
Marks exact mutation positions across the genome.

### **6. Spike Region Mutation Plot**
Shows which mutations fall inside the Spike protein’s genomic coordinates.

---

## 🧪 Tools Used
- SRA Toolkit  
- Bowtie2  
- Samtools  
- BCFtools  
- Python + Matplotlib + Pandas  

---

## 📁 Project Structure

```
ViralGenomeAnalysis/
│
├── sarscov2_reference.fasta
├── SRR14522714_1.fastq
├── SRR14522714_2.fastq
├── aligned.sorted.bam
├── depth.txt
├── variants_filtered.vcf
│
├── analysis/
│   ├── coverage_plot.py
│   ├── snp_indel_breakdown.py
│   ├── qual_depth_scatter.py
│   ├── mutation_lollipop.py
│   ├── spike_mutation_plot.py
│   └── utils_vcf.py
│
├── plots/
│   └── (generated PNG plots)
│
└── main.py
```

---

## ✅ Summary
This project implements a full SARS-CoV-2 sequencing workflow:
- Download data  
- Align reads  
- Call variants  
- Filter variants  
- Visualize coverage and mutation patterns  

The pipeline is fully reproducible and aligned with class expectations.

