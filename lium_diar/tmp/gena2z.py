
fout = open('lst/bnews_b.lst','w')
temp = [chr(i) for i in range(ord("a"),ord("z")+1)]

for i in temp:
	fout.write('pab'+i+'\n')
