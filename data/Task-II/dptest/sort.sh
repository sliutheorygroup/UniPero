#!/bin/bash

count=0

for file in *.f.out; do
    new_name=$(printf "%03d.f.out" "$count")
    mv "$file" "$new_name"
    ((count++))
done

