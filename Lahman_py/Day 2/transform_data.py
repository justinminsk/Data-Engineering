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

pipeline=beam.Pipeline(argv=argv)

side=(
pipeline
|'read bio'>>beam.io.ReadFromText('gs://justinminsk_bucket/baseball/Bio')
|beam.Map(lambda line:next(csv.reader([line])))
|beam.Map(lambda array:(array[0],array[1]))
)

base=(
pipeline
|beam.io.ReadFromText('gs://justinminsk_bucket/baseball/headless_battingext.csv')
|beam.Map(lambda line:next(csv.reader([line])))
|beam.Map(lambda array,header:dict(zip(header,array)),header)
|beam.Map(lambda d:('{} {} {}'.format(d['playerID'],d['nameFirst'],d['nameLast']),int(d['HR'])))
)


means=(
base
|'compute means'>>beam.combiners.Mean.PerKey()
)

counts=(
base
|'compute counts'>>beam.combiners.Count.PerKey()
)

(
means
|beam.Map(lambda tuple,d:(tuple[0],int(round(tuple[1]*d[tuple[0]],0))),beam.pvalue.AsDict(counts))
|beam.Map(lambda tuple,d:(tuple[0],tuple[1],d[tuple[0].split(' ')[0]]),beam.pvalue.AsDict(side))
|beam.Filter(lambda tuple:tuple[1]>=400)
|beam.combiners.ToList()
|beam.Map(lambda array:sorted(array,key=lambda tuple:tuple[1],reverse=True))
|beam.Map(to_Strings)
|beam.Map(lambda array:['id-name,career-homeruns,birth-year']+array)
|beam.FlatMap(lambda x:x)
|beam.io.WriteToText('gs://justinminsk_bucket/baseball/baseballHRs.csv')
)

result=pipeline.run()
result.wait_until_finish()