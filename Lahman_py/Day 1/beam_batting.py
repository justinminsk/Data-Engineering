#!/usr/bin/env python2

import apache_beam as beam
import csv

def get(array):
	return 

pipeline=beam.Pipeline('DirectRunner')


(
pipeline
|beam.io.ReadFromText('battingext.csv')
|beam.Map(lambda line:next(csv.reader([line])))
|beam.Map(lambda array:'{},{},{}'.format(array[0], array[1], array[14]))
|beam.io.WriteToText('output.csv')
)


result=pipeline.run()

result.wait_until_finish()