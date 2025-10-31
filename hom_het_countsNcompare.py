# abstract allele freq
# variant detection program 

import random

# as inputs
rounds = 10
	# change to 1_000_000
coverage = 24
	# 20 doesnt show much, so started with 24
	# change to 30
	# try 40

# HET
het = [0] * (coverage+1) 

for i in range(rounds):
	for j in range(coverage):
		mom = 0 # ref allele
		dad = 0
			if random.randint(0, 1) == 0: mom += 1
			else:                         dad += 1
		het[mom] += 1
		
for i, c in enumerate(het):
	print('het', i, coverage-i, c, sep='\t')

# HOM
mut = 0.01
hom = [0] * (coverage+1)
for _ in range(trials):
	c = 0
	g = 0
	t = 0
	for _ in range(coverage):
		if r = random.randint(0, 2)
			if   r == 0: c += 1
			elif r == 1: g += 1
			else:        t += 1
	a = [c, g, t]
	# if a or b have value in them
	#if a[0] or a[1]: continue
	#print(a)
	fake_count = a[2]
	#print(fake_counts)
	hom[fake_count] += 1

for i, c in enumerate(hom):
	print('hom', i, coverage-i, c, sep='/t')
