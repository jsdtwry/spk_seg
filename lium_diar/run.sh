method=$1
winshift=$2

lst=lst/bnews.lst
mkdir bnews_$method_$winshift
for f in `cat ${lst}`
do
	echo $f
        ./run_bic.sh $f $method $winshift
done
