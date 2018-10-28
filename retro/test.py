#!/usr/bin/env python2

import apache_beam as beam
import csv

header = ['yearID', 'playerID', 'HRTotal']

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
	

pipeline=beam.Pipeline('DirectRunner')

"""
side=(
pipeline
|'read roster'>>beam.io.ReadFromText('roster')
|beam.Map(lambda line:next(csv.reader([line])))
|beam.Map(lambda array:(array[0],array[2] +  ' ' + array[1]))
)
 """

(
pipeline
|beam.io.ReadFromText('events')
|beam.Map(lambda line:next(csv.reader([line])))
|beam.Filter(lambda tuple: int(tuple[2]) == 23)
|beam.Map(lambda tuple:dict(zip(header,tuple)))
|beam.Map(lambda d:('{},{}'.format(d['yearID'][3:9],d['playerID']),int(d['HRTotal'])))
|beam.combiners.Count.PerKey()
|beam.combiners.ToList()
|beam.Map(lambda list:dict(zip(['playerID','HRTotal'],list)))
|beam.Map(lambda dict:dict[0][7:], dict[1])
#|beam.Map(lambda tuple:dict(zip(header,tuple)))
#|beam.Map(lambda dict:(dict['playerID'],int(dict['HRTotal'])))
#|beam.Map(lambda tuple,d:(tuple[0],tuple[1],d[tuple[0].split(' ')[0]]),beam.pvalue.AsDict(side))
|'second to list'>>beam.combiners.ToList()
#|beam.Map(make_string)
#|beam.FlatMap(lambda x:x)
|beam.io.WriteToText('output',num_shards=1)
)


result=pipeline.run()
result.wait_until_finish()
