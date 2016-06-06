liumpath=./LIUM_SpkDiarization-8.4.1.jar
liumcmd='java -cp '${liumpath}

show=$1
method=$2
winlen=$3
winshift=$4
l=$5
h=$6

basedir=/home/wangry/work/data
datadir=./bnews_${method}_${winlen}_${winshift}_${l}_${h}

fDesc="audio2sphinx,1:1:0:0:0:0,13,0:0:0"

fwav=$basedir/bnews/bnews_wav/$show.wav

#seg init
${liumcmd} fr.lium.spkDiarization.programs.MSegInit --fInputMask=$fwav --fInputDesc=$fDesc --sOutputMask=./$datadir/$show.i.seg  $show

#bic/kl2 segmentation
${liumcmd} fr.lium.spkDiarization.programs.MSeg --kind=FULL --sMethod=$method --sModelWindowSize=$winlen --sMinimumWindowSize=$winshift --fInputMask=$fwav --fInputDesc=$fDesc --sInputMask=./$datadir/$show.i.seg --sOutputMask=./$datadir/$show.s.seg --sOutputFormat=eger.hyp $show

# linear clustering
${liumcmd} fr.lium.spkDiarization.programs.MClust --fInputMask=$fwav --fInputDesc=$fDesc --sInputMask=./$datadir/$show.s.seg.seg --sOutputMask=./$datadir/$show.l.seg --cMethod=l --cThr=$l --sOutputFormat=eger.hyp $show

# hierarchical clustering
${liumcmd} fr.lium.spkDiarization.programs.MClust --fInputMask=$fwav --fInputDesc=$fDesc --sInputMask=./$datadir/$show.l.seg.seg --sOutputMask=./$datadir/$show.h.$h.seg --cMethod=h --cThr=$h --sOutputFormat=eger.hyp $show

#Initialize GMM
${liumcmd} fr.lium.spkDiarization.programs.MTrainInit --nbComp=8 --kind=DIAG --fInputMask=$fwav --fInputDesc=$fDesc --sInputMask=./$datadir/$show.h.$h.seg.seg --tOutputMask=./$datadir/$show.init.$h.gmms $show

# EM computation
${liumcmd} fr.lium.spkDiarization.programs.MTrainEM --nbComp=8 --kind=DIAG --fInputMask=$fwav --fInputDesc=$fDesc --sInputMask=./$datadir/$show.h.$h.seg.seg --tOutputMask=./$datadir/$show.$h.gmms  --tInputMask=./$datadir/$show.init.$h.gmms  $show

#Viterbi decoding
${liumcmd} fr.lium.spkDiarization.programs.MDecode --fInputMask=$fwav --fInputDesc=$fDesc --sInputMask=./$datadir/$show.h.$h.seg.seg --sOutputMask=./$datadir/$show.d.$h.seg --sOutputFormat=eger.hyp --dPenality=250 --tInputMask=$datadir/$show.$h.gmms $show

#Adjust segment boundaries
adjseg=./$datadir/$show.adj.$h.seg
${liumcmd} fr.lium.spkDiarization.tools.SAdjSeg --fInputMask=$fwav --fInputDesc=$fDesc --sInputMask=./$datadir/$show.d.$h.seg.seg --sOutputMask=$adjseg --sOutputFormat=eger.hyp $show


