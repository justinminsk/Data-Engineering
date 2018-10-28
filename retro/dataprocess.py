#!/usr/bin/env python2

import apache_beam as beam
import csv

header = ['teamID', 'playerID', 'HRTotal']

argv = [
      '--project=justin-de-classwork',
      '--job_name=minsk',
      '--save_main_session',
      '--staging_location=gs://justinminsk_bucket/retrosheet/staging/',
      '--temp_location=gs://justinminsk_bucket/retrosheet/temp/',
      '--runner=DataflowRunner'
   ]

def make_string(array):
	return (map(lambda tup:'{},{},{}'.format(tup[0],str(tup[2]),tup[1]), array))
	

pipeline=beam.Pipeline(argv=argv)

side=(
pipeline
|'read roster'>>beam.io.ReadFromText('gs://justinminsk_bucket/retrosheet/roster')
|beam.Map(lambda line:next(csv.reader([line])))
|beam.Map(lambda array:(array[0],array[2] +  ' ' + array[1]))
)


(
pipeline
|beam.io.ReadFromText('gs://justinminsk_bucket/retrosheet/events')
|beam.Map(lambda line:next(csv.reader([line])))
|beam.Filter(lambda tuple: int(tuple[2]) == 23)
|beam.Map(lambda tuple:dict(zip(header,tuple)))
|beam.Map(lambda dict:(dict['playerID'],int(dict['HRTotal'])))
|beam.combiners.Count.PerKey()
|beam.Map(lambda tuple,d:(tuple[0],tuple[1],d[tuple[0].split(' ')[0]]),beam.pvalue.AsDict(side))
|beam.combiners.ToList()
|beam.Map(make_string)
|beam.Map(lambda array:['playerID,Name,HRTotal'] + array)
|beam.FlatMap(lambda x:x)
|beam.io.WriteToText('gs://justinminsk_bucket/retrosheet/Minsk',num_shards=1)
)


result=pipeline.run()
result.wait_until_finish()
