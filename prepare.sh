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

cp json/machine.json data/Task-II/$i/script
cp json/job.json data/Task-II/$i/script


for i in BT PT ST KN KNN PST PZT a-PIN_PMN_PT b-PIN_PMN_PT
do
     cp json/job.json data/phase-transition/$i
done

#unzip database.zip
unzip data/fitting/database.zip
mv data/fitting/database/* data/fitting
rm -rf database
