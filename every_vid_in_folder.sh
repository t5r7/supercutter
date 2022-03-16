#!/bin/bash

# loop over every webm file in the current folder
for v in *.webm; do
    python /mnt/c/Users/Tom/Git/Hub/itsmeimtom/supercutter/cutter.py "$v" "$v.json" "cut"
done