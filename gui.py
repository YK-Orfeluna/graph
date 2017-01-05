# -*- coding: utf-8 -* 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import Tkinter

DEBUG = True

#HEAD = 0		# headerに条件が記載されていない
HEAD = 1		# headerに条件が記載されている

FILE = "value.csv"		# 読み込むcsvファイル名

def read_csv() :
	global FILE, HEAD
	df = pd.read_csv(FILE, header=HEAD)
	data = df.values[:, 1:]
	header = df.columns.values.tolist()
	return data, header

data, header = read_csv()

Q = 3		# 質問数
def make_data() :
	global data, Q, DEBUG
	num = data.shape[0]			# 被験者数
	con = data.shape[1] / Q		# 1質問あたりの条件数
	if DEBUG :
		print("number of subject = %s" %num)
		print("number of condition = %s" %con)

	questions = ["Q"+str(i+1) for i in xrange(Q)]
	if DEBUG :
		print("question label = %s" %questions)

	return num, con, questions

num, con, questions = make_data()

def make_ylim() :
	global data, DEBUG
	dn = data.min()
	up = data.max()
	value = (up - dn) / 10
	dn -= value
	up += value
	if DEBUG :
		print("ylim from %s to %s" %(dn, up))
	return dn, up

data_min, data_max = make_ylim()

A, B, C, D = [2, 2, 2, 0]		# 各要因の水準数
def make_label() :
	global DEBUG, con, Q
	if HEAD == 1 :
		global header
		labels = header[1:con+1]

	else :
		global A, B, C, D
		a = ["A"+str(i+1) for i in xrange(a)]
		b = ["B"+str(i+1) for i in xrange(b)]
		c = ["C"+str(i+1) for i in xrange(c)]
		d = ["D"+str(i+1) for i in xrange(d)]

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
	
	labels *= Q
	if DEBUG :
		print("condition label = %s" %labels[0:con])
	return labels


labels = make_label()

def make_color(start=0.3, end=0.7) :
	global Q, DEBUG
	start = round(255 * start, 0)
	end = round(255 * end, 0)
	between = abs(end - start) / (Q - 1)
	list_c = [start]
	value = start
	for i in xrange(Q-2) :
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
	if DEBUG :
		print("color = %s" %colors)
	return colors


colors = make_color()

def t_color(backgroundcolor) :
	color = backgroundcolor[1] + backgroundcolor[2]
	color = int(color, 16)
	if color > 127 :
		text = "black"
	else :
		text = "white"
	return text

def make_graph() :
	global data, labels, colors, con

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

make_graph()
