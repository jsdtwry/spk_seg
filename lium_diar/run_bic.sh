liumpath=./LIUM_SpkDiarization-8.4.1.jar
liumcmd='java -cp '${liumpath}

basedir=/home/wangry/work/data
datadir=./seg_bic_b
show=$1

fDesc="audio2sphinx,1:1:0:0:0:0,13,0:0:0"

fwav=$basedir/bnews/bnews_wav/$show.wav

#seg init
${liumcmd} fr.lium.spkDiarization.programs.MSegInit --fInputMask=$fwav --fInputDesc=$fDesc --sOutputMask=./$datadir/$show.i.seg  $show

#bic/kl2 segmentation
${liumcmd} fr.lium.spkDiarization.programs.MSeg --kind=FULL --sMethod=BIC --fInputMask=$fwav --fInputDesc=$fDesc --sInputMask=./$datadir/$show.i.seg --sOutputMask=./$datadir/$show.s.seg --sOutputFormat=eger.hyp $show

# linear clustering
${liumcmd} fr.lium.spkDiarization.programs.MClust --fInputMask=$fwav --fInputDesc=$fDesc --sInputMask=./$datadir/$show.s.seg.seg --sOutputMask=./$datadir/$show.l.seg --cMethod=l --cThr=2 --sOutputFormat=eger.hyp $show

