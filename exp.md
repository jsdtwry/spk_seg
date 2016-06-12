
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


bnews last exp
===============
./run.sh BIC 25 10 1 1
./run.sh BIC 50 10 1 1
./run.sh BIC 75 10 1 1
./run.sh BIC 100 10 1 1
./run.sh BIC 125 10 1 1
./run.sh BIC 150 10 1 1
./run.sh BIC 200 10 1 1
./run.sh BIC 250 10 1 1
./run.sh BIC 300 10 1 1

./run.sh BIC 25 10 1 2
./run.sh BIC 50 10 1 2
./run.sh BIC 75 10 1 2
./run.sh BIC 100 10 1 2
./run.sh BIC 125 10 1 2
./run.sh BIC 150 10 1 2
./run.sh BIC 200 10 1 2
./run.sh BIC 250 10 1 2
./run.sh BIC 300 10 1 2

./run.sh BIC 25 10 2 2
./run.sh BIC 50 10 2 2
./run.sh BIC 75 10 2 2
./run.sh BIC 100 10 2 2
./run.sh BIC 125 10 2 2
./run.sh BIC 150 10 2 2
./run.sh BIC 200 10 2 2
./run.sh BIC 250 10 2 2
./run.sh BIC 300 10 2 2

./run.sh BIC 25 10 1 3
./run.sh BIC 50 10 1 3
./run.sh BIC 75 10 1 3
./run.sh BIC 100 10 1 3
./run.sh BIC 125 10 1 3
./run.sh BIC 150 10 1 3
./run.sh BIC 200 10 1 3
./run.sh BIC 250 10 1 3
./run.sh BIC 300 10 1 3


./run.sh BIC 25 20 1 1
./run.sh BIC 50 20 1 1
./run.sh BIC 75 20 1 1
./run.sh BIC 100 20 1 1
./run.sh BIC 125 20 1 1
./run.sh BIC 150 20 1 1
./run.sh BIC 200 20 1 1
./run.sh BIC 250 20 1 1
./run.sh BIC 300 20 1 1

./run.sh BIC 25 20 1 2
./run.sh BIC 50 20 1 2
./run.sh BIC 75 20 1 2
./run.sh BIC 100 20 1 2
./run.sh BIC 125 20 1 2
./run.sh BIC 150 20 1 2
./run.sh BIC 200 20 1 2
./run.sh BIC 250 20 1 2
./run.sh BIC 300 20 1 2

./run.sh BIC 25 20 2 2
./run.sh BIC 50 20 2 2
./run.sh BIC 75 20 2 2
./run.sh BIC 100 20 2 2
./run.sh BIC 125 20 2 2
./run.sh BIC 150 20 2 2
./run.sh BIC 200 20 2 2
./run.sh BIC 250 20 2 2
./run.sh BIC 300 20 2 2

./run.sh BIC 25 20 1 3
./run.sh BIC 50 20 1 3
./run.sh BIC 75 20 1 3
./run.sh BIC 100 20 1 3
./run.sh BIC 125 20 1 3
./run.sh BIC 150 20 1 3
./run.sh BIC 200 20 1 3
./run.sh BIC 250 20 1 3
./run.sh BIC 300 20 1 3


//////////////l=1, h=1///////////////
========winlen:  25 ==========
total: 382 detected: 31754 false alarm: 31014 miss detection: 8 right detected: 740
FAR: 0.987832844948
MDR: 0.020942408377
RCL: 1.93717277487
RRL: 0.0233041506582
total: 382 detected: 27052 false alarm: 26465 miss detection: 39 right detected: 587
FAR: 0.98577122211
MDR: 0.102094240838
RCL: 1.53664921466
RRL: 0.02169895017
total: 382 detected: 27052 false alarm: 26465 miss detection: 39 right detected: 587
FAR: 0.98577122211
MDR: 0.102094240838
RCL: 1.53664921466
RRL: 0.02169895017
total: 382 detected: 4254 false alarm: 4033 miss detection: 189 right detected: 221
FAR: 0.913476783692
MDR: 0.494764397906
RCL: 0.578534031414
RRL: 0.0519511048425
total: 382 detected: 4163 false alarm: 3882 miss detection: 166 right detected: 281
FAR: 0.910412757974
MDR: 0.434554973822
RCL: 0.735602094241
RRL: 0.0674993994715
========winlen:  50 ==========
total: 382 detected: 28827 false alarm: 28137 miss detection: 22 right detected: 690
FAR: 0.986605420947
MDR: 0.0575916230366
RCL: 1.80628272251
RRL: 0.0239358934332
total: 382 detected: 22947 false alarm: 22436 miss detection: 49 right detected: 511
FAR: 0.983258830748
MDR: 0.128272251309
RCL: 1.33769633508
RRL: 0.022268706149
total: 382 detected: 22947 false alarm: 22436 miss detection: 49 right detected: 511
FAR: 0.983258830748
MDR: 0.128272251309
RCL: 1.33769633508
RRL: 0.022268706149
total: 382 detected: 5499 false alarm: 5235 miss detection: 144 right detected: 264
FAR: 0.931992166637
MDR: 0.376963350785
RCL: 0.69109947644
RRL: 0.0480087288598
total: 382 detected: 5360 false alarm: 5030 miss detection: 113 right detected: 330
FAR: 0.929416112343
MDR: 0.295811518325
RCL: 0.86387434555
RRL: 0.0615671641791
========winlen:  75 ==========
total: 382 detected: 27006 false alarm: 26317 miss detection: 23 right detected: 689
FAR: 0.985692348028
MDR: 0.0602094240838
RCL: 1.80366492147
RRL: 0.0255128489965
total: 382 detected: 20935 false alarm: 20423 miss detection: 55 right detected: 512
FAR: 0.98163902908
MDR: 0.143979057592
RCL: 1.34031413613
RRL: 0.0244566515405
total: 382 detected: 20935 false alarm: 20423 miss detection: 55 right detected: 512
FAR: 0.98163902908
MDR: 0.143979057592
RCL: 1.34031413613
RRL: 0.0244566515405
total: 382 detected: 5577 false alarm: 5307 miss detection: 144 right detected: 270
FAR: 0.932852873967
MDR: 0.376963350785
RCL: 0.706806282723
RRL: 0.0484131253362
total: 382 detected: 5464 false alarm: 5135 miss detection: 107 right detected: 329
FAR: 0.930759470727
MDR: 0.280104712042
RCL: 0.861256544503
RRL: 0.0602122986823
========winlen:  100 ==========
total: 382 detected: 25706 false alarm: 25045 miss detection: 15 right detected: 661
FAR: 0.984976599678
MDR: 0.0392670157068
RCL: 1.73036649215
RRL: 0.0257138411266
total: 382 detected: 19774 false alarm: 19279 miss detection: 56 right detected: 495
FAR: 0.980570672906
MDR: 0.146596858639
RCL: 1.29581151832
RRL: 0.0250328714474
total: 382 detected: 19774 false alarm: 19279 miss detection: 56 right detected: 495
FAR: 0.980570672906
MDR: 0.146596858639
RCL: 1.29581151832
RRL: 0.0250328714474
total: 382 detected: 5734 false alarm: 5446 miss detection: 133 right detected: 288
FAR: 0.93445435827
MDR: 0.348167539267
RCL: 0.753926701571
RRL: 0.0502267178235
total: 382 detected: 5616 false alarm: 5263 miss detection: 99 right detected: 353
FAR: 0.932329495128
MDR: 0.259162303665
RCL: 0.924083769634
RRL: 0.0628561253561
========winlen:  125 ==========
total: 382 detected: 24829 false alarm: 24186 miss detection: 16 right detected: 643
FAR: 0.984451318789
MDR: 0.0418848167539
RCL: 1.6832460733
RRL: 0.0258971364131
total: 382 detected: 19015 false alarm: 18549 miss detection: 51 right detected: 466
FAR: 0.97982145687
MDR: 0.133507853403
RCL: 1.21989528796
RRL: 0.024506968183
total: 382 detected: 19015 false alarm: 18549 miss detection: 51 right detected: 466
FAR: 0.97982145687
MDR: 0.133507853403
RCL: 1.21989528796
RRL: 0.024506968183
total: 382 detected: 5542 false alarm: 5254 miss detection: 120 right detected: 288
FAR: 0.932221433641
MDR: 0.314136125654
RCL: 0.753926701571
RRL: 0.0519667989895
total: 382 detected: 5434 false alarm: 5086 miss detection: 97 right detected: 348
FAR: 0.93013899049
MDR: 0.253926701571
RCL: 0.910994764398
RRL: 0.064041221936
========winlen:  150 ==========
total: 382 detected: 23988 false alarm: 23358 miss detection: 19 right detected: 630
FAR: 0.983909014322
MDR: 0.0497382198953
RCL: 1.64921465969
RRL: 0.0262631315658
total: 382 detected: 18217 false alarm: 17742 miss detection: 48 right detected: 475
FAR: 0.978922975061
MDR: 0.125654450262
RCL: 1.24345549738
RRL: 0.026074545754
total: 382 detected: 18217 false alarm: 17742 miss detection: 48 right detected: 475
FAR: 0.978922975061
MDR: 0.125654450262
RCL: 1.24345549738
RRL: 0.026074545754
total: 382 detected: 5633 false alarm: 5316 miss detection: 108 right detected: 317
FAR: 0.932958932959
MDR: 0.282722513089
RCL: 0.829842931937
RRL: 0.0562755192615
total: 382 detected: 5520 false alarm: 5151 miss detection: 71 right detected: 369
FAR: 0.930959696367
MDR: 0.185863874346
RCL: 0.965968586387
RRL: 0.066847826087
========winlen:  200 ==========
total: 382 detected: 22631 false alarm: 22050 miss detection: 21 right detected: 581
FAR: 0.982970756063
MDR: 0.0549738219895
RCL: 1.52094240838
RRL: 0.025672749768
total: 382 detected: 16980 false alarm: 16535 miss detection: 52 right detected: 445
FAR: 0.977419164154
MDR: 0.13612565445
RCL: 1.16492146597
RRL: 0.0262073027091
total: 382 detected: 16980 false alarm: 16535 miss detection: 52 right detected: 445
FAR: 0.977419164154
MDR: 0.13612565445
RCL: 1.16492146597
RRL: 0.0262073027091
total: 382 detected: 5692 false alarm: 5380 miss detection: 101 right detected: 312
FAR: 0.933703575148
MDR: 0.264397905759
RCL: 0.816753926702
RRL: 0.0548137737175
total: 382 detected: 5594 false alarm: 5230 miss detection: 77 right detected: 364
FAR: 0.931931575196
MDR: 0.201570680628
RCL: 0.952879581152
RRL: 0.0650697175545
========winlen:  250 ==========
total: 382 detected: 21738 false alarm: 21173 miss detection: 24 right detected: 565
FAR: 0.98227789376
MDR: 0.0628272251309
RCL: 1.47905759162
RRL: 0.0259913515503
total: 382 detected: 16319 false alarm: 15869 miss detection: 48 right detected: 450
FAR: 0.976493754231
MDR: 0.125654450262
RCL: 1.1780104712
RRL: 0.0275752190698
total: 382 detected: 16319 false alarm: 15869 miss detection: 48 right detected: 450
FAR: 0.976493754231
MDR: 0.125654450262
RCL: 1.1780104712
RRL: 0.0275752190698
total: 382 detected: 5522 false alarm: 5226 miss detection: 115 right detected: 296
FAR: 0.931883024251
MDR: 0.301047120419
RCL: 0.774869109948
RRL: 0.0536037667512
total: 382 detected: 5435 false alarm: 5094 miss detection: 93 right detected: 341
FAR: 0.930241051863
MDR: 0.243455497382
RCL: 0.892670157068
RRL: 0.0627414903404
========winlen:  300 ==========
total: 382 detected: 20883 false alarm: 20372 miss detection: 32 right detected: 511
FAR: 0.981593909608
MDR: 0.0837696335079
RCL: 1.33769633508
RRL: 0.0244696643203
total: 382 detected: 15559 false alarm: 15148 miss detection: 56 right detected: 411
FAR: 0.975402446877
MDR: 0.146596858639
RCL: 1.07591623037
RRL: 0.0264155794074
total: 382 detected: 15559 false alarm: 15148 miss detection: 56 right detected: 411
FAR: 0.975402446877
MDR: 0.146596858639
RCL: 1.07591623037
RRL: 0.0264155794074
total: 382 detected: 5292 false alarm: 5004 miss detection: 112 right detected: 288
FAR: 0.929075380616
MDR: 0.293193717277
RCL: 0.753926701571
RRL: 0.0544217687075
total: 382 detected: 5208 false alarm: 4861 miss detection: 81 right detected: 347
FAR: 0.927140949838
MDR: 0.212041884817
RCL: 0.908376963351
RRL: 0.0666282642089


