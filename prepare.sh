%%bash
#copy dpmodel
cd model
mv *.pb graph.pb
cd ..
cp model/graph.pb data/Task-I/script
cp model/graph.pb data/fitting/script


cp model/graph.pb data/Task-II/script
cp model/graph.pb data/Task-II/dptest


for i in BT PT ST KN KNN PST PZT a-PIN_PMN_PT b-PIN_PMN_PT

do
     cp model/graph.pb data/phase-transition/$i
done

#copy json files

cp json/machine.json data/Task-II/script
cp json/job.json data/Task-II/script


for i in BT PT ST KN KNN PST PZT a-PIN_PMN_PT b-PIN_PMN_PT
do
     cp json/job.json data/phase-transition/$i
done

#unzip database.zip
CURRENT=`pwd`
cd data/fitting
unzip database.zip
mv database/* .
cd "$CURRENT"

