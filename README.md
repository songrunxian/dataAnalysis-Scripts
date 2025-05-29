# dataAnalysis-Scripts
A personal collection of frequently used scripts for bioinformatics analysis.

## 📂 Overview
This repository contains reusable R scripts commonly used in my daily bioinformatics workflows, including data merging, visualization, statistical analysis, and pre-processing. Each script is designed to be modular, command-line friendly, and easy to integrate into pipelines.

## 📜 Scripts Included

### 1. `fullJoinFiles.R`
Performs a **full join** of multiple TSV files based on a specified column (e.g., `geneID`).

- ✅ Input: Two or more `.tsv` files
- ✅ Output: A merged `.tsv` file with all data retained
- ✅ Use case: Merging gene expression data from multiple experiments

**Usage example:**
```bash
Rscript fullJoinFiles.R file1.tsv file2.tsv file3.tsv geneID output.tsv