//////////////l=1, h=2///////////////
========winlen: 25 ==========
total: 382 detected: 31754 false alarm: 31014 miss detection: 8 right detected: 740
FAR: 0.987832844948
MDR: 0.020942408377
RCL: 1.93717277487
RRL: 0.0233041506582
total: 382 detected: 27052 false alarm: 26465 miss detection: 39 right detected: 587
FAR: 0.98577122211
MDR: 0.102094240838
RCL: 1.53664921466
RRL: 0.02169895017
total: 382 detected: 27052 false alarm: 26465 miss detection: 39 right detected: 587
FAR: 0.98577122211
MDR: 0.102094240838
RCL: 1.53664921466
RRL: 0.02169895017
total: 382 detected: 492 false alarm: 439 miss detection: 329 right detected: 53
FAR: 0.534713763703
MDR: 0.861256544503
RCL: 0.138743455497
RRL: 0.107723577236
total: 382 detected: 492 false alarm: 430 miss detection: 322 right detected: 62
FAR: 0.529556650246
MDR: 0.842931937173
RCL: 0.162303664921
RRL: 0.126016260163
========winlen: 50 ==========
total: 382 detected: 28827 false alarm: 28137 miss detection: 22 right detected: 690
FAR: 0.986605420947
MDR: 0.0575916230366
RCL: 1.80628272251
RRL: 0.0239358934332
total: 382 detected: 22947 false alarm: 22436 miss detection: 49 right detected: 511
FAR: 0.983258830748
MDR: 0.128272251309
RCL: 1.33769633508
RRL: 0.022268706149
total: 382 detected: 22947 false alarm: 22436 miss detection: 49 right detected: 511
FAR: 0.983258830748
MDR: 0.128272251309
RCL: 1.33769633508
RRL: 0.022268706149
total: 382 detected: 634 false alarm: 559 miss detection: 307 right detected: 75
FAR: 0.594048884166
MDR: 0.803664921466
RCL: 0.196335078534
RRL: 0.118296529968
total: 382 detected: 634 false alarm: 544 miss detection: 297 right detected: 90
FAR: 0.58747300216
MDR: 0.777486910995
RCL: 0.235602094241
RRL: 0.141955835962
========winlen: 75 ==========
total: 382 detected: 27006 false alarm: 26317 miss detection: 23 right detected: 689
FAR: 0.985692348028
MDR: 0.0602094240838
RCL: 1.80366492147
RRL: 0.0255128489965
total: 382 detected: 20935 false alarm: 20423 miss detection: 55 right detected: 512
FAR: 0.98163902908
MDR: 0.143979057592
RCL: 1.34031413613
RRL: 0.0244566515405
total: 382 detected: 20935 false alarm: 20423 miss detection: 55 right detected: 512
FAR: 0.98163902908
MDR: 0.143979057592
RCL: 1.34031413613
RRL: 0.0244566515405
total: 382 detected: 697 false alarm: 605 miss detection: 292 right detected: 92
FAR: 0.612968591692
MDR: 0.764397905759
RCL: 0.240837696335
RRL: 0.131994261119
total: 382 detected: 694 false alarm: 579 miss detection: 276 right detected: 115
FAR: 0.602497398543
MDR: 0.722513089005
RCL: 0.301047120419
RRL: 0.165706051873
========winlen: 100 ==========
total: 382 detected: 25706 false alarm: 25045 miss detection: 15 right detected: 661
FAR: 0.984976599678
MDR: 0.0392670157068
RCL: 1.73036649215
RRL: 0.0257138411266
total: 382 detected: 19774 false alarm: 19279 miss detection: 56 right detected: 495
FAR: 0.980570672906
MDR: 0.146596858639
RCL: 1.29581151832
RRL: 0.0250328714474
total: 382 detected: 19774 false alarm: 19279 miss detection: 56 right detected: 495
FAR: 0.980570672906
MDR: 0.146596858639
RCL: 1.29581151832
RRL: 0.0250328714474
total: 382 detected: 669 false alarm: 579 miss detection: 292 right detected: 90
FAR: 0.602497398543
MDR: 0.764397905759
RCL: 0.235602094241
RRL: 0.134529147982
total: 382 detected: 669 false alarm: 562 miss detection: 281 right detected: 107
FAR: 0.595338983051
MDR: 0.735602094241
RCL: 0.280104712042
RRL: 0.159940209268
========winlen: 125 ==========
total: 382 detected: 24829 false alarm: 24186 miss detection: 16 right detected: 643
FAR: 0.984451318789
MDR: 0.0418848167539
RCL: 1.6832460733
RRL: 0.0258971364131
total: 382 detected: 19015 false alarm: 18549 miss detection: 51 right detected: 466
FAR: 0.97982145687
MDR: 0.133507853403
RCL: 1.21989528796
RRL: 0.024506968183
total: 382 detected: 19015 false alarm: 18549 miss detection: 51 right detected: 466
FAR: 0.97982145687
MDR: 0.133507853403
RCL: 1.21989528796
RRL: 0.024506968183
total: 382 detected: 627 false alarm: 531 miss detection: 286 right detected: 96
FAR: 0.581599123768
MDR: 0.748691099476
RCL: 0.251308900524
RRL: 0.153110047847
total: 382 detected: 627 false alarm: 523 miss detection: 280 right detected: 104
FAR: 0.577900552486
MDR: 0.732984293194
RCL: 0.272251308901
RRL: 0.165869218501
========winlen: 150 ==========
total: 382 detected: 23988 false alarm: 23358 miss detection: 19 right detected: 630
FAR: 0.983909014322
MDR: 0.0497382198953
RCL: 1.64921465969
RRL: 0.0262631315658
total: 382 detected: 18217 false alarm: 17742 miss detection: 48 right detected: 475
FAR: 0.978922975061
MDR: 0.125654450262
RCL: 1.24345549738
RRL: 0.026074545754
total: 382 detected: 18217 false alarm: 17742 miss detection: 48 right detected: 475
FAR: 0.978922975061
MDR: 0.125654450262
RCL: 1.24345549738
RRL: 0.026074545754
total: 382 detected: 681 false alarm: 571 miss detection: 272 right detected: 110
FAR: 0.599160545645
MDR: 0.712041884817
RCL: 0.287958115183
RRL: 0.161527165932
total: 382 detected: 681 false alarm: 551 miss detection: 256 right detected: 130
FAR: 0.590568060021
MDR: 0.670157068063
RCL: 0.340314136126
RRL: 0.190895741557
========winlen: 200 ==========
total: 382 detected: 22631 false alarm: 22050 miss detection: 21 right detected: 581
FAR: 0.982970756063
MDR: 0.0549738219895
RCL: 1.52094240838
RRL: 0.025672749768
total: 382 detected: 16980 false alarm: 16535 miss detection: 52 right detected: 445
FAR: 0.977419164154
MDR: 0.13612565445
RCL: 1.16492146597
RRL: 0.0262073027091
total: 382 detected: 16980 false alarm: 16535 miss detection: 52 right detected: 445
FAR: 0.977419164154
MDR: 0.13612565445
RCL: 1.16492146597
RRL: 0.0262073027091
total: 382 detected: 641 false alarm: 525 miss detection: 267 right detected: 116
FAR: 0.578831312018
MDR: 0.698952879581
RCL: 0.303664921466
RRL: 0.18096723869
total: 382 detected: 640 false alarm: 510 miss detection: 255 right detected: 130
FAR: 0.571748878924
MDR: 0.667539267016
RCL: 0.340314136126
RRL: 0.203125
========winlen: 250 ==========
total: 382 detected: 21738 false alarm: 21173 miss detection: 24 right detected: 565
FAR: 0.98227789376
MDR: 0.0628272251309
RCL: 1.47905759162
RRL: 0.0259913515503
total: 382 detected: 16319 false alarm: 15869 miss detection: 48 right detected: 450
FAR: 0.976493754231
MDR: 0.125654450262
RCL: 1.1780104712
RRL: 0.0275752190698
total: 382 detected: 16319 false alarm: 15869 miss detection: 48 right detected: 450
FAR: 0.976493754231
MDR: 0.125654450262
RCL: 1.1780104712
RRL: 0.0275752190698
total: 382 detected: 617 false alarm: 505 miss detection: 270 right detected: 112
FAR: 0.569334836528
MDR: 0.706806282723
RCL: 0.293193717277
RRL: 0.18152350081
total: 382 detected: 617 false alarm: 493 miss detection: 263 right detected: 124
FAR: 0.563428571429
MDR: 0.688481675393
RCL: 0.324607329843
RRL: 0.200972447326
========winlen: 300 ==========
total: 382 detected: 20883 false alarm: 20372 miss detection: 32 right detected: 511
FAR: 0.981593909608
MDR: 0.0837696335079
RCL: 1.33769633508
RRL: 0.0244696643203
total: 382 detected: 15559 false alarm: 15148 miss detection: 56 right detected: 411
FAR: 0.975402446877
MDR: 0.146596858639
RCL: 1.07591623037
RRL: 0.0264155794074
total: 382 detected: 15559 false alarm: 15148 miss detection: 56 right detected: 411
FAR: 0.975402446877
MDR: 0.146596858639
RCL: 1.07591623037
RRL: 0.0264155794074
total: 382 detected: 604 false alarm: 478 miss detection: 256 right detected: 126
FAR: 0.555813953488
MDR: 0.670157068063
RCL: 0.329842931937
RRL: 0.208609271523
total: 382 detected: 603 false alarm: 465 miss detection: 247 right detected: 138
FAR: 0.548996458087
MDR: 0.646596858639
RCL: 0.361256544503
RRL: 0.228855721393

