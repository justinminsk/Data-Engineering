#!/bin/bash

for i in {2012..2016..4}
	do
	HTML="https://en.wikipedia.org/wiki/United_States_presidential_election,_${i}"
	PAGE=$(curl $HTML)
	echo $PAGE | sed 's/<tr style="background:#B0CEFF"> <td align="left"><a href="\/wiki\/United_States_presidential_election_in_\([[:alpha]]*\),_/\n 0,\1,  \n/g' > dem.txt
	echo $PAGE |  sed 's/<tr style="background:#FFB6B6"> <td align="left"><a href="\/wiki\/United_States_presidential_election_in_\([[:alpha:]]*\),_/\n 1,\1, \n/g' > rep.txt
	cat rep.txt | grep '1,[[:alpha:]]*,[[:digit:]]*' >> Pres_table.csv
	cat dem.txt | grep '0,[[:alpha:]]*,[[:digit:]]*' >> Pres_table.csv
	done
	