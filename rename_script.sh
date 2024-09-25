#!/bin/bash

find . -type f -name 'D17_*' | while read FILE ; do
    newfile="$(echo ${FILE} |sed -e 's/D17_//')" ;
    mv "${FILE}" "${newfile}" ;
done 
