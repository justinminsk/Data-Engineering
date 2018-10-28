#!/bin/bash

for i in {1..12}
	do
		unzip 2015${i}.zip
		mv *ONTIME.csv 2015${i}.csv
		echo ${i} done
	done