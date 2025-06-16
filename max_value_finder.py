import sys
import csv

# 获取文件名
input_file = sys.argv[1]

# 打开并读取文件
with open(input_file, newline='') as f:
    reader = csv.reader(f, delimiter='\t')
    header = next(reader)

    # 输出新的表头
    print(f"{header[0]}\t{header[1]}\tMaxValue\tMaxColumn")

    # 逐行处理数据
    for row in reader:
        # 提取第3-7列数据（索引2~6）
        values = row[2:7]
        values_float = list(map(float, values))  # 转成浮点数

        max_val = max(values_float)
        max_idx = values_float.index(max_val)
        max_col_name = header[2 + max_idx]

        print(f"{row[0]}\t{row[1]}\t{max_val}\t{max_col_name}")
