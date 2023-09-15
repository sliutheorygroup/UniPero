mkdir collect
cd collect
mkdir energy force
cd ..
for i in BST-300K BST-450K BT-300K BT-450K BZT-BCT-300K BZT-BCT-450K NN-BT-300K NN-BT-450K PIN-PMN-PT-300K  PIN-PMN-PT-450K PMN-PT-300K PMN-PT-450K PT-300K PT-450K PZT-300K PZT-450K ST-300K ST-450K KNN-300K KNN-450K KNN-900K BST-900K BT-900K BZT-BCT-900K NN-BT-900K PIN-PMN-PT-900K PMN-PT-900K PT-900K ST-900K PZT-900K
do
	cp $i/dptest-$i.e.out ./collect/energy
	cp $i/dptest-$i.f.out ./collect/force
	cd collect/energy
	sed -i '1d' *.out
	mkdir $i
	mv dptest-$i.e.out $i
	cd $i
	mv dptest-$i.e.out 000.e.out
	cd ../../../
	cp ./script/sample-e.py collect/energy/$i
	cd collect/energy/$i
	python sample-e.py
	cp EN ../
	cd ../
	mv EN EN-$i
	cd ../../
done
	cp ./script/sort.sh collect/force
	cp ./script/sample-f.py collect/force
        cd collect/force
        sed -i '1d' *.out
        bash sort.sh
        ulimit -s unlimited
        python sample-f.py

