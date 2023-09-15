#!/bin/bash

CURRENT=`pwd`

for j in $(seq 50 10 200)
do
  cd $j 
  a=$(grep -o -E 'JOB ID: [0-9]+' log1 | awk '{print $NF}')
  lbg job download $a
  cd $a
  mv traj.lammpstrj ../
  rm -rf $a
    rm lat.dat
    nline=$((5009 * 250))
    tail -$nline  traj.lammpstrj >> traj-last.lammpstrj
    python ../avg-dump.py traj-last.lammpstrj traj-last$j.xsf
    rm traj-last.lammpstrj
    latt=$(tail -1 lat.dat)
    echo $a $latt >> $CURRENT/Tvslat.dat
    cd $CURRENT
done

python sort.py
