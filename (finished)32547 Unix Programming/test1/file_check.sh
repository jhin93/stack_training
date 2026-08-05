# !/usr/bin/env bash

if [ -f "$1" ]
then
    wc -l "$1"
else
    echo "File not found"
fi

