#!/usr/bin/env python2

import apache_beam as beam
import csv

pipeline = beam.Pipeline('DirectRunner')

(
pipeline
|beam.io.ReadFromText('headless_battingext.csv')
|beam.Map(lambda line:next(csv.reader([line])))
|beam.Map(lambda array:'{},{},{}'.format(array[0],array[1],array[2]))
|beam.io.WriteToText('outputsql.csv', num_shards=1)
)

result = pipeline.run()
result.wait_until_finish()