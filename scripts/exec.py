from bic_change_dectection_sad import *
import os
import sys
from os.path import join
import os.path
'''
def listFiles(dirpath,suffix): 
    listlines=[]
    files = os.listdir(dirpath)
    for eachfile in files:
        curfile = dirpath + os.sep + eachfile
        if os.path.isdir(curfile):
            for mid in listFiles(curfile,suffix):
                listlines.append(mid)
        elif eachfile.endswith(suffix):
            listlines.append([dirpath,eachfile])                       
    return listlines

#plot_bic('paas.wav','paas.sad')
basedir = 'score'
list_wav = listFiles('D:\\workspaces\\cslt\\task\\160413_speaker_darization\\change_point_detection\\Sox\\bnews_wav', '.wav')
list_sad = listFiles('D:\\workspaces\\cslt\\task\\160413_speaker_darization\\change_point_detection\\Sox\\bnews_sad', '.sad')

list_wav_f = []
list_sad_f = []
for i in list_wav:
    list_wav_f.append(i[0]+'\\'+i[1])

for i in list_sad:
    list_sad_f.append(i[0]+'\\'+i[1])

for i in range(len(list_wav)):
    time, bic_value = cal_bic(list_wav_f[i],list_sad_f[i])
    print basedir+'\\'+list_wav_f[i].split('\\')[-1].split('.')[0]+'.score'
    fout = file(basedir+'\\'+list_wav_f[i].split('\\')[-1].split('.')[0]+'.score', 'w')
    for j in range(len(time)):
        fout.write(str(time[j])+' '+str(bic_value[j])+'\n')
'''
#plot_bic('paaa.wav','paaa.sad')

#fout = open('bnews.lst','w')


base_wav = '/home/wangry/work/data/bnews/bnews_wav/'
base_sad = '/home/wangry/work/data/bnews/bnews_sad/'
base_score = '/home/wangry/work/data/bnews/bnews_score_2.5_1/'

temp = [chr(i) for i in range(ord("a"),ord("z")+1)]
for i in temp:
    wav = base_wav + 'paa'+i+'.wav'
    sad = base_sad + 'paa'+i+'.sad'
    score = base_score + 'paa'+i+'.score'
    print wav, sad
    time, bic_value = cal_bic(wav, sad)
    fout = open(score, 'w')
    for j in range(len(time)):
        fout.write(str(time[j])+' '+str(bic_value[j])+'\n')
