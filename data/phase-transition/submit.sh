#!/bin/bash

for i in ; do
    if [ -f "$i/cp.sh" ]; then
        cd "$i"
        chmod +x cp.sh
        ./cp.sh 
        cd ..
    fi
done

wait
echo "All submissions completed."
