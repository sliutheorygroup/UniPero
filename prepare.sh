%%bash
#copy dpmodel
cd model
mv *.pb graph.pb
cd ..
cp model/graph.pb data/TaskI/script
cp model/graph.pb data/fitting/script

for i in 300K 450K 900K
do 
     cp model/graph.pb data/TaskII/$i/script
     cp model/graph.pb data/TaskII/$i/dptest
done

for i in BT PT ST KN KNN PST PZT a-PIN_PMN_PT b-PIN_PMN_PT

do
     cp model/graph.pb data/phase-transition/$i
done

#copy json files
for i in 300K 450K 900K
do 
     cp json/machine.json data/TaskII/$i/script
     cp json/job.json data/TaskII/$i/script
done

for i in BT PT ST KN KNN PST PZT a-PIN_PMN_PT b-PIN_PMN_PT
do
     cp json/job.json data/phase-transition/$i
done

#unzip database.zip
unzip data/fitting/database.zip
mv database.zip/* ..
rm -rf database
