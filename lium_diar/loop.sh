lst=lst/bnews_b.lst
for f in `cat ${lst}`
do
	echo $f
        ./run_bic.sh $f
done
