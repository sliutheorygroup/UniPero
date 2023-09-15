for i in 50 60 70 80 90 100 110 120 130 140 150 160 170 180 190 200 210 220 230 240
do   
	mkdir $i
	cp  conf.lmp graph.pb input.lammps job.json $i
        cd $i
	sed -i "s/variable        TEMP            equal 50.000000/variable        TEMP            equal $i.000000/g" input.lammps
	lbg job submit -i job.json -p ./ >log1
	cd ..
done
