# -*- coding: utf-8 -* 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

debug = True

file = "value.csv"		# 読み込むcsvファイル名
df = pd.read_csv(file, header=1)
header = df.columns.values.tolist()
data = df.values[:, 1:]

num = data.shape[0]			# 被験者数
q = 3						# 質問数
con = data.shape[1] / q		# 1質問あたりの条件数
if debug :
	print("number of subject = %s" %num)
	print("number of condition = %s" %con)

labels = header[1:con+1]
labels *= q
if debug :
	print("condition label = %s" %labels[:con])

def make_ylim() :
	global data
	dn = data.min()
	up = data.max()
	value = abs(up - dn) / 10
	dn -= value
	up += value
	return dn, up

data_min, data_max = make_ylim()
if debug :
	print("ylim from %s to %s" %(data_min, data_max))

questions = ["Q"+str(i+1) for i in xrange(q)]
if debug :
	print("question label = %s" %questions)
	
"""
a, b, c, d = [2, 2, 2, 0]

a = ["A"+str(i+1) for i in xrange(a)]
b = ["B"+str(i+1) for i in xrange(b)]
c = ["C"+str(i+1) for i in xrange(c)]
d = ["D"+str(i+1) for i in xrange(d)]

def make_label() :
	global a, b, c, d, q
	labels = []
	if len(b) == 0:
		for i in a :
			labels.append(i)
	elif len(c) == 0 :
		for i in a :
			for k in b :
				labels.append(i+k)
	elif len(d) == 0 :
		for i in a :
			for k in b :
				for j in c :
					labels.append(i+k+j)
	elif len(d) != 0 :
		for i in a :
			for k in b :
				for j in c :
					for s in d :
						labels.append(i+k+j+s)
	labels *= q
	return labels
labels = make_label()
if debug :
	print("condition label = %s" %labels[0:con])
"""

def make_color() :
	global q
	start = 0.3
	start = round(255 * start, 0)
	end = 0.7
	end = round(255 * end, 0)
	between = abs(end - start) / (q - 1)
	list_c = [start]
	value = start
	for i in xrange(q-2) :
		if start < end :
			value += between
		else :
			value -= between
		list_c.append(value)
	list_c.append(end)
	colors = []
	for i in list_c :
		value = "%x" %i
		value *= 3
		colors.append("#"+value)
	return colors
colors = make_color()
if debug :
	print("color = %s" %colors)

fig, ax1 = plt.subplots()

bp = plt.boxplot(data, labels=labels, showmeans=True, patch_artist=True)
plt.setp(bp["medians"], color="red", linewidth=3)

for i,x in enumerate(colors) :
	p = i*con
	for i in xrange(con) :
		bp["boxes"][p+i].set_facecolor(x)

plt.ylim(data_min, data_max)

xtickNames = plt.setp(ax1, xticklabels=labels)
plt.setp(xtickNames, rotation=45, fontsize=12)

def t_color(backgroundcolor) :
	color = backgroundcolor[1] + backgroundcolor[2]
	color = int(color, 16)
	if color > 127 :
		text = "black"
	else :
		text = "white"
	return text

x = 0.80
y = 0.83
for i,j in enumerate(questions) :
	if i == len(questions) / 2 :
		x = 0.85
		y = 0.83
		#t_color = "white"
	plt.figtext(x, y, j, backgroundcolor=colors[i], weight="roman", size="small", color=t_color(colors[i]))
	y -= 0.03

plt.show()