//////////////l=1, h=3///////////////
========winlen: 25 ==========
total: 382 detected: 31754 false alarm: 31014 miss detection: 8 right detected: 740
FAR: 0.987832844948
MDR: 0.020942408377
RCL: 1.93717277487
RRL: 0.0233041506582
total: 382 detected: 27052 false alarm: 26465 miss detection: 39 right detected: 587
FAR: 0.98577122211
MDR: 0.102094240838
RCL: 1.53664921466
RRL: 0.02169895017
total: 382 detected: 27052 false alarm: 26465 miss detection: 39 right detected: 587
FAR: 0.98577122211
MDR: 0.102094240838
RCL: 1.53664921466
RRL: 0.02169895017
total: 382 detected: 137 false alarm: 117 miss detection: 362 right detected: 20
FAR: 0.234468937876
MDR: 0.947643979058
RCL: 0.0523560209424
RRL: 0.14598540146
total: 382 detected: 137 false alarm: 118 miss detection: 363 right detected: 19
FAR: 0.236
MDR: 0.950261780105
RCL: 0.0497382198953
RRL: 0.138686131387
========winlen: 50 ==========
total: 382 detected: 28827 false alarm: 28137 miss detection: 22 right detected: 690
FAR: 0.986605420947
MDR: 0.0575916230366
RCL: 1.80628272251
RRL: 0.0239358934332
total: 382 detected: 22947 false alarm: 22436 miss detection: 49 right detected: 511
FAR: 0.983258830748
MDR: 0.128272251309
RCL: 1.33769633508
RRL: 0.022268706149
total: 382 detected: 22947 false alarm: 22436 miss detection: 49 right detected: 511
FAR: 0.983258830748
MDR: 0.128272251309
RCL: 1.33769633508
RRL: 0.022268706149
total: 382 detected: 243 false alarm: 203 miss detection: 342 right detected: 40
FAR: 0.347008547009
MDR: 0.895287958115
RCL: 0.104712041885
RRL: 0.164609053498
total: 382 detected: 243 false alarm: 198 miss detection: 338 right detected: 45
FAR: 0.341379310345
MDR: 0.884816753927
RCL: 0.11780104712
RRL: 0.185185185185
========winlen: 75 ==========
total: 382 detected: 27006 false alarm: 26317 miss detection: 23 right detected: 689
FAR: 0.985692348028
MDR: 0.0602094240838
RCL: 1.80366492147
RRL: 0.0255128489965
total: 382 detected: 20935 false alarm: 20423 miss detection: 55 right detected: 512
FAR: 0.98163902908
MDR: 0.143979057592
RCL: 1.34031413613
RRL: 0.0244566515405
total: 382 detected: 20935 false alarm: 20423 miss detection: 55 right detected: 512
FAR: 0.98163902908
MDR: 0.143979057592
RCL: 1.34031413613
RRL: 0.0244566515405
total: 382 detected: 270 false alarm: 231 miss detection: 343 right detected: 39
FAR: 0.376835236542
MDR: 0.897905759162
RCL: 0.102094240838
RRL: 0.144444444444
total: 382 detected: 270 false alarm: 224 miss detection: 337 right detected: 46
FAR: 0.369636963696
MDR: 0.88219895288
RCL: 0.120418848168
RRL: 0.17037037037
========winlen: 100 ==========
total: 382 detected: 25706 false alarm: 25045 miss detection: 15 right detected: 661
FAR: 0.984976599678
MDR: 0.0392670157068
RCL: 1.73036649215
RRL: 0.0257138411266
total: 382 detected: 19774 false alarm: 19279 miss detection: 56 right detected: 495
FAR: 0.980570672906
MDR: 0.146596858639
RCL: 1.29581151832
RRL: 0.0250328714474
total: 382 detected: 19774 false alarm: 19279 miss detection: 56 right detected: 495
FAR: 0.980570672906
MDR: 0.146596858639
RCL: 1.29581151832
RRL: 0.0250328714474
total: 382 detected: 254 false alarm: 212 miss detection: 340 right detected: 42
FAR: 0.356902356902
MDR: 0.890052356021
RCL: 0.109947643979
RRL: 0.165354330709
total: 382 detected: 254 false alarm: 208 miss detection: 337 right detected: 46
FAR: 0.352542372881
MDR: 0.88219895288
RCL: 0.120418848168
RRL: 0.181102362205
========winlen: 125 ==========
total: 382 detected: 24829 false alarm: 24186 miss detection: 16 right detected: 643
FAR: 0.984451318789
MDR: 0.0418848167539
RCL: 1.6832460733
RRL: 0.0258971364131
total: 382 detected: 19015 false alarm: 18549 miss detection: 51 right detected: 466
FAR: 0.97982145687
MDR: 0.133507853403
RCL: 1.21989528796
RRL: 0.024506968183
total: 382 detected: 19015 false alarm: 18549 miss detection: 51 right detected: 466
FAR: 0.97982145687
MDR: 0.133507853403
RCL: 1.21989528796
RRL: 0.024506968183
total: 382 detected: 263 false alarm: 217 miss detection: 336 right detected: 46
FAR: 0.362270450751
MDR: 0.879581151832
RCL: 0.120418848168
RRL: 0.174904942966
total: 382 detected: 263 false alarm: 210 miss detection: 330 right detected: 53
FAR: 0.35472972973
MDR: 0.86387434555
RCL: 0.138743455497
RRL: 0.201520912548
========winlen: 150 ==========
total: 382 detected: 23988 false alarm: 23358 miss detection: 19 right detected: 630
FAR: 0.983909014322
MDR: 0.0497382198953
RCL: 1.64921465969
RRL: 0.0262631315658
total: 382 detected: 18217 false alarm: 17742 miss detection: 48 right detected: 475
FAR: 0.978922975061
MDR: 0.125654450262
RCL: 1.24345549738
RRL: 0.026074545754
total: 382 detected: 18217 false alarm: 17742 miss detection: 48 right detected: 475
FAR: 0.978922975061
MDR: 0.125654450262
RCL: 1.24345549738
RRL: 0.026074545754
total: 382 detected: 271 false alarm: 210 miss detection: 321 right detected: 61
FAR: 0.35472972973
MDR: 0.840314136126
RCL: 0.159685863874
RRL: 0.225092250923
total: 382 detected: 271 false alarm: 204 miss detection: 315 right detected: 67
FAR: 0.348122866894
MDR: 0.824607329843
RCL: 0.175392670157
RRL: 0.247232472325
========winlen: 200 ==========
total: 382 detected: 22631 false alarm: 22050 miss detection: 21 right detected: 581
FAR: 0.982970756063
MDR: 0.0549738219895
RCL: 1.52094240838
RRL: 0.025672749768
total: 382 detected: 16980 false alarm: 16535 miss detection: 52 right detected: 445
FAR: 0.977419164154
MDR: 0.13612565445
RCL: 1.16492146597
RRL: 0.0262073027091
total: 382 detected: 16980 false alarm: 16535 miss detection: 52 right detected: 445
FAR: 0.977419164154
MDR: 0.13612565445
RCL: 1.16492146597
RRL: 0.0262073027091
total: 382 detected: 271 false alarm: 208 miss detection: 319 right detected: 63
FAR: 0.352542372881
MDR: 0.835078534031
RCL: 0.164921465969
RRL: 0.232472324723
total: 382 detected: 271 false alarm: 202 miss detection: 313 right detected: 69
FAR: 0.345890410959
MDR: 0.819371727749
RCL: 0.180628272251
RRL: 0.254612546125
========winlen: 250 ==========
total: 382 detected: 21738 false alarm: 21173 miss detection: 24 right detected: 565
FAR: 0.98227789376
MDR: 0.0628272251309
RCL: 1.47905759162
RRL: 0.0259913515503
total: 382 detected: 16319 false alarm: 15869 miss detection: 48 right detected: 450
FAR: 0.976493754231
MDR: 0.125654450262
RCL: 1.1780104712
RRL: 0.0275752190698
total: 382 detected: 16319 false alarm: 15869 miss detection: 48 right detected: 450
FAR: 0.976493754231
MDR: 0.125654450262
RCL: 1.1780104712
RRL: 0.0275752190698
total: 382 detected: 281 false alarm: 213 miss detection: 314 right detected: 68
FAR: 0.357983193277
MDR: 0.821989528796
RCL: 0.178010471204
RRL: 0.241992882562
total: 382 detected: 281 false alarm: 209 miss detection: 310 right detected: 72
FAR: 0.353637901861
MDR: 0.811518324607
RCL: 0.188481675393
RRL: 0.256227758007
========winlen: 300 ==========
total: 382 detected: 20883 false alarm: 20372 miss detection: 32 right detected: 511
FAR: 0.981593909608
MDR: 0.0837696335079
RCL: 1.33769633508
RRL: 0.0244696643203
total: 382 detected: 15559 false alarm: 15148 miss detection: 56 right detected: 411
FAR: 0.975402446877
MDR: 0.146596858639
RCL: 1.07591623037
RRL: 0.0264155794074
total: 382 detected: 15559 false alarm: 15148 miss detection: 56 right detected: 411
FAR: 0.975402446877
MDR: 0.146596858639
RCL: 1.07591623037
RRL: 0.0264155794074
total: 382 detected: 276 false alarm: 201 miss detection: 307 right detected: 75
FAR: 0.344768439108
MDR: 0.803664921466
RCL: 0.196335078534
RRL: 0.271739130435
total: 382 detected: 276 false alarm: 193 miss detection: 300 right detected: 83
FAR: 0.335652173913
MDR: 0.785340314136
RCL: 0.217277486911
RRL: 0.300724637681


