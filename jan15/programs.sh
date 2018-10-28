#!/bin/bash

RESULT=$(grep "History" < programs.html)

FINAL=$(echo $RESULT | sed 's/History/his/g') 

echo $FINAL
