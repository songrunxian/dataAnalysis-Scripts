gene_list_file = "comm.txt"
data_file = "GO_machineLearn_train_yinji.txt"
output_file = "GO_filtered.txt"

with open(gene_list_file, 'r') as f:
    gene_ids = set(line.strip() for line in f if line.strip())

with open(data_file, 'r') as fin, open(output_file, 'w') as fout:
    header = fin.readline()
    fout.write(header)

    count = 0
    for line in fin:
        gene_id = line.split('\t', 1)[0]
        if gene_id in gene_ids:
            fout.write(line)
            count += 1

print(f"write {count}  items，save in {output_file}")
