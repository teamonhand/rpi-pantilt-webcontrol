#!/bin/sh

set -x
PAN=4
TILT=3

# syntax pt.sh <4=pan;3=tilt> <movement=0to100>

echo $1=$2%>/dev/servoblaster
#echo 4=80%>/dev/servoblaster
