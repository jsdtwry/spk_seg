

def genref(ref_filename, seg_filename):
    fout = open(seg_filename, 'w')
    show = ref_filename.split('.')[0]
    ref = []
    ref_l = open(ref_filename).readlines()
    for index, i in enumerate(ref_l):
        time1 = float(i.split('     ')[-2])
        time2 = float(i.split('     ')[-1].split(' ')[-2])
        name = i.split('     ')[-1].split(' ')[-1]
        print show, time1, time2, 'speaker', name
        fout.write(show+' '+str(time1)+' '+str(time2)+' speaker '+name)


genref('paaz.ref', 'paaz.ref.seg')