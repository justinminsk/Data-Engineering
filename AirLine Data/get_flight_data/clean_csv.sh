#!/bin/bash

for i in {1..12}
	do
		sed 's/"//g' < 2015${i}.csv | sed 's/,$//g' > temp.csv
		mv temp.csv 2015${i}.csv
		echo ${i} done
	done