#!/bin/bash

echo "--Start--"

echo "Removing final_output"

rm final_output.csv
./test.py
cat output*>>temp
cat temp | grep 'nameFirst' > final_output.csv
sed '/nameFirst/d' < temp >> final_output.csv
echo "Removing Temp. Files"
rm temp
rm output*

echo "done"