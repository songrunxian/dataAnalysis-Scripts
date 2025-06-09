#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import os

fq1_files = sorted(glob.glob("*_1.fq.gz"))

with open("paired_file_list.txt", "w") as out:
    for fq1 in fq1_files:
        fq2 = fq1.replace("_1.fq.gz", "_2.fq.gz")
        if os.path.exists(fq2):
            out.write(f"{fq1}\t{fq2}\n")
        else:
            print(f"No：{fq2}")

print("make file: paired_file_list.txt")