//////////////l=2, h=2///////////////
========winlen: 25 ==========
total: 382 detected: 31754 false alarm: 31014 miss detection: 8 right detected: 740
FAR: 0.987832844948
MDR: 0.020942408377
RCL: 1.93717277487
RRL: 0.0233041506582
total: 382 detected: 120 false alarm: 108 miss detection: 370 right detected: 12
FAR: 0.220408163265
MDR: 0.968586387435
RCL: 0.0314136125654
RRL: 0.1
total: 382 detected: 120 false alarm: 108 miss detection: 370 right detected: 12
FAR: 0.220408163265
MDR: 0.968586387435
RCL: 0.0314136125654
RRL: 0.1
total: 382 detected: 90 false alarm: 64 miss detection: 356 right detected: 26
FAR: 0.143497757848
MDR: 0.931937172775
RCL: 0.0680628272251
RRL: 0.288888888889
total: 382 detected: 89 false alarm: 62 miss detection: 355 right detected: 27
FAR: 0.13963963964
MDR: 0.929319371728
RCL: 0.0706806282723
RRL: 0.303370786517
========winlen: 50 ==========
total: 382 detected: 28827 false alarm: 28137 miss detection: 22 right detected: 690
FAR: 0.986605420947
MDR: 0.0575916230366
RCL: 1.80628272251
RRL: 0.0239358934332
total: 382 detected: 246 false alarm: 220 miss detection: 356 right detected: 26
FAR: 0.365448504983
MDR: 0.931937172775
RCL: 0.0680628272251
RRL: 0.105691056911
total: 382 detected: 246 false alarm: 220 miss detection: 356 right detected: 26
FAR: 0.365448504983
MDR: 0.931937172775
RCL: 0.0680628272251
RRL: 0.105691056911
total: 382 detected: 179 false alarm: 136 miss detection: 339 right detected: 43
FAR: 0.262548262548
MDR: 0.887434554974
RCL: 0.112565445026
RRL: 0.240223463687
total: 382 detected: 179 false alarm: 129 miss detection: 333 right detected: 50
FAR: 0.252446183953
MDR: 0.871727748691
RCL: 0.130890052356
RRL: 0.279329608939
========winlen: 75 ==========
total: 382 detected: 27006 false alarm: 26317 miss detection: 23 right detected: 689
FAR: 0.985692348028
MDR: 0.0602094240838
RCL: 1.80366492147
RRL: 0.0255128489965
total: 382 detected: 252 false alarm: 218 miss detection: 348 right detected: 34
FAR: 0.363333333333
MDR: 0.910994764398
RCL: 0.0890052356021
RRL: 0.134920634921
total: 382 detected: 252 false alarm: 218 miss detection: 348 right detected: 34
FAR: 0.363333333333
MDR: 0.910994764398
RCL: 0.0890052356021
RRL: 0.134920634921
total: 382 detected: 208 false alarm: 160 miss detection: 334 right detected: 48
FAR: 0.29520295203
MDR: 0.874345549738
RCL: 0.125654450262
RRL: 0.230769230769
total: 382 detected: 208 false alarm: 157 miss detection: 332 right detected: 51
FAR: 0.291280148423
MDR: 0.869109947644
RCL: 0.133507853403
RRL: 0.245192307692
========winlen: 100 ==========
total: 382 detected: 25706 false alarm: 25045 miss detection: 15 right detected: 661
FAR: 0.984976599678
MDR: 0.0392670157068
RCL: 1.73036649215
RRL: 0.0257138411266
total: 382 detected: 265 false alarm: 225 miss detection: 342 right detected: 40
FAR: 0.370675453048
MDR: 0.895287958115
RCL: 0.104712041885
RRL: 0.150943396226
total: 382 detected: 265 false alarm: 225 miss detection: 342 right detected: 40
FAR: 0.370675453048
MDR: 0.895287958115
RCL: 0.104712041885
RRL: 0.150943396226
total: 382 detected: 243 false alarm: 175 miss detection: 314 right detected: 68
FAR: 0.314183123878
MDR: 0.821989528796
RCL: 0.178010471204
RRL: 0.279835390947
total: 382 detected: 243 false alarm: 169 miss detection: 310 right detected: 74
FAR: 0.306715063521
MDR: 0.811518324607
RCL: 0.193717277487
RRL: 0.304526748971
========winlen: 125 ==========
total: 382 detected: 24829 false alarm: 24186 miss detection: 16 right detected: 643
FAR: 0.984451318789
MDR: 0.0418848167539
RCL: 1.6832460733
RRL: 0.0258971364131
total: 382 detected: 243 false alarm: 202 miss detection: 342 right detected: 41
FAR: 0.345890410959
MDR: 0.895287958115
RCL: 0.107329842932
RRL: 0.168724279835
total: 382 detected: 243 false alarm: 202 miss detection: 342 right detected: 41
FAR: 0.345890410959
MDR: 0.895287958115
RCL: 0.107329842932
RRL: 0.168724279835
total: 382 detected: 212 false alarm: 144 miss detection: 314 right detected: 68
FAR: 0.273764258555
MDR: 0.821989528796
RCL: 0.178010471204
RRL: 0.320754716981
total: 382 detected: 212 false alarm: 142 miss detection: 312 right detected: 70
FAR: 0.270992366412
MDR: 0.816753926702
RCL: 0.183246073298
RRL: 0.330188679245
========winlen: 150 ==========
total: 382 detected: 23988 false alarm: 23358 miss detection: 19 right detected: 630
FAR: 0.983909014322
MDR: 0.0497382198953
RCL: 1.64921465969
RRL: 0.0262631315658
total: 382 detected: 267 false alarm: 212 miss detection: 327 right detected: 55
FAR: 0.356902356902
MDR: 0.856020942408
RCL: 0.143979057592
RRL: 0.205992509363
total: 382 detected: 267 false alarm: 212 miss detection: 327 right detected: 55
FAR: 0.356902356902
MDR: 0.856020942408
RCL: 0.143979057592
RRL: 0.205992509363
total: 382 detected: 233 false alarm: 155 miss detection: 304 right detected: 78
FAR: 0.288640595903
MDR: 0.795811518325
RCL: 0.204188481675
RRL: 0.334763948498
total: 382 detected: 233 false alarm: 149 miss detection: 298 right detected: 84
FAR: 0.280602636535
MDR: 0.780104712042
RCL: 0.219895287958
RRL: 0.360515021459
========winlen: 200 ==========
total: 382 detected: 22631 false alarm: 22050 miss detection: 21 right detected: 581
FAR: 0.982970756063
MDR: 0.0549738219895
RCL: 1.52094240838
RRL: 0.025672749768
total: 382 detected: 291 false alarm: 227 miss detection: 318 right detected: 64
FAR: 0.372742200328
MDR: 0.832460732984
RCL: 0.167539267016
RRL: 0.219931271478
total: 382 detected: 291 false alarm: 227 miss detection: 318 right detected: 64
FAR: 0.372742200328
MDR: 0.832460732984
RCL: 0.167539267016
RRL: 0.219931271478
total: 382 detected: 259 false alarm: 171 miss detection: 295 right detected: 88
FAR: 0.309222423146
MDR: 0.772251308901
RCL: 0.230366492147
RRL: 0.339768339768
total: 382 detected: 259 false alarm: 160 miss detection: 285 right detected: 99
FAR: 0.29520295203
MDR: 0.746073298429
RCL: 0.259162303665
RRL: 0.382239382239
========winlen: 250 ==========
total: 382 detected: 21738 false alarm: 21173 miss detection: 24 right detected: 565
FAR: 0.98227789376
MDR: 0.0628272251309
RCL: 1.47905759162
RRL: 0.0259913515503
total: 382 detected: 288 false alarm: 227 miss detection: 321 right detected: 61
FAR: 0.372742200328
MDR: 0.840314136126
RCL: 0.159685863874
RRL: 0.211805555556
total: 382 detected: 288 false alarm: 227 miss detection: 321 right detected: 61
FAR: 0.372742200328
MDR: 0.840314136126
RCL: 0.159685863874
RRL: 0.211805555556
total: 382 detected: 261 false alarm: 174 miss detection: 296 right detected: 87
FAR: 0.312949640288
MDR: 0.774869109948
RCL: 0.227748691099
RRL: 0.333333333333
total: 382 detected: 261 false alarm: 172 miss detection: 295 right detected: 89
FAR: 0.310469314079
MDR: 0.772251308901
RCL: 0.232984293194
RRL: 0.340996168582
========winlen: 300 ==========
total: 382 detected: 20883 false alarm: 20372 miss detection: 32 right detected: 511
FAR: 0.981593909608
MDR: 0.0837696335079
RCL: 1.33769633508
RRL: 0.0244696643203
total: 382 detected: 317 false alarm: 246 miss detection: 310 right detected: 71
FAR: 0.391719745223
MDR: 0.811518324607
RCL: 0.185863874346
RRL: 0.223974763407
total: 382 detected: 317 false alarm: 246 miss detection: 310 right detected: 71
FAR: 0.391719745223
MDR: 0.811518324607
RCL: 0.185863874346
RRL: 0.223974763407
total: 382 detected: 288 false alarm: 189 miss detection: 282 right detected: 99
FAR: 0.330998248687
MDR: 0.738219895288
RCL: 0.259162303665
RRL: 0.34375
total: 382 detected: 288 false alarm: 184 miss detection: 277 right detected: 104
FAR: 0.325088339223
MDR: 0.725130890052
RCL: 0.272251308901
RRL: 0.361111111111


