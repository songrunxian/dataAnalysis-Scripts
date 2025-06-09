# dataAnalysis-Scripts
A personal collection of frequently used scripts for bioinformatics analysis.

## 📂 Overview
This repository contains reusable code scripts commonly used in my daily bioinformatics workflows, including data merging, visualization, statistical analysis, and pre-processing. Each script is designed to be modular, command-line friendly, and easy to integrate into pipelines.

## 📜 Scripts Included

### 1. `fullJoinFiles.R`
Performs a **full join** of multiple TSV files based on a specified column (e.g., `geneID`).

- ✅ Input: Two or more `.tsv` files
- ✅ Output: A merged `.tsv` file with all data retained
- ✅ Use case: Merging gene expression data from multiple experiments

**Usage example:**
```bash
Rscript fullJoinFiles.R file1.tsv file2.tsv file3.tsv geneID output.tsv
```

### 2. `extract_matching_rows_by_geneid.py`
This script extracts all rows from a large tab-delimited file where the first-column gene IDs match those listed in `comm.txt`, and writes them to a new output file.

### 3. `count_genes_num.py`
how many genes are located on each chromosome, assuming:
Each line of the file corresponds to one gene.
The first column contains the chromosome number or ID

### 4. `merge_fastq_side_by_side.py`
Function:
Scan all *_1.fq.gz files in the current directory, find the corresponding *_2.fq.gz files,
and output each paired filename as a tab-separated line into the file paired_file_list.txt.
Example output:
B-Ctrl-cs_L1_1.fq.gz    B-Ctrl-cs_L1_2.fq.gz

# How_to_train_gene_network_with_xgboost
This is my work Log
