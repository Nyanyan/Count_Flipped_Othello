import math
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = "MS Gothic"

s = '''
full_search_depth 14
n_random_play 10000000
whole_avg 2.24369
ply 1 avg 1 sd 0 count 4
ply 2 avg 1 sd 0 count 12
ply 3 avg 1.14286 sd 0.349927 count 56
ply 4 avg 1.18033 sd 0.38446 count 244
ply 5 avg 1.23209 sd 0.485316 count 1396
ply 6 avg 1.35902 sd 0.576684 count 8200
ply 7 avg 1.35613 sd 0.604575 count 55092
ply 8 avg 1.46296 sd 0.668504 count 390216
ply 9 avg 1.45586 sd 0.694716 count 3005320
ply 10 avg 1.54146 sd 0.744091 count 24571192
ply 11 avg 1.54306 sd 0.770652 count 212260296
ply 12 avg 1.60909 sd 0.809349 count 1939892240
ply 13 avg 1.61895 sd 0.835977 count 18429768516
ply 14 avg 1.67161 sd 0.868672 count 184042835408
ply 15 avg 1.67734 sd 0.888833 count 9996689
ply 16 avg 1.74714 sd 0.92984 count 9996243
ply 17 avg 1.73909 sd 0.942695 count 9996119
ply 18 avg 1.80186 sd 0.981101 count 9995808
ply 19 avg 1.79991 sd 0.995374 count 9995714
ply 20 avg 1.85568 sd 1.0306 count 9995509
ply 21 avg 1.8584 sd 1.04669 count 9995442
ply 22 avg 1.90995 sd 1.08021 count 9995327
ply 23 avg 1.91705 sd 1.09767 count 9995272
ply 24 avg 1.96583 sd 1.12966 count 9995196
ply 25 avg 1.9753 sd 1.14815 count 9995149
ply 26 avg 2.02257 sd 1.18014 count 9995088
ply 27 avg 2.03375 sd 1.19821 count 9995062
ply 28 avg 2.08053 sd 1.23035 count 9995034
ply 29 avg 2.09341 sd 1.24874 count 9995012
ply 30 avg 2.1394 sd 1.28067 count 9994985
ply 31 avg 2.15486 sd 1.30003 count 9994979
ply 32 avg 2.19948 sd 1.33154 count 9994959
ply 33 avg 2.21806 sd 1.35246 count 9994944
ply 34 avg 2.26418 sd 1.38467 count 9994939
ply 35 avg 2.28418 sd 1.40552 count 9994935
ply 36 avg 2.33009 sd 1.43819 count 9994923
ply 37 avg 2.35324 sd 1.46011 count 9994916
ply 38 avg 2.3993 sd 1.49301 count 9994910
ply 39 avg 2.42543 sd 1.51591 count 9994902
ply 40 avg 2.47367 sd 1.55045 count 9994897
ply 41 avg 2.50268 sd 1.57455 count 9994896
ply 42 avg 2.55254 sd 1.60881 count 9994889
ply 43 avg 2.58394 sd 1.63494 count 9994888
ply 44 avg 2.63656 sd 1.67046 count 9994887
ply 45 avg 2.67334 sd 1.69963 count 9994885
ply 46 avg 2.72962 sd 1.73595 count 9994880
ply 47 avg 2.77165 sd 1.76759 count 9994876
ply 48 avg 2.83096 sd 1.80728 count 9994873
ply 49 avg 2.87805 sd 1.84062 count 9994869
ply 50 avg 2.94472 sd 1.88313 count 9994868
ply 51 avg 3.00071 sd 1.92152 count 9994864
ply 52 avg 3.07251 sd 1.96784 count 9994861
ply 53 avg 3.1404 sd 2.01257 count 9994857
ply 54 avg 3.22616 sd 2.06594 count 9994852
ply 55 avg 3.31042 sd 2.12162 count 9994843
ply 56 avg 3.41501 sd 2.18569 count 9994821
ply 57 avg 3.53146 sd 2.25978 count 9994748
ply 58 avg 3.68207 sd 2.34986 count 9994418
ply 59 avg 3.90071 sd 2.47539 count 9991146
ply 60 avg 4.34496 sd 2.69263 count 9904118
'''

s = s.splitlines()[1:]

full_search_depth = int(s[0].split()[1])
n_random_play = int(s[1].split()[1])
whole_avg = float(s[2].split()[1])

x = [int(elem.split()[1]) for elem in s[3:]]
avg = [float(elem.split()[3]) for elem in s[3:]]
sd = [float(elem.split()[5]) for elem in s[3:]]
count = [int(elem.split()[7]) for elem in s[3:]]
avg_plus_sd = [avg[i] + sd[i] for i in range(len(avg))]
avg_minus_sd = [avg[i] - sd[i] for i in range(len(avg))]
avg_plus_95_confidence = [avg[i] + sd[i] / math.sqrt(count[i]) * 1.96 for i in range(len(avg))]
avg_minus_95_confidence = [avg[i] - sd[i] / math.sqrt(count[i]) * 1.96 for i in range(len(avg))]

#print([sd[i] / math.sqrt(count[i]) * 1.96 for i in range(len(avg))])

plt.vlines(full_search_depth, 0, 7, color='g', linestyles='dotted')
plt.fill_between(x, avg_plus_sd, avg_minus_sd, fc="yellow")
#plt.fill_between(x, avg_plus_95_confidence, avg_minus_95_confidence, fc="yellow")
plt.plot(x, avg)
plt.xlabel('手')
plt.ylabel('返る石の平均値(+-標準偏差)')
plt.ylim([0, 7])
plt.grid()
plt.show()