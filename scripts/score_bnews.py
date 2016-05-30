import os
import sys
from os.path import join
import os.path

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

def cal_rate(ref_filename, score_filename, sad_filename):
    fin = open(ref_filename)
    fin_score = open(score_filename)
    lines = fin.readlines()
    lines_score = fin_score.readlines()

    llr_threshold = 320
    bic_threshold = 1000
    ft = 0.3


    ref = []
    lastspk = ''
    for i in lines:
        ref.append(float(i))

    #sad
    '''
    fin_sad = open(sad_filename)
    lines_sad = fin_sad.readlines()
    for i in lines_sad:
        ref.append(float(i[:8]))
        ref.append(float(i[8:-1]))
    '''

    test = []
    for n, i in enumerate(lines_score):
        if n < len(lines_score)-1:
            each = i.split(' ')
            #if float(each[1]) > llr_threshold:
            #print n, each
            #if float(each[2]) < bic_threshold and float(each[2]) < float(lines_score[n-1].split(' ')[2]) and float(each[2]) < float(lines_score[n+1].split(' ')[2]):
            if float(each[1]) > bic_threshold:
                test.append(float(each[0]))

    print '----'
    print len(ref)
    print len(test)

    #false alarm
    false_alarm = 0
    right_alarm = 0
    for i in test:
        shot = 0
        for j in ref:
            if abs(i-j)<=ft:
                #print 'right alarm',i, j
                right_alarm += 1
                shot = 1
                break
        if shot==0:
            false_alarm += 1
            #print 'false alarm',i, j

    #print false_alarm
    #print right_alarm

    #miss detection
    miss_detection = 0
    right_detection = 0
    for i in ref:
        shot = 0
        for j in test:
            if abs(i-j)<=ft:
                right_detection += 1
                shot = 1
                break
        if shot==0:
            miss_detection += 1

    #print miss_detection
    #print right_detection
    return len(ref),len(test), false_alarm, miss_detection


'''
ref_filename = 'ref\\paae.cpd'
score_filename = 'score\\paae.score'
sad_filename = 'bnews_sad\\paae.sad'

total, false_alarm, miss_detection = cal_rate(ref_filename, score_filename, sad_filename)


FAR = float(false_alarm)/(total+false_alarm)
MDR = float(miss_detection)/total

print total, false_alarm, miss_detection
print FAR
print MDR
'''


total = 0
test_total = 0
false_alarm = 0
miss_detection = 0
for i in listFiles('/home/wangry/work/data/bnews/bnews_score_1_1/', 'score'):
    #print '---'
    filename = i[1].split('.')[0]
    ref_filename = '/home/wangry/work/data/bnews/bnews_cpd/'+filename+'.cpd'
    score_filename = '/home/wangry/work/data/bnews/bnews_score_2.5_1/'+filename+'.score'
    sad_filename = '/home/wangry/work/data/bnews/bnews_sad/'+filename+'.sad'
    cal =  cal_rate(ref_filename, score_filename, sad_filename)
    total += cal[0]
    test_total +=  cal[1]
    false_alarm += cal[2]
    miss_detection += cal[3]

print 'total:',total, 'detected:',test_total, 'false alarm:',false_alarm, 'miss detection:',miss_detection

FAR = float(false_alarm)/(total+false_alarm)
MDR = float(miss_detection)/total

print 'FAR:',FAR
print 'MDR:',MDR
