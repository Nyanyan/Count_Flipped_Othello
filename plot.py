import math
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = "MS Gothic"

s = '''
full_search_depth 12
n_random_play 10000000
whole_avg 2.24391
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
ply 13 avg 1.61088 sd 0.831211 count 9997408
ply 14 avg 1.6913 sd 0.876789 count 9996845
ply 15 avg 1.67747 sd 0.889182 count 9996650
ply 16 avg 1.74664 sd 0.929374 count 9996207
ply 17 avg 1.73939 sd 0.943314 count 9996090
ply 18 avg 1.8012 sd 0.980495 count 9995796
ply 19 avg 1.7997 sd 0.995794 count 9995701
ply 20 avg 1.85608 sd 1.03051 count 9995486
ply 21 avg 1.8589 sd 1.04741 count 9995398
ply 22 avg 1.91122 sd 1.08053 count 9995273
ply 23 avg 1.91657 sd 1.09712 count 9995217
ply 24 avg 1.96629 sd 1.13037 count 9995140
ply 25 avg 1.97444 sd 1.14737 count 9995104
ply 26 avg 2.02226 sd 1.17958 count 9995052
ply 27 avg 2.03357 sd 1.198 count 9995024
ply 28 avg 2.07968 sd 1.22982 count 9995001
ply 29 avg 2.09421 sd 1.24907 count 9994989
ply 30 avg 2.13873 sd 1.28048 count 9994970
ply 31 avg 2.15571 sd 1.30075 count 9994955
ply 32 avg 2.20012 sd 1.33192 count 9994940
ply 33 avg 2.21817 sd 1.35154 count 9994934
ply 34 avg 2.26451 sd 1.38512 count 9994924
ply 35 avg 2.2839 sd 1.40575 count 9994914
ply 36 avg 2.33066 sd 1.43811 count 9994912
ply 37 avg 2.35231 sd 1.45974 count 9994907
ply 38 avg 2.39952 sd 1.49256 count 9994902
ply 39 avg 2.42493 sd 1.5162 count 9994897
ply 40 avg 2.47391 sd 1.55062 count 9994893
ply 41 avg 2.50192 sd 1.57387 count 9994892
ply 42 avg 2.55163 sd 1.60938 count 9994890
ply 43 avg 2.5837 sd 1.63495 count 9994887
ply 44 avg 2.63622 sd 1.66999 count 9994885
ply 45 avg 2.67323 sd 1.69923 count 9994883
ply 46 avg 2.72967 sd 1.73675 count 9994880
ply 47 avg 2.77002 sd 1.76681 count 9994873
ply 48 avg 2.83136 sd 1.80612 count 9994872
ply 49 avg 2.87867 sd 1.84078 count 9994870
ply 50 avg 2.94448 sd 1.88232 count 9994868
ply 51 avg 3.00118 sd 1.92232 count 9994867
ply 52 avg 3.07456 sd 1.96882 count 9994863
ply 53 avg 3.14183 sd 2.01321 count 9994858
ply 54 avg 3.22723 sd 2.06715 count 9994854
ply 55 avg 3.31049 sd 2.12168 count 9994850
ply 56 avg 3.41522 sd 2.18721 count 9994831
ply 57 avg 3.53119 sd 2.2607 count 9994770
ply 58 avg 3.68208 sd 2.34977 count 9994430
ply 59 avg 3.90004 sd 2.47568 count 9991081
ply 60 avg 4.34456 sd 2.69423 count 9904256
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