#!/bin/sh

#set -x

# syntax pt.sh <servo-number> <movement=0to100>

echo $1=$2%>/dev/servoblaster

