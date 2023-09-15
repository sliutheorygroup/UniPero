for i in CT BT ST PT NN ST1
do
	cd $i
	cp EN ../
	cd ../
	mv EN EN-$i
done

cat EN* >>3-element