!!!!!!!!!!!!!!!!!winshift=20!!!!!!!!!!!!!!!!!!
//////////////l=1, h=1///////////////
========winlen: 25 ==========
total: 382 detected: 19299 false alarm: 18899 miss detection: 74 right detected: 400
FAR: 0.980187749598
MDR: 0.193717277487
RCL: 1.04712041885
RRL: 0.020726462511
total: 382 detected: 17039 false alarm: 16668 miss detection: 86 right detected: 371
FAR: 0.977595307918
MDR: 0.225130890052
RCL: 0.971204188482
RRL: 0.0217735782616
total: 382 detected: 17039 false alarm: 16668 miss detection: 86 right detected: 371
FAR: 0.977595307918
MDR: 0.225130890052
RCL: 0.971204188482
RRL: 0.0217735782616
total: 382 detected: 6568 false alarm: 6299 miss detection: 139 right detected: 269
FAR: 0.942822930699
MDR: 0.36387434555
RCL: 0.704188481675
RRL: 0.0409561510353
total: 382 detected: 6452 false alarm: 6099 miss detection: 99 right detected: 353
FAR: 0.94105847863
MDR: 0.259162303665
RCL: 0.924083769634
RRL: 0.054711717297
========winlen: 50 ==========
total: 382 detected: 16098 false alarm: 15685 miss detection: 54 right detected: 413
FAR: 0.976224559656
MDR: 0.141361256545
RCL: 1.08115183246
RRL: 0.0256553609144
total: 382 detected: 14120 false alarm: 13745 miss detection: 66 right detected: 375
FAR: 0.972959580944
MDR: 0.17277486911
RCL: 0.98167539267
RRL: 0.0265580736544
total: 382 detected: 14120 false alarm: 13745 miss detection: 66 right detected: 375
FAR: 0.972959580944
MDR: 0.17277486911
RCL: 0.98167539267
RRL: 0.0265580736544
total: 382 detected: 8509 false alarm: 8185 miss detection: 93 right detected: 324
FAR: 0.955410295319
MDR: 0.243455497382
RCL: 0.848167539267
RRL: 0.038077329886
total: 382 detected: 8342 false alarm: 7942 miss detection: 63 right detected: 400
FAR: 0.954108601634
MDR: 0.164921465969
RCL: 1.04712041885
RRL: 0.0479501318629
========winlen: 75 ==========
total: 382 detected: 14806 false alarm: 14398 miss detection: 68 right detected: 408
FAR: 0.974154262517
MDR: 0.178010471204
RCL: 1.06806282723
RRL: 0.0275563960557
total: 382 detected: 12574 false alarm: 12197 miss detection: 78 right detected: 377
FAR: 0.969631926226
MDR: 0.204188481675
RCL: 0.986910994764
RRL: 0.0299825035788
total: 382 detected: 12574 false alarm: 12197 miss detection: 78 right detected: 377
FAR: 0.969631926226
MDR: 0.204188481675
RCL: 0.986910994764
RRL: 0.0299825035788
total: 382 detected: 8093 false alarm: 7755 miss detection: 94 right detected: 338
FAR: 0.953053951088
MDR: 0.246073298429
RCL: 0.884816753927
RRL: 0.041764487829
total: 382 detected: 7941 false alarm: 7518 miss detection: 48 right detected: 423
FAR: 0.95164556962
MDR: 0.125654450262
RCL: 1.10732984293
RRL: 0.0532678503967
========winlen: 100 ==========
total: 382 detected: 14001 false alarm: 13585 miss detection: 54 right detected: 416
FAR: 0.972649817427
MDR: 0.141361256545
RCL: 1.0890052356
RRL: 0.0297121634169
total: 382 detected: 11636 false alarm: 11255 miss detection: 70 right detected: 381
FAR: 0.96717367019
MDR: 0.183246073298
RCL: 0.997382198953
RRL: 0.0327432107253
total: 382 detected: 11636 false alarm: 11255 miss detection: 70 right detected: 381
FAR: 0.96717367019
MDR: 0.183246073298
RCL: 0.997382198953
RRL: 0.0327432107253
total: 382 detected: 7701 false alarm: 7367 miss detection: 86 right detected: 334
FAR: 0.950703316557
MDR: 0.225130890052
RCL: 0.874345549738
RRL: 0.0433709907804
total: 382 detected: 7612 false alarm: 7206 miss detection: 56 right detected: 406
FAR: 0.949657353716
MDR: 0.146596858639
RCL: 1.06282722513
RRL: 0.0533368365738
========winlen: 125 ==========
total: 382 detected: 13552 false alarm: 13150 miss detection: 48 right detected: 402
FAR: 0.971770617795
MDR: 0.125654450262
RCL: 1.05235602094
RRL: 0.0296635182999
total: 382 detected: 11096 false alarm: 10732 miss detection: 64 right detected: 364
FAR: 0.965628936477
MDR: 0.167539267016
RCL: 0.952879581152
RRL: 0.0328046142754
total: 382 detected: 11096 false alarm: 10732 miss detection: 64 right detected: 364
FAR: 0.965628936477
MDR: 0.167539267016
RCL: 0.952879581152
RRL: 0.0328046142754
total: 382 detected: 7371 false alarm: 7042 miss detection: 79 right detected: 329
FAR: 0.948545258621
MDR: 0.206806282723
RCL: 0.861256544503
RRL: 0.0446343779677
total: 382 detected: 7261 false alarm: 6885 miss detection: 55 right detected: 376
FAR: 0.947433603963
MDR: 0.143979057592
RCL: 0.984293193717
RRL: 0.0517835008952
========winlen: 150 ==========
total: 382 detected: 13076 false alarm: 12665 miss detection: 54 right detected: 411
FAR: 0.970721238599
MDR: 0.141361256545
RCL: 1.07591623037
RRL: 0.031431630468
total: 382 detected: 10530 false alarm: 10161 miss detection: 67 right detected: 369
FAR: 0.963767428626
MDR: 0.175392670157
RCL: 0.965968586387
RRL: 0.0350427350427
total: 382 detected: 10530 false alarm: 10161 miss detection: 67 right detected: 369
FAR: 0.963767428626
MDR: 0.175392670157
RCL: 0.965968586387
RRL: 0.0350427350427
total: 382 detected: 7236 false alarm: 6904 miss detection: 78 right detected: 332
FAR: 0.947570683503
MDR: 0.204188481675
RCL: 0.869109947644
RRL: 0.0458817025981
total: 382 detected: 7125 false alarm: 6737 miss detection: 52 right detected: 388
FAR: 0.946340778199
MDR: 0.13612565445
RCL: 1.01570680628
RRL: 0.0544561403509
========winlen: 200 ==========
total: 382 detected: 12369 false alarm: 11979 miss detection: 56 right detected: 390
FAR: 0.969096351428
MDR: 0.146596858639
RCL: 1.02094240838
RRL: 0.0315304390007
total: 382 detected: 9780 false alarm: 9420 miss detection: 70 right detected: 360
FAR: 0.961028361559
MDR: 0.183246073298
RCL: 0.942408376963
RRL: 0.0368098159509
total: 382 detected: 9780 false alarm: 9420 miss detection: 70 right detected: 360
FAR: 0.961028361559
MDR: 0.183246073298
RCL: 0.942408376963
RRL: 0.0368098159509
total: 382 detected: 6666 false alarm: 6337 miss detection: 82 right detected: 329
FAR: 0.943146301533
MDR: 0.214659685864
RCL: 0.861256544503
RRL: 0.0493549354935
total: 382 detected: 6579 false alarm: 6202 miss detection: 62 right detected: 377
FAR: 0.941980558931
MDR: 0.162303664921
RCL: 0.986910994764
RRL: 0.0573035415717
========winlen: 250 ==========
total: 382 detected: 11813 false alarm: 11440 miss detection: 64 right detected: 373
FAR: 0.967687362544
MDR: 0.167539267016
RCL: 0.976439790576
RRL: 0.0315753830526
total: 382 detected: 9291 false alarm: 8948 miss detection: 79 right detected: 343
FAR: 0.959056806002
MDR: 0.206806282723
RCL: 0.897905759162
RRL: 0.0369174469917
total: 382 detected: 9291 false alarm: 8948 miss detection: 79 right detected: 343
FAR: 0.959056806002
MDR: 0.206806282723
RCL: 0.897905759162
RRL: 0.0369174469917
total: 382 detected: 6316 false alarm: 6005 miss detection: 91 right detected: 311
FAR: 0.940191012995
MDR: 0.238219895288
RCL: 0.814136125654
RRL: 0.0492400253325
total: 382 detected: 6243 false alarm: 5886 miss detection: 67 right detected: 357
FAR: 0.939055520102
MDR: 0.175392670157
RCL: 0.934554973822
RRL: 0.0571840461317
========winlen: 300 ==========
total: 382 detected: 11358 false alarm: 11001 miss detection: 66 right detected: 357
FAR: 0.966441184222
MDR: 0.17277486911
RCL: 0.934554973822
RRL: 0.0314315900687
total: 382 detected: 8871 false alarm: 8534 miss detection: 73 right detected: 337
FAR: 0.957155675191
MDR: 0.19109947644
RCL: 0.88219895288
RRL: 0.0379889527674
total: 382 detected: 8871 false alarm: 8534 miss detection: 73 right detected: 337
FAR: 0.957155675191
MDR: 0.19109947644
RCL: 0.88219895288
RRL: 0.0379889527674
total: 382 detected: 5961 false alarm: 5649 miss detection: 87 right detected: 312
FAR: 0.936660586967
MDR: 0.227748691099
RCL: 0.816753926702
RRL: 0.0523402113739
total: 382 detected: 5909 false alarm: 5537 miss detection: 58 right detected: 372
FAR: 0.935462071296
MDR: 0.151832460733
RCL: 0.973821989529
RRL: 0.0629548146895


