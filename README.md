# dataAnalysis-Scripts
A personal collection of frequently used scripts for bioinformatics analysis.

## Overview
This repository contains reusable code scripts commonly used in my daily bioinformatics workflows, including data merging, visualization, statistical analysis, and pre-processing. Each script is designed to be modular, command-line friendly, and easy to integrate into pipelines.

## Scripts Included

### 1. `fullJoinFiles.R`
Performs a **full join** of multiple TSV files based on a specified column (e.g., `geneID`).

- Input: Two or more `.tsv` files
- Output: A merged `.tsv` file with all data retained
- Use case: Merging gene expression data from multiple experiments

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
**Usage example:**
```bash
python merge_fastq_side_by_side.py --pattern _1.clean.fq.gz
```

### 5. `对自制的maf进行去重`
peak1  chr1  100  200
peak2  chr1  150  250  # overlap with peak1
peak3  chr1  260  300
↓
peak1  chr1  100  200
peak3  chr1  260  300

### 6. `提取maf的交集部分`
peak1  chr1  100  200
peak2  chr1  150  250
↓
chr1  150  200

### 7. `max_value_finder.py` 
直接检索到特征贡献最大的那么特征：
![1750044512038](https://github.com/user-attachments/assets/a6f4298a-8f73-4101-863e-92adcb5aeac8)
这个格式 直接找到

### 8. `Rscript:Differential Expression: Up vs Down`
![1749695856989](https://github.com/user-attachments/assets/1239ee9d-03ae-4c3e-89ca-e65dbf7285e6)

### 9.`如何统计reads的长度分布？`

### 10.`字典替换`
awk 'NR==FNR {dict[$1] = $2; next} {for (i=1; i<=NF; i++) if ($i in dict) $i = dict[$i]; print}' relationship_HZ_msu.txt loc_yang.txt > loc_yated.txt



# How_to_train_gene_network_with_xgboost
This is my work Log
