
basedir=/home/wangry/work/data

fDesc="audio2sphinx,1:1:0:0:0:0,13,0:0:0"

fwav=$basedir/bnews/bnews_wav/paaz.wav

#java -cp ../LIUM_SpkDiarization-8.4.1.jar fr.lium.spkDiarization.programs.MSegInit --fInputMask=$fwav --fInputDesc=$fDesc --sOutputMask=paaz.i.seg  paaz



java -Xmx2024m -jar ../LIUM_SpkDiarization-8.4.1.jar --thresholds=1.5:2.5,2.5:3.5,250.0:300,0:3.0 --fInputMask=$fwav --sInputMask="" --sInput2Format=eger.hyp --sInput2Mask="./paaz.ref.seg" --doCEClustering  paaz

#java -Xmx2024m -jar ./lib/LIUM_SpkDiarization.jar --help --thresholds=1.5:2.5,2.5:3.5,250.0:300,0:3.0 --loadInputSegmentation --fInputMask="./sph/%s.sph" --sInputMask="./sph/%s.uem.seg" --sInput2Mask="./ref/%s.seg"  --doTuning=2 --doCEClustering  $show &> out.tx
