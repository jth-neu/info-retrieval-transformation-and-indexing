#!/usr/bin/env bash
if [ "$1" != "" ] && [ $2 -gt 0 ]
then
	python3 Indexing.py "$1" $2
else
	echo Invalid input.
fi