//////////////l=1, h=2///////////////
========winlen: 25 ==========
total: 382 detected: 19299 false alarm: 18899 miss detection: 74 right detected: 400
FAR: 0.980187749598
MDR: 0.193717277487
RCL: 1.04712041885
RRL: 0.020726462511
total: 382 detected: 17039 false alarm: 16668 miss detection: 86 right detected: 371
FAR: 0.977595307918
MDR: 0.225130890052
RCL: 0.971204188482
RRL: 0.0217735782616
total: 382 detected: 17039 false alarm: 16668 miss detection: 86 right detected: 371
FAR: 0.977595307918
MDR: 0.225130890052
RCL: 0.971204188482
RRL: 0.0217735782616
total: 382 detected: 542 false alarm: 461 miss detection: 301 right detected: 81
FAR: 0.546856465006
MDR: 0.787958115183
RCL: 0.212041884817
RRL: 0.149446494465
total: 382 detected: 542 false alarm: 441 miss detection: 284 right detected: 101
FAR: 0.535844471446
MDR: 0.743455497382
RCL: 0.264397905759
RRL: 0.186346863469
========winlen: 50 ==========
total: 382 detected: 16098 false alarm: 15685 miss detection: 54 right detected: 413
FAR: 0.976224559656
MDR: 0.141361256545
RCL: 1.08115183246
RRL: 0.0256553609144
total: 382 detected: 14120 false alarm: 13745 miss detection: 66 right detected: 375
FAR: 0.972959580944
MDR: 0.17277486911
RCL: 0.98167539267
RRL: 0.0265580736544
total: 382 detected: 14120 false alarm: 13745 miss detection: 66 right detected: 375
FAR: 0.972959580944
MDR: 0.17277486911
RCL: 0.98167539267
RRL: 0.0265580736544
total: 382 detected: 703 false alarm: 598 miss detection: 279 right detected: 105
FAR: 0.610204081633
MDR: 0.730366492147
RCL: 0.274869109948
RRL: 0.149359886202
total: 382 detected: 701 false alarm: 582 miss detection: 268 right detected: 119
FAR: 0.603734439834
MDR: 0.701570680628
RCL: 0.311518324607
RRL: 0.169757489301
========winlen: 75 ==========
total: 382 detected: 14806 false alarm: 14398 miss detection: 68 right detected: 408
FAR: 0.974154262517
MDR: 0.178010471204
RCL: 1.06806282723
RRL: 0.0275563960557
total: 382 detected: 12574 false alarm: 12197 miss detection: 78 right detected: 377
FAR: 0.969631926226
MDR: 0.204188481675
RCL: 0.986910994764
RRL: 0.0299825035788
total: 382 detected: 12574 false alarm: 12197 miss detection: 78 right detected: 377
FAR: 0.969631926226
MDR: 0.204188481675
RCL: 0.986910994764
RRL: 0.0299825035788
total: 382 detected: 782 false alarm: 665 miss detection: 265 right detected: 117
FAR: 0.635148042025
MDR: 0.693717277487
RCL: 0.306282722513
RRL: 0.149616368286
total: 382 detected: 781 false alarm: 630 miss detection: 241 right detected: 151
FAR: 0.622529644269
MDR: 0.630890052356
RCL: 0.395287958115
RRL: 0.193341869398
========winlen: 100 ==========
total: 382 detected: 14001 false alarm: 13585 miss detection: 54 right detected: 416
FAR: 0.972649817427
MDR: 0.141361256545
RCL: 1.0890052356
RRL: 0.0297121634169
total: 382 detected: 11636 false alarm: 11255 miss detection: 70 right detected: 381
FAR: 0.96717367019
MDR: 0.183246073298
RCL: 0.997382198953
RRL: 0.0327432107253
total: 382 detected: 11636 false alarm: 11255 miss detection: 70 right detected: 381
FAR: 0.96717367019
MDR: 0.183246073298
RCL: 0.997382198953
RRL: 0.0327432107253
total: 382 detected: 800 false alarm: 675 miss detection: 257 right detected: 125
FAR: 0.638599810785
MDR: 0.67277486911
RCL: 0.32722513089
RRL: 0.15625
total: 382 detected: 800 false alarm: 659 miss detection: 245 right detected: 141
FAR: 0.633045148895
MDR: 0.641361256545
RCL: 0.369109947644
RRL: 0.17625
========winlen: 125 ==========
total: 382 detected: 13552 false alarm: 13150 miss detection: 48 right detected: 402
FAR: 0.971770617795
MDR: 0.125654450262
RCL: 1.05235602094
RRL: 0.0296635182999
total: 382 detected: 11096 false alarm: 10732 miss detection: 64 right detected: 364
FAR: 0.965628936477
MDR: 0.167539267016
RCL: 0.952879581152
RRL: 0.0328046142754
total: 382 detected: 11096 false alarm: 10732 miss detection: 64 right detected: 364
FAR: 0.965628936477
MDR: 0.167539267016
RCL: 0.952879581152
RRL: 0.0328046142754
total: 382 detected: 840 false alarm: 686 miss detection: 228 right detected: 154
FAR: 0.642322097378
MDR: 0.596858638743
RCL: 0.403141361257
RRL: 0.183333333333
total: 382 detected: 840 false alarm: 661 miss detection: 210 right detected: 179
FAR: 0.633748801534
MDR: 0.549738219895
RCL: 0.468586387435
RRL: 0.213095238095
========winlen: 150 ==========
total: 382 detected: 13076 false alarm: 12665 miss detection: 54 right detected: 411
FAR: 0.970721238599
MDR: 0.141361256545
RCL: 1.07591623037
RRL: 0.031431630468
total: 382 detected: 10530 false alarm: 10161 miss detection: 67 right detected: 369
FAR: 0.963767428626
MDR: 0.175392670157
RCL: 0.965968586387
RRL: 0.0350427350427
total: 382 detected: 10530 false alarm: 10161 miss detection: 67 right detected: 369
FAR: 0.963767428626
MDR: 0.175392670157
RCL: 0.965968586387
RRL: 0.0350427350427
total: 382 detected: 851 false alarm: 706 miss detection: 237 right detected: 145
FAR: 0.648897058824
MDR: 0.620418848168
RCL: 0.379581151832
RRL: 0.170387779083
total: 382 detected: 851 false alarm: 682 miss detection: 218 right detected: 169
FAR: 0.640977443609
MDR: 0.570680628272
RCL: 0.442408376963
RRL: 0.198589894242
========winlen: 200 ==========
total: 382 detected: 12369 false alarm: 11979 miss detection: 56 right detected: 390
FAR: 0.969096351428
MDR: 0.146596858639
RCL: 1.02094240838
RRL: 0.0315304390007
total: 382 detected: 9780 false alarm: 9420 miss detection: 70 right detected: 360
FAR: 0.961028361559
MDR: 0.183246073298
RCL: 0.942408376963
RRL: 0.0368098159509
total: 382 detected: 9780 false alarm: 9420 miss detection: 70 right detected: 360
FAR: 0.961028361559
MDR: 0.183246073298
RCL: 0.942408376963
RRL: 0.0368098159509
total: 382 detected: 818 false alarm: 659 miss detection: 225 right detected: 159
FAR: 0.633045148895
MDR: 0.589005235602
RCL: 0.416230366492
RRL: 0.194376528117
total: 382 detected: 817 false alarm: 635 miss detection: 207 right detected: 182
FAR: 0.624385447394
MDR: 0.541884816754
RCL: 0.476439790576
RRL: 0.22276621787
========winlen: 250 ==========
total: 382 detected: 11813 false alarm: 11440 miss detection: 64 right detected: 373
FAR: 0.967687362544
MDR: 0.167539267016
RCL: 0.976439790576
RRL: 0.0315753830526
total: 382 detected: 9291 false alarm: 8948 miss detection: 79 right detected: 343
FAR: 0.959056806002
MDR: 0.206806282723
RCL: 0.897905759162
RRL: 0.0369174469917
total: 382 detected: 9291 false alarm: 8948 miss detection: 79 right detected: 343
FAR: 0.959056806002
MDR: 0.206806282723
RCL: 0.897905759162
RRL: 0.0369174469917
total: 382 detected: 775 false alarm: 605 miss detection: 212 right detected: 170
FAR: 0.612968591692
MDR: 0.55497382199
RCL: 0.44502617801
RRL: 0.21935483871
total: 382 detected: 775 false alarm: 585 miss detection: 194 right detected: 190
FAR: 0.604963805584
MDR: 0.507853403141
RCL: 0.497382198953
RRL: 0.245161290323
========winlen: 300 ==========
total: 382 detected: 11358 false alarm: 11001 miss detection: 66 right detected: 357
FAR: 0.966441184222
MDR: 0.17277486911
RCL: 0.934554973822
RRL: 0.0314315900687
total: 382 detected: 8871 false alarm: 8534 miss detection: 73 right detected: 337
FAR: 0.957155675191
MDR: 0.19109947644
RCL: 0.88219895288
RRL: 0.0379889527674
total: 382 detected: 8871 false alarm: 8534 miss detection: 73 right detected: 337
FAR: 0.957155675191
MDR: 0.19109947644
RCL: 0.88219895288
RRL: 0.0379889527674
total: 382 detected: 779 false alarm: 589 miss detection: 194 right detected: 190
FAR: 0.606591143151
MDR: 0.507853403141
RCL: 0.497382198953
RRL: 0.243902439024
total: 382 detected: 778 false alarm: 573 miss detection: 181 right detected: 205
FAR: 0.6
MDR: 0.473821989529
RCL: 0.53664921466
RRL: 0.263496143959


