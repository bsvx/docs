#!/usr/bin/env python

import numpy
import matplotlib.pyplot as plot
import bsvxpy as bsv

n_files = 5

# here is where we'll handle grabbing field count.
# this compares the number of bsvx fields encoded
# into hex versus the predicted number of csv fields
# when strings are written as plaintext using comma
# delimitation.

# since certain strings contain commas, csv will
# incorrectly represent them as separate fields, 
# when in reality they are the same field.

# bsvx will have fewer (and the correct number of)
# fields when compared to csv
obj_lists = []

field_count_1 = bsv.Reader("data/test_input.bsvx")
obj_lists.append(field_count_1.read())

field_count_2 = bsv.Reader("data/test_string.bsvx")
obj_lists.append(field_count_2.read())

field_count_3 = bsv.Reader("data/test_string_size2.bsvx")
obj_lists.append(field_count_3.read())

field_count_4 = bsv.Reader("data/test_string_size4.bsvx")
obj_lists.append(field_count_4.read())

field_count_5 = bsv.Reader("data/test_string_size8.bsvx")
obj_lists.append(field_count_5.read())

csv_files = []
bsvx_files = []

for i in range(len(obj_lists)): # get length of each of the lists, i.e. however many fields are in the bsvx object
    bsvx_files.append(len(obj_lists[i]))

for i in range(len(obj_lists)): # iterate over the list of lists, and any time you find a comma add 1 to the number of fields
    count = len(obj_lists[i])
    for j in obj_lists[i]:
        if type(j.get_data()) is str:
            count = count + j.get_data().count(',')
    csv_files.append(count)

print(bsvx_files)
print(csv_files)

index = numpy.arange(n_files)
width = 0.3

plot.bar(index, csv_files, width, color='r', label='.csv File')
plot.bar(index + width, bsvx_files, width, color='b', label='.bsvx File')

plot.xlabel('Files')
plot.ylabel('Field Counts')
plot.title('A Comparison of .csv And .bsvx Field Counts')
plot.xticks(index + width / 2, ('A', 'B', 'C', 'D', 'E'))
plot.legend()

plot.savefig('figures/2.png')
