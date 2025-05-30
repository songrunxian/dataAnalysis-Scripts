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

### 2. `How_to_train_gene_network_with_xgboost`
This is my work Log by AI 
