#!/usr/bin/env python

import os
import seq_utils
import sys


def count_seqs1(data_path):
    filenames = sorted(os.listdir(data_path))
    os.chdir(data_path)
    for fileN in filenames:
	input_file = open(fileN)
        seq_count = seq_utils.count_seqs(input_file)
        print fileN, "has number of seqs :", seq_count

if len(sys.argv) < 2:
   sys.exit("Usage: count_all_seqs.py path to data")


count_seqs1(sys.argv[1])      
