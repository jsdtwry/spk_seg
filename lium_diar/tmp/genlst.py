fout = open('lst/meet.lst', 'w')
flist = open('/home/wangry/work/data/meet/meet_sph/seg_mt.lst').readlines()
for i in flist:
	fout.write(i.split('.')[-2]+'\n')

