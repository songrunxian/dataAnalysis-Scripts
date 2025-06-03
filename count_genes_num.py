from collections import defaultdict

# 预定义你关心的染色体列表
chromosomes = [
    'Chr1', 'Chr2', 'Chr3', 'Chr4', 'Chr5', 'Chr6', 'Chr7',
    'Chr8', 'Chr9', 'Chr10', 'Chr11', 'Chr12', 'ChrSy', 'ChrUn'
]

# 创建一个计数字典
counts = defaultdict(int)

# 读取 GFF 文件
with open('find', 'r') as file:
    for line in file:
        # 跳过注释行
        if line.startswith('#'):
            continue
        fields = line.strip().split('\t')
        if fields and fields[0] in chromosomes:
            counts[fields[0]] += 1

# 打印结果
for chrom in sorted(chromosomes, key=lambda x: int(x[3:]) if x[3:].isdigit() else 100 + chromosomes.index(x)):
    print(f"{chrom}: {counts[chrom]}")

