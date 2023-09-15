for i in 10 20 30 40 50 60 70 80 90 100 110 120 130 140 150 200 250 300 350 400 450 500 550 600 650 700
do   
	mkdir $i
	cp  conf.lmp graph.pb input.lammps job.json $i
        cd $i
	sed -i "s/variable        TEMP            equal 50.000000/variable        TEMP            equal $i.000000/g" input.lammps
	lbg job submit -i job.json -p ./ >log1
	cd ..
done
