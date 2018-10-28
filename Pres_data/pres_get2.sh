#!/bin/bash
for i in {2012..2016..4}
	do
	HTML="https://en.wikipedia.org/wiki/United_States_presidential_election,_${i}"
	PAGE=$(curl $HTML)
	echo $PAGE | sed 's/\(<table class="wikitable sortable" style="text-align:right">\)/\n\1/g' | sed 's/<th>U.S. Total<\/th>/\n/g' > temp.txt
	cat temp.txt | grep '<table class="wikitable sortable" style="text-align:right">' > table.txt
	cat table.txt | sed 's/\(<tr style="background:#B0CEFF">\)/\n\1/g' | sed 's/<td>WTA<\/td>/\n/g' | grep '<tr style="background:#B0CEFF">' > dem_table.txt
	cat table.txt | sed 's/\(<tr style="background:#FFB6B6">\)/\n\1/g' | sed 's/<td>WTA<\/td>/\n/g' | grep '<tr style="background:#FFB6B6">' > rep_table.txt
	cat rep_table.txt | sed 's/>/\n get this /g' | sed 's/>/\n get this /g' | sed 's/Nebraska, 3rd<\/a//g' | sed 's/Nebraska, 2nd<\/a//g'  | sed 's/Nebraska, 1st<\/a//g' | sed 's/Maine, 1st<\/a//g' | sed 's/Maine, 2nd<\/a//g' > rep_table2.txt
	cat rep_table2.txt | sed 's/\([[:alpha:]]<\/a\)/\1\ getthis/g' | grep 'getthis' > rep_table3.txt
	cat rep_table3.txt | sed 's/getthis//g' | sed 's/get this//g' > final_rep.txt
	cat final_rep.txt | sed "s/\([[:alpha:]]\)<\/a/\1, ${i}, 1/g" > add_to_table.txt
	cat add_to_table.txt >> Presidental_table.csv
	cat dem_table.txt | sed 's/>/\n get this /g' | sed 's/Nebraska, 3rd<\/a//g' | sed 's/Nebraska, 2nd<\/a//g'  | sed 's/Nebraska, 1st<\/a//g' | sed 's/Maine, 2nd<\/a//g' | sed 's/Maine, 1st<\/a//g' > dem_table2.txt
	cat dem_table2.txt | sed 's/\([[:alpha:]]<\/a\)/\1 getthis/g' | grep 'getthis' > dem_table3.txt
	cat dem_table3.txt | sed 's/getthis//g' | sed 's/get this//g' > final_dem.txt
	cat final_dem.txt | sed "s/\([[:alpha:]]\)<\/a/\1, ${i}, 0/g" > add_to_table.txt
	cat add_to_table.txt >> Presidental_table.csv
	done

rm temp.txt
rm table.txt
rm rep_table.txt
rm rep_table2.txt
rm rep_table3.txt 
rm dem_table.txt
rm dem_table2.txt 
rm dem_table3.txt
rm final_dem.txt
rm final_rep.txt
rm add_to_table.txt

# add line head for the csv
# state, year, Republican