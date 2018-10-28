#!/usr/bin/env python2

import apache_beam as beam
import csv

def sqaure(line):
	num_line=map(lambda x:int(x), line)
	sqaures=map(lambda x: x**2, num_line)
	return map(lambda x: str(x),sqaures)
	


pipeline=beam.Pipeline('DirectRunner')


(
pipeline
|beam.io.ReadFromText('numbers.csv')
|beam.Map(lambda line:next(csv.reader([line])))
|beam.Map(lambda array: sqaure(array))
|beam.Map(lambda array:','.join(array))
|beam.io.WriteToText('output.csv')
)


result=pipeline.run()

result.wait_until_finish()