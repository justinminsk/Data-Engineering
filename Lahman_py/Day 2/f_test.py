#!/usr/bin/env python2

import apache_beam as beam
import csv

argv = [
      '--project=justin-de-classwork',
      '--job_name=batinghrs',
      '--save_main_session',
      '--staging_location=gs://justinminsk_bucket/baseball/staging/',
      '--temp_location=gs://justinminsk_bucket/baseball/temp/',
      '--runner=DataflowRunner'
   ]


header=['nameFirst','nameLast','teamName','playerID','yearID','stint','teamID','lgID','G','AB','R','H','Doubles','Triples','HR','RBI','SB','CS','BB','SO','IBB','HBP','SH','SF','GIDP']

def to_Strings(array):
    return(map(lambda tuple:'{},{},{}'.format(tuple[0],tuple[1],tuple[2]),array))

pipeline=beam.Pipeline('DirectRunner')

(
pipeline
|'read bio'>>beam.io.ReadFromText('gs://justinminsk_bucket/baseball/Bio')
|beam.Map(lambda line:next(csv.reader([line])))
|beam.Map(lambda array:(array[0],array[1]))
|beam.io.WriteToText('output',num_shards=1)
)

result=pipeline.run()
result.wait_until_finish()