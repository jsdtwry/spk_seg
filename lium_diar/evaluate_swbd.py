import os
import sys
from os.path import join
import os.path

lst_filename = 'lst/swbd.lst'

#ref_filename = '/home/wangry/work/data/bnews/bnews_cpd/paaa.cpd'
#det_filename = '/home/wangry/work/spk_seg/lium_diar/seg/paaa.s.seg'

ft = 0.3

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
        time = float(i.split('\t')[0])
        #time = float(i.split('\t')[-2])
        name = i.split('\t')[2]
        #print name
        #name = i.split('     ')[-1].split(' ')[-1]
        if index==0:
            #ref.append(time)
            continue
        elif name!=ref_l[index-1].split('\t')[2]:
            ref.append(time)
    return ref

def cal_singal(ref_filename, det_file0me):
    ref_l = open(ref_filename).readlines()
    det_l = open(det_filename).readlines()
    ref = []
    det = []

    ref = genref(ref_filename)

    for i in det_l:
        each = i[:-1].split(' ')
        if float(each[1])==0:
            continue
        det.append(float(each[1]))

    print ref
    det.sort()
    print det
    #false alarm
    false_alarm = 0
    right_alarm = 0
    for i in det:
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
    print right_alarm

    #miss detection
    miss_detection = 0
    right_detection = 0
    for i in ref:
        shot = 0
        for j in det:
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
    ref_filename = '/home/wangry/work/data/swbd/swbd_ref/'+i+'.ref'
    det_filename = '/home/wangry/work/spk_seg/lium_diar/swbd_BIC_100/'+i+'.s.seg'
    print "==========="+i
    cal =  cal_singal(ref_filename, det_filename)
    print cal
    total += cal[0]
    det_total +=  cal[1]
    false_alarm += cal[2]
    miss_detection += cal[3]
    right_alarm += cal[4]

print 'total:',total, 'detected:',det_total, 'false alarm:',false_alarm, 'miss detection:',miss_detection, 'right detected:', right_alarm

FAR = float(false_alarm)/(total+false_alarm)
MDR = float(miss_detection)/total
RCL = float(total - miss_detection)/total
RRL = float(total - miss_detection)/det_total

print 'FAR:',FAR
print 'MDR:',MDR
print 'RCL:',RCL
print 'RRL:',RRL