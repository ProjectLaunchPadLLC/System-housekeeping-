#!/bin/bash

# Usage: ./large-files.sh <size-in-MB> <path>
# Example: ./large-files.sh 100 /mnt/c

SIZE_MB=$1
SCAN_PATH=$2

find "$SCAN_PATH" -type f -size +"${SIZE_MB}"M -printf "%p %k KB\n" | sort -nr -k2
