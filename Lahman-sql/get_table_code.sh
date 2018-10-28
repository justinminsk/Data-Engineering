#!/bin/bash

LINE=$(cat lahman2016.sql)
echo $LINE > temp1
sed 's/\(CREATE TABLE `Batting`\)/\n\1/' < temp1 > temp2 
sed 's/CREATE TABLE `BattingPost`/\n/' < temp2 | grep 'CREATE TABLE `Batting`' > temp3
sed 's/ ENGINE.*/;/' > table_code.sql
rm temp1
rm temp2
rm temp3
