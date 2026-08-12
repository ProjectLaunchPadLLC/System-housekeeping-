#!/bin/bash

# Usage: ./unused-files.sh <days> <path>
# Example: ./unused-files.sh 90 /mnt/c

DAYS=$1
SCAN_PATH=$2

find "$SCAN_PATH" -type f -atime +"$DAYS" -printf "%p %AD %k KB\n" | sort
