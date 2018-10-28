#!/usr/bin/env python2

import csv
rlist=[]
file=open('numbers.csv', 'r')
reader=csv.reader(file)
for line in reader:
	rlist += [line]
print rlist
file.close()