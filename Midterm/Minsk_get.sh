HTML="http://static.hurstathletics.com/custompages/MBasketball/2016-17/plyr_00.htm"
PAGE=$(curl $HTML)
echo $PAGE > Minsk.txt
cat Minsk.txt | sed 's/\r//g' > Minsk1.txt
cat Minsk1.txt | sed 's/\(<tr bgcolor="#ffffff">\)/\n\1/g' | sed 's/<\/tr>//g' | grep '<tr bgcolor="#ffffff">' | sed 's/3FG//g' > Minsk2.txt
cat Minsk2.txt | sed 's/&nbsp;<\/td>//g' | sed 's/<td align=left><font face=verdana size=1 color="#000000">\([[:digit:]].*\)/\n get \1 \n/g' > Minsk3.txt
cat Minsk3.txt | sed 's/<td align=right><font face=verdana size=1 color="#000000">\([[:digit:]].[[:digit:]]\)/\n get \1/g' | sed 's/get [[:digit:]].[[:digit:]] <td align=right><font face=verdana size=1 color="#000000">//g' | sed 's/<td align=right><font face=verdana size=1 color="#000000">\([[:digit:]][[:digit:]].[[:digit:]]\)/\n get \1/g' > Minsk4.txt
cat Minsk4.txt | sed 's/<td align=center><font face=verdana size=1 color="#000000">/\n/g' | sed 's/get 1.000 <td align=right><font face=verdana size=1 color="#000000">[[:digit:]]//g' | grep 'get' > Minsk5.txt
cat Minsk5.txt | sed 's/get 9.5   <tr><td> <table border=0 cellspacing=0 cellpadding=2>//g' | sed 's/get [[:digit:]][[:digit:]][[:digit:]]//g' | sed 's/get 1.000//g' | tr -d "\n" > Minsk6.txt
cat Minsk6.txt | sed 's/ get \([[:digit:]][[:digit:]]\/[[:digit:]][[:digit:]]\/[[:digit:]][[:digit:]]\)/\1, /g' | sed 's/ get \([[:digit:]]\/[[:digit:]]\/[[:digit:]][[:digit:]]\)/\1, /g' | sed 's/ get \([[:digit:]]\/[[:digit:]][[:digit:]]\/[[:digit:]][[:digit:]]\)/\1, /g' | sed 's/ get \([[:digit:]].[[:digit:]]\)/\1 \n/g' | sed 's/ get \([[:digit:]][[:digit:]].[[:digit:]]\)/\1 \n/g' > Minskf.txt
cat Minskf.txt | sed 's/ //g' | sed 's/\(11\/11\/16,7.0\)/date,avg\n\1/'> Minsk.csv

rm Minsk.txt
rm Minsk1.txt
rm Minsk2.txt
rm Minsk3.txt
rm Minsk4.txt
rm Minsk5.txt
rm Minsk6.txt
rm Minskf.txt