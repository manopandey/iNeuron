#!/bin/bash

num=$(ls './Python Programming Basic Assignment'* | tail -1 | egrep -o [0-9]+)
cp "template.py" "Python Programming Basic Assignment "$((num+1))".py"

