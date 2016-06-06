method=$1
winlen=$2
winshift=$3
l=$4
h=$5
lst=lst/bnews.lst
mkdir bnews_${method}_${winlen}_${winshift}_${l}_${h}
for f in `cat ${lst}`
do
	echo $f
        ./run_bic.sh $f $method $winlen $winshift ${l} ${h}
done
