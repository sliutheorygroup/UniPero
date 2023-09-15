
CURRENT=`pwd`

mkdir collect
cd collect
mkdir energy force
cd "$CURRENT"


for j in 300K 450K 900K
do
for i in BST BT BZT-BCT NN-BT PMN-PT PZT KNN PIN-PMN-PT PT ST
do
#dptest

        cp ./dptest/abscf2dp.py $i-$j/script 
        cp ./dptest/graph.pb $i-$j/script
        cd $i-$j/script
        python abscf2dp.py
        dp test -m graph.pb -s deepmd/* -n 200 -d dptest-$i-$j
        cd "$CURRENT"

#energy

	cp ./$i-$j/script/dptest-$i-$j.e.out ./collect/energy
	cp ./$i-$j/script/dptest-$i-$j.f.out ./collect/force
	cd collect/energy
	sed -i '1d' *.out
        mkdir $i-$j
	mv dptest-$i-$j.e.out $i-$j
	cd $i-$j
	mv dptest-$i-$j.e.out 000.e.out
	cd ../../../
	cp ./dptest/sample-e.py collect/energy/$i-$j
	cd collect/energy/$i-$j
	python sample-e.py
	cp EN ../
	cd ../
	mv EN EN-$i-$j
	cd "$CURRENT"

#force

	cp ./dptest/sort.sh collect/force
	cp ./dptest/sample-f.py collect/force
        cd collect/force
        sed -i '1d' *.out
    
        count=0

        for file in *.f.out; do
            new_name=$(printf "%03d.f.out" "$count")
            mv "$file" "$new_name"
            ((count++))
        done
        ulimit -s unlimited
        python sample-f.py
        mv Force-all Force-all-$i-$j
        cd "$CURRENT"
done
done
