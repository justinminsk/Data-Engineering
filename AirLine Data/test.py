#!/usr/bin/env python2

header = ['nameFirst', 'nameLast', 'age']
data = ['Chad', 'Redmond', 52]

dict(zip(header, data))

data = [('Chad', 'Redmond', 52), ('Roger', 'Griffiths', 60), ('Don', 'Platte', 75)]

sorted(data, key = lambda tuple: tuple[2], reverse = True)