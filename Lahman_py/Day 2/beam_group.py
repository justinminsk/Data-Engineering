#!/usr/bin/env python2

import apache_beam as beam
import csv

header = ['nameFirst','nameLast','teamName','playerID','yearID','stint','teamID','lgID','G','AB','R','H','2B','3B','HR','RBI','SB','CS','BB','SO','IBB','HBP','SH','SF','GIDP']


def make_string(array):
	return (map(lambda tup: '{},{}'.format(tup[0],round(tup[1], 2)), array))


print '\n-----Starting Pipeline-----\n\n'

pipeline = beam.Pipeline('DirectRunner')

(
pipeline
|beam.io.ReadFromText('headless_battingext.csv')
|beam.Map(lambda line:next(csv.reader([line])))
|beam.Map(lambda d_array:dict(zip(header, d_array)))
|beam.Map(lambda d_dict:(d_dict['playerID'],int(d_dict['HR'])))
|beam.combiners.Count.PerKey()
|beam.Filter(lambda d_tup: int(d_tup[1]) >= 20)
|beam.combiners.ToList()
|beam.Map(lambda tup:sorted(tup, key = lambda tup:tup[1], reverse = True))
|beam.Map(make_string)
|beam.Map(lambda t_array:['playerID,SEASONS'] + t_array)
|beam.FlatMap(lambda x:x)
|beam.io.WriteToText('output',num_shards=1)
)

result = pipeline.run()
result.wait_until_finish()

print '\n\n-----Ending Pipeline-----\n'
