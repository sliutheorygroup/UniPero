#!/bin/bash
 

for i in ; do
    if [ -f "$i/avg-dump.sh" ]; then
        cd $i
        chmod +x avg-dump.sh
        bash ./avg-dump.sh &
        cd ..
    fi
done

wait
echo "All average structures calculation completed."
