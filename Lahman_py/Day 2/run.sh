#!/bin/bash

echo '-----Starting Bash-----'

echo '-----Removing Old Files-----'
rm output.csv
./transform_data.py

echo '----Making CSV-----'
cat output-00000-of-00001 > output.csv
rm output-00000-of-00001


echo '-----Ending Bash-----'