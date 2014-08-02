for file in *.nex; 
do 
sed -i 's/FORMAT / FORMAT DATATYPE=standard/g' $file; 
sed -i 's/SYMBOLS=//g' $file;
sed -i 's/SYMBOLS=//g' $file;
done

