#!/bin/bash

CURRENT=`pwd`

for j in 10 20 30 40 50 60 70 80 90 100 110 120 130 140 150 200 250 300 350 400 450 500 550 600 650 700
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
    echo $j $latt >> $CURRENT/Tvslat.dat
    cd $CURRENT
done

python sort.py
