#!/usr/bin/env python2

import apache_beam as beam
import csv

header = ['nameFirst','nameLast','teamName','playerID','yearID','stint','teamID','lgID','G','AB','R','H','2B','3B','HR','RBI','SB','CS','BB','SO','IBB','HBP','SH','SF','GIDP']

test = [('John', 'Abadie', '0'), ('John', 'Abadie', '0'), ('Frank', 'Abercrombie', '0')]


def make_string(array):
	return (map(lambda tup:','.join(tup), array))


print '\n-----Starting Pipeline-----\n\n'

pipeline = beam.Pipeline('DirectRunner')

(
pipeline
|beam.io.ReadFromText('headless_battingext.csv')
|beam.Map(lambda line:next(csv.reader([line])))
|beam.Map(lambda array, header:dict(zip(header, array)),header)
|beam.Map(lambda d_dict:(d_dict['nameFirst'],d_dict['nameLast'],d_dict['HR'],d_dict['yearID']))
|beam.Filter(lambda d_tup: int(d_tup[2]) >= 50)
|beam.combiners.ToList()
|beam.Map(lambda tup:sorted(tup, key = lambda tup:tup[3], reverse = True))
|beam.Map(make_string)
|beam.Map(lambda t_array:['nameFirst,nameLast,HR'] + t_array)
|beam.FlatMap(lambda x:x)
|beam.io.WriteToText('output',num_shards=1)
)

result = pipeline.run()
result.wait_until_finish()

print '\n\n-----Ending Pipeline-----\n'
