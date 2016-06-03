import os
import sys
from os.path import join
import os.path

lst_filename = 'lst/bnews.lst'

#ref_filename = '/home/wangry/work/data/bnews/bnews_cpd/paaa.cpd'
#det_filename = '/home/wangry/work/spk_seg/lium_diar/seg/paaa.s.seg'

ft = 0.3
st = 0.3

lst_l = open(lst_filename).readlines()

lst = []

for i in lst_l:
    lst.append(i[:-1])

#print ref
#print det
def genref(ref_filename):
    ref = []
    ref_l = open(ref_filename).readlines()
    for index, i in enumerate(ref_l):
        time = float(i.split('     ')[-2])
        name = i.split('     ')[-1].split(' ')[-1]
        if index==0:
            #ref.append(time)
            continue
        elif name!=ref_l[index-1].split('     ')[-1].split(' ')[-1]:
            ref.append(time)
    return ref

def gensad(sad_filename):
    sad = []
    sad_l = open(sad_filename).readlines()
    for i in sad_l:
        sad.append([float(i[:8]), float(i[8:-1])])
    return  sad


def is_insilence(point, sad):
    for index, i in enumerate(sad):
        if index == len(sad)-1:
                return 0
        if point > i[0] and point < i[1]:
            return 0
        elif point >= i[1] and point <= sad[index+1][0]:
            return i[1], sad[index+1][0]
    return 0


def cal_singal(ref_filename, det_filename, sad_filename):
    ref_l = open(ref_filename).readlines()
    det_l = open(det_filename).readlines()
    det = []

    ref = genref(ref_filename)
    sad = gensad(sad_filename)

    for i in det_l:
        each = i[:-1].split(' ')
        if float(each[1])==0:
            continue
        det.append(float(each[1]))

    #print sad
    print ref
    det.sort()
    print det
    #false alarm
    false_alarm = 0
    right_alarm = 0
    for i in det:
        shot = 0
        for j in ref:
            insilence = is_insilence(j, sad)
            if insilence!=0:    # is in silence
                if i > insilence[0]-st and i < insilence[1]+st:
                    print 'xxxxxxxxxxxxxxxx',insilence
                    right_alarm += 1
                    shot = 1
                    break
            else:
                if abs(i-j)<=ft:
                    #print 'right alarm',i, j
                    right_alarm += 1
                    shot = 1
                    break
        if shot==0:
            false_alarm += 1
            #print 'false alarm',i, j

    #print false_alarm
    print right_alarm

    #miss detection
    miss_detection = 0
    right_detection = 0
    for i in ref:
        shot = 0
        for j in det:
            insilence = is_insilence(i, sad)
            if insilence!=0:    # is in silence
                if j > insilence[0]-st and j < insilence[1]+st:
                    right_detection += 1
                    shot = 1
                    break
            else:
                if abs(i-j)<=ft:
                    right_detection += 1
                    shot = 1
                    break
        if shot==0:
            miss_detection += 1

    #print miss_detection
    print right_detection
    return len(ref),len(det), false_alarm, miss_detection, right_alarm

total = 0
det_total = 0
false_alarm = 0
miss_detection = 0
right_alarm = 0

#print cal_singal(ref_filename, det_filename)
for i in lst:
    sad_filename = '/home/wangry/work/data/bnews/bnews_sad/'+i+'.sad'
    ref_filename = '/home/wangry/work/data/bnews/bnews_ref/'+i+'.ref'
    det_filename = '/home/wangry/work/data/res/bnews_BIC_300/'+i+'.l.seg'
    print "==========="+i
    cal =  cal_singal(ref_filename, det_filename, sad_filename)
    print cal
    total += cal[0]
    det_total +=  cal[1]
    false_alarm += cal[2]
    miss_detection += cal[3]
    right_alarm += cal[4]

print 'total:',total, 'detected:',det_total, 'false alarm:',false_alarm, 'miss detection:',miss_detection, 'right detected:', right_alarm

FAR = float(false_alarm)/(total+false_alarm)
MDR = float(miss_detection)/total
RCL = float(right_alarm)/total
RRL = float(right_alarm)/det_total

print 'FAR:',FAR
print 'MDR:',MDR
print 'RCL:',RCL
print 'RRL:',RRL