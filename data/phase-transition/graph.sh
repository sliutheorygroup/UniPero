for i in 
do
   cd $i
   mv latt_sort.txt $i.dat
   cp $i.dat ../graph
   cd ..
done
cd graph
