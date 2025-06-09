#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import os
import argparse

parser = argparse.ArgumentParser(description="Generate paired-end file list based on given R1 suffix pattern.")
parser.add_argument('--pattern', type=str, required=True,
                    help="Suffix pattern for R1 files, e.g., '_1.fq.gz' or '_1.clean.fq.gz'")
args = parser.parse_args()

suffix = args.pattern
fq1_files = sorted(glob.glob(f"*{suffix}"))

with open("paired_file_list.txt", "w") as out:
    for fq1 in fq1_files:
        fq2 = fq1.replace(suffix, suffix.replace("_1", "_2"))
        if os.path.exists(fq2):
            out.write(f"{fq1}\t{fq2}\n")
        else:
            print(f"❌ Missing pair for: {fq1} → expected {fq2}")

print("✅paired_file_list.txt generated.")
