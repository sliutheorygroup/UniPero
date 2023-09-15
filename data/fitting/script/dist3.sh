for i in CT BT ST PT NN ST1
do
	mkdir $i
done
	mv 000*  ST
	mv 069*  ST1
	mv 001* PT
	mv 009* CT
	mv 010*  CT
	mv 047* NN
	mv 066* NN
	mv 073* CT
	mv 094*  PT
	mv 114*  BT

	for i in CT BT ST PT NN ST1
do
	cp sample-e.py $i
        cd $i
        python sample-e.py
        cd ..
done
