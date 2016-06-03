
#bic_0.5_1
#400
total: 186 detected: 1039 false alarm: 992 miss detection: 159
FAR: 0.842105263158
MDR: 0.854838709677

#bic_1_1
#600
total: 186 detected: 643 false alarm: 552 miss detection: 141
FAR: 0.747967479675
MDR: 0.758064516129

#bic_1.5_1
#750
total: 186 detected: 496 false alarm: 339 miss detection: 126
FAR: 0.645714285714
MDR: 0.677419354839

#bic_2_1
#870
total: 186 detected: 532 false alarm: 297 miss detection: 114
FAR: 0.614906832298
MDR: 0.612903225806

#bic_2.5_1
#1000
total: 186 detected: 601 false alarm: 343 miss detection: 119
FAR: 0.648393194707
MDR: 0.639784946237


#lium bic exp

bic_2.5
total: 186 detected: 426 false alarm: 330 miss detection: 90
FAR: 0.639534883721
MDR: 0.483870967742

bic_2.5_cluster
total: 186 detected: 166 false alarm: 73 miss detection: 93
FAR: 0.281853281853
MDR: 0.5





===========pacx
[37.49, 45.68, 57.19, 57.5, 106.97, 114.68]
[37.31, 45.14, 107.2, 112.93, 114.83]

bnews
===========

./run.sh BIC 50
total: 382 detected: 699 false alarm: 553 miss detection: 236 right detected: 146
FAR: 0.591443850267
MDR: 0.61780104712
RCL: 0.38219895288
RRL: 0.20886981402
./run.sh BIC 100
total: 382 detected: 667 false alarm: 471 miss detection: 186 right detected: 196
FAR: 0.552168815944
MDR: 0.486910994764
RCL: 0.513089005236
RRL: 0.293853073463
./run.sh BIC 150
total: 382 detected: 578 false alarm: 378 miss detection: 181 right detected: 200
FAR: 0.497368421053
MDR: 0.473821989529
RCL: 0.523560209424
RRL: 0.346020761246
./run.sh BIC 200
total: 382 detected: 531 false alarm: 337 miss detection: 188 right detected: 194
FAR: 0.468706536857
MDR: 0.492146596859
RCL: 0.507853403141
RRL: 0.365348399247
./run.sh BIC 250
total: 382 detected: 479 false alarm: 295 miss detection: 198 right detected: 184
FAR: 0.435745937962
MDR: 0.51832460733
RCL: 0.48167539267
RRL: 0.384133611691
./run.sh BIC 300
total: 382 detected: 454 false alarm: 269 miss detection: 197 right detected: 185
FAR: 0.413210445469
MDR: 0.515706806283
RCL: 0.484293193717
RRL: 0.407488986784

./run.sh GLR 50
total: 382 detected: 699 false alarm: 553 miss detection: 236 right detected: 146
FAR: 0.591443850267
MDR: 0.61780104712
RCL: 0.38219895288
RRL: 0.20886981402
./run.sh GLR 100
./run.sh GLR 150
./run.sh GLR 200
./run.sh GLR 250
./run.sh GLR 300


./run.sh KL2 50
total: 382 detected: 600 false alarm: 433 miss detection: 215 right detected: 167
FAR: 0.531288343558
MDR: 0.562827225131
RCL: 0.437172774869
RRL: 0.278333333333
./run.sh KL2 100
total: 382 detected: 604 false alarm: 424 miss detection: 202 right detected: 180
FAR: 0.526054590571
MDR: 0.528795811518
RCL: 0.471204188482
RRL: 0.298013245033
./run.sh KL2 150
total: 382 detected: 536 false alarm: 364 miss detection: 210 right detected: 172
FAR: 0.487935656836
MDR: 0.549738219895
RCL: 0.450261780105
RRL: 0.320895522388
./run.sh KL2 200
total: 382 detected: 494 false alarm: 334 miss detection: 222 right detected: 160
FAR: 0.466480446927
MDR: 0.581151832461
RCL: 0.418848167539
RRL: 0.323886639676
./run.sh KL2 250
total: 382 detected: 451 false alarm: 288 miss detection: 219 right detected: 163
FAR: 0.429850746269
MDR: 0.573298429319
RCL: 0.426701570681
RRL: 0.361419068736
./run.sh KL2 300
total: 382 detected: 430 false alarm: 275 miss detection: 227 right detected: 155
FAR: 0.418569254186
MDR: 0.594240837696
RCL: 0.405759162304
RRL: 0.360465116279



bnews evaluate with sad
===============
why do this? change evaluation judgement.
example:
[37.49, 45.68, 57.19, 57.5, 106.97, 114.68]
[37.92, 45.01, 107.02, 114.54]

silence: 45.25 - 46.21, 106.76 - 107.02


miss detection become of that is: 181-146 19.34%
false alarm become of that is: 379-342 9.76%

===============
BIC 50
total: 382 detected: 699 false alarm: 496 miss detection: 202 right detected: 203
FAR: 0.564920273349
MDR: 0.528795811518
RCL: 0.531413612565
RRL: 0.290414878398

BIC 100
total: 382 detected: 667 false alarm: 415 miss detection: 146 right detected: 252
FAR: 0.520702634881
MDR: 0.38219895288
RCL: 0.659685863874
RRL: 0.377811094453

BIC 150
total: 382 detected: 578 false alarm: 342 miss detection: 146 right detected: 236
FAR: 0.472375690608
MDR: 0.38219895288
RCL: 0.61780104712
RRL: 0.40830449827

BIC 200
total: 382 detected: 531 false alarm: 300 miss detection: 151 right detected: 231
FAR: 0.439882697947
MDR: 0.395287958115
RCL: 0.604712041885
RRL: 0.435028248588

BIC 250
total: 382 detected: 479 false alarm: 255 miss detection: 158 right detected: 224
FAR: 0.400313971743
MDR: 0.413612565445
RCL: 0.586387434555
RRL: 0.46764091858

BIC 300
total: 382 detected: 454 false alarm: 234 miss detection: 162 right detected: 220
FAR: 0.37987012987
MDR: 0.424083769634
RCL: 0.575916230366
RRL: 0.484581497797


swbd
===============
BIC 50
total: 8970 detected: 20009 false alarm: 15514 miss detection: 3805 right detected: 4495
FAR: 0.633638294396
MDR: 0.424191750279
RCL: 0.575808249721
RRL: 0.258133839772
BIC 100
total: 8970 detected: 9682 false alarm: 7210 miss detection: 6169 right detected: 2472
FAR: 0.445611866502
MDR: 0.68773690078
RCL: 0.31226309922
RRL: 0.28929973146
BIC 150
total: 8970 detected: 6391 false alarm: 4714 miss detection: 7057 right detected: 1677
FAR: 0.344489915229
MDR: 0.786733556299
RCL: 0.213266443701
RRL: 0.299327178845
BIC 200
total: 8970 detected: 4752 false alarm: 3496 miss detection: 7518 right detected: 1256
FAR: 0.280442804428
MDR: 0.838127090301
RCL: 0.161872909699
RRL: 0.305555555556