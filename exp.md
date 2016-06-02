
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