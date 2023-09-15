for i in P27T9Z9N6M3 P27T10N10M3I4 B9P3T9N2M10 B6P6T6N4M2  B3P9T3N6M3
do
	cd $i
	cp EN ../
	cd ../
	mv EN EN-$i
done

cat EN* >>6-element