//////////////l=1, h=3///////////////
========winlen: 25 ==========
total: 382 detected: 19299 false alarm: 18899 miss detection: 74 right detected: 400
FAR: 0.980187749598
MDR: 0.193717277487
RCL: 1.04712041885
RRL: 0.020726462511
total: 382 detected: 17039 false alarm: 16668 miss detection: 86 right detected: 371
FAR: 0.977595307918
MDR: 0.225130890052
RCL: 0.971204188482
RRL: 0.0217735782616
total: 382 detected: 17039 false alarm: 16668 miss detection: 86 right detected: 371
FAR: 0.977595307918
MDR: 0.225130890052
RCL: 0.971204188482
RRL: 0.0217735782616
total: 382 detected: 196 false alarm: 166 miss detection: 352 right detected: 30
FAR: 0.302919708029
MDR: 0.921465968586
RCL: 0.0785340314136
RRL: 0.15306122449
total: 382 detected: 196 false alarm: 164 miss detection: 350 right detected: 32
FAR: 0.300366300366
MDR: 0.916230366492
RCL: 0.0837696335079
RRL: 0.163265306122
========winlen: 50 ==========
total: 382 detected: 16098 false alarm: 15685 miss detection: 54 right detected: 413
FAR: 0.976224559656
MDR: 0.141361256545
RCL: 1.08115183246
RRL: 0.0256553609144
total: 382 detected: 14120 false alarm: 13745 miss detection: 66 right detected: 375
FAR: 0.972959580944
MDR: 0.17277486911
RCL: 0.98167539267
RRL: 0.0265580736544
total: 382 detected: 14120 false alarm: 13745 miss detection: 66 right detected: 375
FAR: 0.972959580944
MDR: 0.17277486911
RCL: 0.98167539267
RRL: 0.0265580736544
total: 382 detected: 287 false alarm: 233 miss detection: 328 right detected: 54
FAR: 0.378861788618
MDR: 0.858638743455
RCL: 0.141361256545
RRL: 0.188153310105
total: 382 detected: 287 false alarm: 228 miss detection: 325 right detected: 59
FAR: 0.373770491803
MDR: 0.850785340314
RCL: 0.15445026178
RRL: 0.205574912892
========winlen: 75 ==========
total: 382 detected: 14806 false alarm: 14398 miss detection: 68 right detected: 408
FAR: 0.974154262517
MDR: 0.178010471204
RCL: 1.06806282723
RRL: 0.0275563960557
total: 382 detected: 12574 false alarm: 12197 miss detection: 78 right detected: 377
FAR: 0.969631926226
MDR: 0.204188481675
RCL: 0.986910994764
RRL: 0.0299825035788
total: 382 detected: 12574 false alarm: 12197 miss detection: 78 right detected: 377
FAR: 0.969631926226
MDR: 0.204188481675
RCL: 0.986910994764
RRL: 0.0299825035788
total: 382 detected: 326 false alarm: 254 miss detection: 310 right detected: 72
FAR: 0.399371069182
MDR: 0.811518324607
RCL: 0.188481675393
RRL: 0.220858895706
total: 382 detected: 326 false alarm: 243 miss detection: 300 right detected: 83
FAR: 0.3888
MDR: 0.785340314136
RCL: 0.217277486911
RRL: 0.254601226994
========winlen: 100 ==========
total: 382 detected: 14001 false alarm: 13585 miss detection: 54 right detected: 416
FAR: 0.972649817427
MDR: 0.141361256545
RCL: 1.0890052356
RRL: 0.0297121634169
total: 382 detected: 11636 false alarm: 11255 miss detection: 70 right detected: 381
FAR: 0.96717367019
MDR: 0.183246073298
RCL: 0.997382198953
RRL: 0.0327432107253
total: 382 detected: 11636 false alarm: 11255 miss detection: 70 right detected: 381
FAR: 0.96717367019
MDR: 0.183246073298
RCL: 0.997382198953
RRL: 0.0327432107253
total: 382 detected: 324 false alarm: 245 miss detection: 303 right detected: 79
FAR: 0.390749601276
MDR: 0.793193717277
RCL: 0.206806282723
RRL: 0.243827160494
total: 382 detected: 324 false alarm: 240 miss detection: 299 right detected: 84
FAR: 0.385852090032
MDR: 0.782722513089
RCL: 0.219895287958
RRL: 0.259259259259
========winlen: 125 ==========
total: 382 detected: 13552 false alarm: 13150 miss detection: 48 right detected: 402
FAR: 0.971770617795
MDR: 0.125654450262
RCL: 1.05235602094
RRL: 0.0296635182999
total: 382 detected: 11096 false alarm: 10732 miss detection: 64 right detected: 364
FAR: 0.965628936477
MDR: 0.167539267016
RCL: 0.952879581152
RRL: 0.0328046142754
total: 382 detected: 11096 false alarm: 10732 miss detection: 64 right detected: 364
FAR: 0.965628936477
MDR: 0.167539267016
RCL: 0.952879581152
RRL: 0.0328046142754
total: 382 detected: 332 false alarm: 248 miss detection: 298 right detected: 84
FAR: 0.393650793651
MDR: 0.780104712042
RCL: 0.219895287958
RRL: 0.253012048193
total: 382 detected: 332 false alarm: 241 miss detection: 291 right detected: 91
FAR: 0.38683788122
MDR: 0.761780104712
RCL: 0.238219895288
RRL: 0.274096385542
========winlen: 150 ==========
total: 382 detected: 13076 false alarm: 12665 miss detection: 54 right detected: 411
FAR: 0.970721238599
MDR: 0.141361256545
RCL: 1.07591623037
RRL: 0.031431630468
total: 382 detected: 10530 false alarm: 10161 miss detection: 67 right detected: 369
FAR: 0.963767428626
MDR: 0.175392670157
RCL: 0.965968586387
RRL: 0.0350427350427
total: 382 detected: 10530 false alarm: 10161 miss detection: 67 right detected: 369
FAR: 0.963767428626
MDR: 0.175392670157
RCL: 0.965968586387
RRL: 0.0350427350427
total: 382 detected: 344 false alarm: 247 miss detection: 285 right detected: 97
FAR: 0.392686804452
MDR: 0.746073298429
RCL: 0.253926701571
RRL: 0.281976744186
total: 382 detected: 344 false alarm: 234 miss detection: 272 right detected: 110
FAR: 0.37987012987
MDR: 0.712041884817
RCL: 0.287958115183
RRL: 0.31976744186
========winlen: 200 ==========
total: 382 detected: 12369 false alarm: 11979 miss detection: 56 right detected: 390
FAR: 0.969096351428
MDR: 0.146596858639
RCL: 1.02094240838
RRL: 0.0315304390007
total: 382 detected: 9780 false alarm: 9420 miss detection: 70 right detected: 360
FAR: 0.961028361559
MDR: 0.183246073298
RCL: 0.942408376963
RRL: 0.0368098159509
total: 382 detected: 9780 false alarm: 9420 miss detection: 70 right detected: 360
FAR: 0.961028361559
MDR: 0.183246073298
RCL: 0.942408376963
RRL: 0.0368098159509
total: 382 detected: 320 false alarm: 227 miss detection: 289 right detected: 93
FAR: 0.372742200328
MDR: 0.756544502618
RCL: 0.243455497382
RRL: 0.290625
total: 382 detected: 320 false alarm: 220 miss detection: 282 right detected: 100
FAR: 0.365448504983
MDR: 0.738219895288
RCL: 0.261780104712
RRL: 0.3125
========winlen: 250 ==========
total: 382 detected: 11813 false alarm: 11440 miss detection: 64 right detected: 373
FAR: 0.967687362544
MDR: 0.167539267016
RCL: 0.976439790576
RRL: 0.0315753830526
total: 382 detected: 9291 false alarm: 8948 miss detection: 79 right detected: 343
FAR: 0.959056806002
MDR: 0.206806282723
RCL: 0.897905759162
RRL: 0.0369174469917
total: 382 detected: 9291 false alarm: 8948 miss detection: 79 right detected: 343
FAR: 0.959056806002
MDR: 0.206806282723
RCL: 0.897905759162
RRL: 0.0369174469917
total: 382 detected: 325 false alarm: 229 miss detection: 286 right detected: 96
FAR: 0.374795417349
MDR: 0.748691099476
RCL: 0.251308900524
RRL: 0.295384615385
total: 382 detected: 325 false alarm: 225 miss detection: 282 right detected: 100
FAR: 0.370675453048
MDR: 0.738219895288
RCL: 0.261780104712
RRL: 0.307692307692
========winlen: 300 ==========
total: 382 detected: 11358 false alarm: 11001 miss detection: 66 right detected: 357
FAR: 0.966441184222
MDR: 0.17277486911
RCL: 0.934554973822
RRL: 0.0314315900687
total: 382 detected: 8871 false alarm: 8534 miss detection: 73 right detected: 337
FAR: 0.957155675191
MDR: 0.19109947644
RCL: 0.88219895288
RRL: 0.0379889527674
total: 382 detected: 8871 false alarm: 8534 miss detection: 73 right detected: 337
FAR: 0.957155675191
MDR: 0.19109947644
RCL: 0.88219895288
RRL: 0.0379889527674
total: 382 detected: 350 false alarm: 232 miss detection: 264 right detected: 118
FAR: 0.377850162866
MDR: 0.69109947644
RCL: 0.30890052356
RRL: 0.337142857143
total: 382 detected: 350 false alarm: 226 miss detection: 258 right detected: 124
FAR: 0.371710526316
MDR: 0.675392670157
RCL: 0.324607329843
RRL: 0.354285714286


