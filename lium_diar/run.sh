method=$1
winlen=$2
winshift=$3

lst=lst/bnews.lst
mkdir bnews_${method}_${winlen}_${winshift}
for f in `cat ${lst}`
do
	echo $f
        ./run_bic.sh $f $method $winlen $winshift
done
