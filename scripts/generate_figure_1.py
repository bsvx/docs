#!/usr/bin/env python

import numpy
import matplotlib.pyplot as plot
import os
from pathlib import Path

n_files = 5

# here is where we'll handle grabbing file sizes
# bsvx file sizes are larger than csv, but they
# solve the issue of comma delimitation

csv_files = ["test_input.csv", "test_string.csv", "test_string_size2.csv", "test_string_size4.csv", "test_string_size8.csv"]
bsvx_files = ["test_input.bsvx", "test_string.bsvx", "test_string_size2.bsvx", "test_string_size4.bsvx", "test_string_size8.bsvx"]
data_folder = Path("data/")

csv_file_sizes = []
bsvx_file_sizes = []

for c in csv_files:
    csv_file_sizes.append(os.path.getsize(data_folder / c))

for b in bsvx_files:
    bsvx_file_sizes.append(os.path.getsize(data_folder / b))

print(csv_file_sizes)

index = numpy.arange(n_files)
width = 0.3

plot.bar(index, csv_file_sizes, width, color='r', label='.csv File')
plot.bar(index + width, bsvx_file_sizes, width, color='b', label='.bsvx File')

plot.xlabel('Files')
plot.ylabel('File Size (in bytes)')
plot.title('A Comparison of .csv And .bsvx File Sizes')
plot.xticks(index + width / 2, ('A', 'B', 'C', 'D', 'E'))
plot.legend()

plot.savefig('figures/1.png')