//////////////l=2, h=2///////////////
========winlen: 25 ==========
total: 382 detected: 19299 false alarm: 18899 miss detection: 74 right detected: 400
FAR: 0.980187749598
MDR: 0.193717277487
RCL: 1.04712041885
RRL: 0.020726462511
total: 382 detected: 250 false alarm: 217 miss detection: 349 right detected: 33
FAR: 0.362270450751
MDR: 0.913612565445
RCL: 0.086387434555
RRL: 0.132
total: 382 detected: 250 false alarm: 217 miss detection: 349 right detected: 33
FAR: 0.362270450751
MDR: 0.913612565445
RCL: 0.086387434555
RRL: 0.132
total: 382 detected: 215 false alarm: 163 miss detection: 330 right detected: 52
FAR: 0.299082568807
MDR: 0.86387434555
RCL: 0.13612565445
RRL: 0.241860465116
total: 382 detected: 215 false alarm: 154 miss detection: 323 right detected: 61
FAR: 0.287313432836
MDR: 0.84554973822
RCL: 0.159685863874
RRL: 0.283720930233
========winlen: 50 ==========
total: 382 detected: 16098 false alarm: 15685 miss detection: 54 right detected: 413
FAR: 0.976224559656
MDR: 0.141361256545
RCL: 1.08115183246
RRL: 0.0256553609144
total: 382 detected: 463 false alarm: 387 miss detection: 306 right detected: 76
FAR: 0.503250975293
MDR: 0.801047120419
RCL: 0.198952879581
RRL: 0.164146868251
total: 382 detected: 463 false alarm: 387 miss detection: 306 right detected: 76
FAR: 0.503250975293
MDR: 0.801047120419
RCL: 0.198952879581
RRL: 0.164146868251
total: 382 detected: 349 false alarm: 257 miss detection: 290 right detected: 92
FAR: 0.402190923318
MDR: 0.759162303665
RCL: 0.240837696335
RRL: 0.263610315186
total: 382 detected: 349 false alarm: 243 miss detection: 278 right detected: 106
FAR: 0.3888
MDR: 0.727748691099
RCL: 0.277486910995
RRL: 0.303724928367
========winlen: 75 ==========
total: 382 detected: 14806 false alarm: 14398 miss detection: 68 right detected: 408
FAR: 0.974154262517
MDR: 0.178010471204
RCL: 1.06806282723
RRL: 0.0275563960557
total: 382 detected: 526 false alarm: 433 miss detection: 289 right detected: 93
FAR: 0.531288343558
MDR: 0.756544502618
RCL: 0.243455497382
RRL: 0.17680608365
total: 382 detected: 526 false alarm: 433 miss detection: 289 right detected: 93
FAR: 0.531288343558
MDR: 0.756544502618
RCL: 0.243455497382
RRL: 0.17680608365
total: 382 detected: 424 false alarm: 302 miss detection: 262 right detected: 122
FAR: 0.441520467836
MDR: 0.685863874346
RCL: 0.319371727749
RRL: 0.287735849057
total: 382 detected: 424 false alarm: 286 miss detection: 249 right detected: 138
FAR: 0.428143712575
MDR: 0.651832460733
RCL: 0.361256544503
RRL: 0.325471698113
========winlen: 100 ==========
total: 382 detected: 14001 false alarm: 13585 miss detection: 54 right detected: 416
FAR: 0.972649817427
MDR: 0.141361256545
RCL: 1.0890052356
RRL: 0.0297121634169
total: 382 detected: 538 false alarm: 429 miss detection: 273 right detected: 109
FAR: 0.528976572133
MDR: 0.714659685864
RCL: 0.285340314136
RRL: 0.202602230483
total: 382 detected: 538 false alarm: 429 miss detection: 273 right detected: 109
FAR: 0.528976572133
MDR: 0.714659685864
RCL: 0.285340314136
RRL: 0.202602230483
total: 382 detected: 453 false alarm: 313 miss detection: 242 right detected: 140
FAR: 0.45035971223
MDR: 0.633507853403
RCL: 0.366492146597
RRL: 0.309050772627
total: 382 detected: 453 false alarm: 303 miss detection: 234 right detected: 150
FAR: 0.442335766423
MDR: 0.612565445026
RCL: 0.392670157068
RRL: 0.331125827815
========winlen: 125 ==========
total: 382 detected: 13552 false alarm: 13150 miss detection: 48 right detected: 402
FAR: 0.971770617795
MDR: 0.125654450262
RCL: 1.05235602094
RRL: 0.0296635182999
total: 382 detected: 494 false alarm: 389 miss detection: 278 right detected: 105
FAR: 0.504539559014
MDR: 0.727748691099
RCL: 0.274869109948
RRL: 0.212550607287
total: 382 detected: 494 false alarm: 389 miss detection: 278 right detected: 105
FAR: 0.504539559014
MDR: 0.727748691099
RCL: 0.274869109948
RRL: 0.212550607287
total: 382 detected: 411 false alarm: 271 miss detection: 242 right detected: 140
FAR: 0.415007656968
MDR: 0.633507853403
RCL: 0.366492146597
RRL: 0.340632603406
total: 382 detected: 411 false alarm: 260 miss detection: 231 right detected: 151
FAR: 0.404984423676
MDR: 0.604712041885
RCL: 0.395287958115
RRL: 0.367396593674
========winlen: 150 ==========
total: 382 detected: 13076 false alarm: 12665 miss detection: 54 right detected: 411
FAR: 0.970721238599
MDR: 0.141361256545
RCL: 1.07591623037
RRL: 0.031431630468
total: 382 detected: 518 false alarm: 408 miss detection: 272 right detected: 110
FAR: 0.516455696203
MDR: 0.712041884817
RCL: 0.287958115183
RRL: 0.212355212355
total: 382 detected: 518 false alarm: 408 miss detection: 272 right detected: 110
FAR: 0.516455696203
MDR: 0.712041884817
RCL: 0.287958115183
RRL: 0.212355212355
total: 382 detected: 445 false alarm: 296 miss detection: 235 right detected: 149
FAR: 0.436578171091
MDR: 0.615183246073
RCL: 0.390052356021
RRL: 0.334831460674
total: 382 detected: 444 false alarm: 281 miss detection: 222 right detected: 163
FAR: 0.42383107089
MDR: 0.581151832461
RCL: 0.426701570681
RRL: 0.367117117117
========winlen: 200 ==========
total: 382 detected: 12369 false alarm: 11979 miss detection: 56 right detected: 390
FAR: 0.969096351428
MDR: 0.146596858639
RCL: 1.02094240838
RRL: 0.0315304390007
total: 382 detected: 491 false alarm: 359 miss detection: 250 right detected: 132
FAR: 0.484480431849
MDR: 0.65445026178
RCL: 0.34554973822
RRL: 0.26883910387
total: 382 detected: 491 false alarm: 359 miss detection: 250 right detected: 132
FAR: 0.484480431849
MDR: 0.65445026178
RCL: 0.34554973822
RRL: 0.26883910387
total: 382 detected: 439 false alarm: 287 miss detection: 230 right detected: 152
FAR: 0.428998505232
MDR: 0.602094240838
RCL: 0.397905759162
RRL: 0.346241457859
total: 382 detected: 439 false alarm: 268 miss detection: 212 right detected: 171
FAR: 0.412307692308
MDR: 0.55497382199
RCL: 0.447643979058
RRL: 0.389521640091
========winlen: 250 ==========
total: 382 detected: 11813 false alarm: 11440 miss detection: 64 right detected: 373
FAR: 0.967687362544
MDR: 0.167539267016
RCL: 0.976439790576
RRL: 0.0315753830526
total: 382 detected: 487 false alarm: 358 miss detection: 253 right detected: 129
FAR: 0.483783783784
MDR: 0.662303664921
RCL: 0.337696335079
RRL: 0.264887063655
total: 382 detected: 487 false alarm: 358 miss detection: 253 right detected: 129
FAR: 0.483783783784
MDR: 0.662303664921
RCL: 0.337696335079
RRL: 0.264887063655
total: 382 detected: 433 false alarm: 274 miss detection: 223 right detected: 159
FAR: 0.417682926829
MDR: 0.583769633508
RCL: 0.416230366492
RRL: 0.367205542725
total: 382 detected: 433 false alarm: 268 miss detection: 218 right detected: 165
FAR: 0.412307692308
MDR: 0.570680628272
RCL: 0.431937172775
RRL: 0.381062355658
========winlen: 300 ==========
total: 382 detected: 11358 false alarm: 11001 miss detection: 66 right detected: 357
FAR: 0.966441184222
MDR: 0.17277486911
RCL: 0.934554973822
RRL: 0.0314315900687
total: 382 detected: 466 false alarm: 336 miss detection: 251 right detected: 130
FAR: 0.467966573816
MDR: 0.657068062827
RCL: 0.340314136126
RRL: 0.278969957082
total: 382 detected: 466 false alarm: 336 miss detection: 251 right detected: 130
FAR: 0.467966573816
MDR: 0.657068062827
RCL: 0.340314136126
RRL: 0.278969957082
total: 382 detected: 424 false alarm: 271 miss detection: 229 right detected: 153
FAR: 0.415007656968
MDR: 0.599476439791
RCL: 0.400523560209
RRL: 0.360849056604
total: 382 detected: 423 false alarm: 264 miss detection: 223 right detected: 159
FAR: 0.40866873065
MDR: 0.583769633508
RCL: 0.416230366492
RRL: 0.375886524823


