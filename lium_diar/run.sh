method=$1
winshift=$2

lst=lst/swbd.lst
mkdir swbd_${method}_${winshift}
for f in `cat ${lst}`
do
	echo $f
        ./run_bic.sh $f $method $winshift
done
