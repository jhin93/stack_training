#!/usr/bin/env bash

DIR=$1
EXT=$2

ls "$DIR" | grep "\.$EXT$" | wc -l
