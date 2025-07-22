# dataAnalysis-Scripts
A personal collection of frequently used scripts for bioinformatics analysis.

## Overview
This repository contains reusable code scripts commonly used in my daily bioinformatics workflows, including data merging, visualization, statistical analysis, and pre-processing. Each script is designed to be modular, command-line friendly, and easy to integrate into pipelines.

## Scripts Included

### 1. `extract_information_from_uniport.py`

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

def load_mapping(dict_file):
    mapping = {}
    with open(dict_file, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:
                old, new = parts[0], parts[1]
                mapping[old] = new
    return mapping

def replace_text(input_file, output_file, mapping):
    with open(input_file, 'r', encoding='utf-8') as fin, \
         open(output_file, 'w', encoding='utf-8') as fout:
        for line in fin:
            for old, new in mapping.items():
                line = line.replace(old, new)
            fout.write(line)

if __name__ == "__main__":
    dict_path = 'relationship_HZ_msu.txt'
    input_path = 'all_yin'
    output_path = 'all_yin_replaced.txt'

    mapping = load_mapping(dict_path)
    replace_text(input_path, output_path, mapping)

    print("替换完成，结果保存在:", output_path)

### 11.`偶数行变成奇数行第二列`
# 假设输入文件名为 input.txt，输出到 output.txt

output_lines = []

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f]

for i in range(0, len(lines), 2):
    if i + 1 < len(lines):
        # 偶数行存在，合并为一行
        first_cols = lines[i].split()
        second_line = lines[i + 1]
        if len(first_cols) >= 1:
            merged_line = f"{first_cols[0]}\t{second_line}"
            output_lines.append(merged_line)
        else:
            # 如果奇数行是空的
            output_lines.append(second_line)
    else:
        # 最后一行是奇数行且没有对应偶数行
        output_lines.append(lines[i])

# 写入输出文件
with open("output.txt", "w") as f:
    for line in output_lines:
        f.write(line + "\n")

### 12.`格式转换`
<img width="944" height="616" alt="1753154518661" src="https://github.com/user-attachments/assets/b4a4d1b2-7c6c-48df-8604-b0001968070a" />
awk '{a[$2] = (a[$2] ? a[$2] "," $1 ":" $3 : $1 ":" $3)} END {for (i in a) print i, a[i]}' OFS='\t' your_file.txt








# How_to_train_gene_network_with_xgboost
This is my work Log
