#!/usr/bin/env python2

import apache_beam as beam
import csv

array = ['John','Abadie','Philadelphia Centennials','abadijo01','1875','1','PH3','NA','11','45','3','10','0','0','0','4','1','0','0','3','','','','','']

def get_ba(array):
	try:
		AB = float(array[9])
		H = float(array[11])
		BA = str(round(H / AB, 3))
		return array[:12] + [BA] + array[13:]
	except ValueError:
		return array[:12] + ['BA'] + array[13:]
	except ZeroDivisionError:
		return array[:12] + ['undefined'] + array[13:]


argv = [
      '--project=justin-de-classwork',
      '--job_name=battingaverage',
      '--save_main_session',
      '--staging_location=gs://justinminsk_bucket/baseball/staging/',
      '--temp_location=gs://justinminsk_bucket/baseball/temp/',
      '--runner=DataflowRunner'
]		

print '...Starting Pipeline'	

pipeline = beam.Pipeline(argv=argv)

(
pipeline
|beam.io.ReadFromText('gs://justinminsk_bucket/baseball/bdata.csv')
|beam.Map(lambda line:next(csv.reader([line])))
|beam.Map(get_ba)
|beam.Map(lambda array:','.join(array))
|beam.io.WriteToText('gs://justinminsk_bucket/baseball/output.csv')
)

result=pipeline.run()

result.wait_until_finish()

print '--Done--'
