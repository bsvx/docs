#!/usr/bin/env python

import numpy
import matplotlib.pyplot as plot

n_files = 5

# here is where we'll handle grabbing file sizes
# for now these values are placeholders

csv_files = [128, 256, 512, 1024, 2048]
bsvx_files = [64, 128, 256, 512, 1024]

index = numpy.arange(n_files)
width = 0.3

plot.bar(index, csv_files, width, color='r', label='.csv File')
plot.bar(index + width, bsvx_files, width, color='b', label='.bsvx File')

plot.xlabel('Files')
plot.ylabel('File Size (in MB)')
plot.title('A Comparison of .csv And .bsvx File Sizes')
plot.xticks(index + width / 2, ('A', 'B', 'C', 'D', 'E'))
plot.legend()

plot.savefig('figures/1.png')
