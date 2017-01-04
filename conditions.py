# -*- coding: utf-8 -* 

import numpy as np
debug = True
con = 8
a, b, c, d = [2, 2, 2, 0]

a = ["A"+str(i+1) for i in xrange(a)]
b = ["B"+str(i+1) for i in xrange(b)]
c = ["C"+str(i+1) for i in xrange(c)]
d = ["D"+str(i+1) for i in xrange(d)]

def make_label() :
	global a, b, c, d
	labels = ""
	if len(b) == 0:
		for i in a :
			labels += (i+",")
	elif len(c) == 0 :
		for i in a :
			for k in b :
				labels += (i+k+",")
	elif len(d) == 0 :
		for i in a :
			for k in b :
				for j in c :
					labels += (i+k+j+",")
	elif len(d) != 0 :
		for i in a :
			for k in b :
				for j in c :
					for s in d :
						labels += (i+k+j+s+",")
	labels = "condition," + labels[:-1]
	return labels

labels = make_label()

if debug :
	print("condition label = %s" %labels)

#labels = np.array(labels)
data = np.ones([1, con+1])
np.savetxt("condition.csv", data, delimiter=",", header=labels)
#np.savetxt("condition.csv", labels, delimiter=",", fmt="%s")
