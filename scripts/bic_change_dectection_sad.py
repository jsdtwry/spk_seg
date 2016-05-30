import numpy as np
from scipy.io import wavfile
from matplotlib import pyplot
import features
import math
from sklearn import mixture
#import sidekit

bin_width = 2.5
bin_shift = 0.1

win_shift = 0.01

lamda = 1

def inlist(a, ref):
    for i in ref:
        if a > i[0] and a < i[1]:
            return True
    return False

def getsad_ref(sadfilename):
    ref = []
    fin_sad = open(sadfilename)
    lines_sad = fin_sad.readlines()
    for i in lines_sad:
        ref.append([float(i[:8]), float(i[8:-1])])
    return ref

def mfcc_cut_vad(mfcc_feat, ref):
    an_win_mfcc = []
    i = 0
    an_win_content = 0
    while i < len(mfcc_feat):
        if an_win_content == bin_width/win_shift:
            an_win_content = 0
        if inlist((i+1)*win_shift, ref):
            an_win_mfcc.append([(i+1)*win_shift, mfcc_feat[i]])
            #print mfcc_time[i], mfcc_feat[i]
            an_win_content += 1
        i += 1
    return an_win_mfcc

'''get one window mfcc and its time'''
def mfcc_cut_vad_an_win(mfcc_feat, ref):
    an_bin_mfcc = []
    an_win_mfcc = []
    i = 0
    bin_shift_num = bin_shift/win_shift
    start_win = 0
    an_win_content = 0

    while i+bin_shift_num < len(mfcc_feat):
        if an_win_content == bin_width/win_shift-1:
            an_win_content = 0
            an_bin_mfcc.append([(an_win_mfcc[0][0]+an_win_mfcc[int(bin_width/win_shift)-2][0])/2, an_win_mfcc])
            an_win_mfcc = []
            start_win += bin_shift_num
            i = start_win
        if inlist((i+1)*win_shift, ref):
            an_win_mfcc.append([(i+1)*win_shift, mfcc_feat[i]])
            an_win_content += 1
        i += 1
    return an_bin_mfcc

def bic(an_win_mfcc):
    likescores = []
    time = []
    bic = []
    for i, each in enumerate(an_win_mfcc):
        win_w = [j[1] for j in each[1]]
        mid = len(win_w)/2 + 1
        win_l = win_w[:mid]
        win_r = win_w[mid-1:]
        #print len(win_l), len(win_r), len(win_w)

        gl = mixture.GMM(n_components=1, covariance_type='full')
        gl.fit(win_l)

        gr = mixture.GMM(n_components=1, covariance_type='full')
        gr.fit(win_r)

        gw = mixture.GMM(n_components=1, covariance_type='full')
        gw.fit(win_w)

        d = len(gw.means_[0])
        #print d
        r = len(win_w)*math.log(np.linalg.det(gw.covars_)) - len(win_l)*math.log(np.linalg.det(gl.covars_)) - len(win_r)*math.log(np.linalg.det(gr.covars_))
        bic_value = r - (d+d*(d+1)/2.0)/2.0*math.log(float(len(win_w)))*lamda
        time.append(each[0])
        bic.append(bic_value)
    return time, bic


def plot_bic(wavfilename, sadfilename):
    sample_rate, wav = wavfile.read(wavfilename)
    mfcc_feat = features.mfcc(wav, sample_rate)
    ref = getsad_ref(sadfilename)
    an_win_mfcc = mfcc_cut_vad_an_win(mfcc_feat, ref)
    [time, bic_value] = bic(an_win_mfcc)
    pyplot.plot(time, bic_value)
    pyplot.scatter(time, bic_value)
    pyplot.show()


def cal_bic(wavfilename, sadfilename):
    sample_rate, wav = wavfile.read(wavfilename)
    mfcc_feat = features.mfcc(wav, sample_rate)
    ref = getsad_ref(sadfilename)
    an_win_mfcc = mfcc_cut_vad_an_win(mfcc_feat, ref)
    [time, bic_value] = bic(an_win_mfcc)
    return time, bic_value



