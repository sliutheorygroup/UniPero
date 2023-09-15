mkdir 3-element 4-element 5-element 6-element 
cd script
cp -r dist3.sh cat3.sh sample-e.py ../3-element
cp -r dist4.sh cat4.sh sample-e.py ../4-element
cp -r dist5.sh cat5.sh sample-e.py ../5-element
cp -r dist6.sh cat6.sh sample-e.py ../6-element
cd ..

for i in 000 001 009 010
do
	cp -r $i* 3-element
done

for i in 002 003 004
do
	cp -r $i* 4-element
done

for i in 005 006 007 008
do
	cp -r $i* 5-element
done

for i in {011..038}
do
	cp -r $i* 4-element
done

for i in {039..044}
do
	cp -r $i* 5-element
done

for i in {045..046}
do
	cp -r $i* 6-element
done

for i in 047
do
	cp -r $i* 3-element
done

for i in {048..053}
do
	cp -r $i* 5-element
done

for i in {054..065}
do
	cp -r $i* 6-element
done

for i in 066 073 094 114 069
do  
	cp -r $i* 3-element
done

for i in 067 068 070 071 072 108
do
	cp -r $i* 4-element
done

for i in {074..075}
do
	cp -r $i* 4-element
done

for i in {077..082}
do
	cp -r $i* 5-element
done

for i in 083 100 111 115 076
do 
	cp -r $i* 6-element 
done

for i in {084..093}
do
	cp -r $i* 4-element
done

for i in {095..096}
do
	cp -r $i* 5-element
done

for i in {097..099}
do
	cp -r $i* 4-element
done

for i in {101..102}
do
	cp -r $i* 5-element
done

for i in {103..105}
do
	cp -r $i* 4-element
done

for i in {109..110}
do
	cp -r $i* 4-element
done

for i in {106..107}
do
        cp -r $i* 5-element
done

for i in {112..113}
do
        cp -r $i* 5-element
done


folders=("3-element" "4-element" "5-element" "6-element")


current_dir=$(pwd)


for folder in "${folders[@]}"; do
  
    if [ -d "$current_dir/$folder" ]; then
        
        cd "$current_dir/$folder"

       
        dist_script=$(ls dist*.sh)
        if [ -n "$dist_script" ]; then
            bash "$dist_script"
        fi

      
        cat_script=$(ls cat*.sh)
        if [ -n "$cat_script" ]; then
            bash "$cat_script"
        fi

        
        cd "$current_dir"
    fi
done

mkdir -p Force

cp -r *.out script/sample-f.py Force

cd Force

python sample-f.py 
