
for j in 300K 450K 900K
do 
for i in BT BZT-BCT NN-BT PMN-PT PZT KNN PIN-PMN-PT PT ST BST
do
	mkdir  $i-$j
	cp ./conf/$i/conf.lmp $i-$j
	cp script/graph.pb script/input.lammps script/job.json $i-$j
	cd $i-$j
    sed -i "s/\(variable TEMP equal \)[0-9.]\+/\\1$j/g" input.lammps
	lbg job submit -i job.json -p ./ >jobid
	cd ..
done
done
