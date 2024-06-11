
import csv
import pandas as pd
import numpy as np
import math
import re


data_appddos_list = pd.read_csv("ApplicationDDoS/app10.csv",low_memory=False)
#data_benign_list = pd.read_csv("Benign/ben10.csv",low_memory=False)
#data_botddos_list = pd.read_csv("BotnetDDoS/bot10.csv",low_memory=False)
#data_drdos_list = pd.read_csv("DrDoS/drdos10.csv",low_memory=False)
#data_lddos_list = pd.read_csv("LDDoS/lddos10.csv",low_memory=False)
#data_netddos_list = pd.read_csv("NetworkDDoS/net10.csv",low_memory=False)
#print(data_appddos_list)
'''
bwdsegmentsizeavg = data_appddos_list["Bwd Segment Size Avg"] 
data = np.array(bwdsegmentsizeavg)
d = data[11]
print(d)
data_appddos_array = np.array(data_appddos_list)
#print(data_appddos_array)
print(data_appddos_array[34701,60])
a = np.delete(data,34701,0)
print(a[34703])
'''
representation_app = data_appddos_list[["Bwd Segment Size Avg","Bwd Bulk Rate Avg","URG Flag Count","CWR Flag Count","Active Max","Down/Up Ratio","Active Min","Bwd Packet Length Std","Total Length of Bwd Packet"]]
#representation_bot = data_botddos_list[["Bwd Segment Size Avg","Bwd Bulk Rate Avg","URG Flag Count","CWR Flag Count","Active Max","Down/Up Ratio","Active Min","Bwd Packet Length Std","Total Length of Bwd Packet"]] #2626
#representation_drdos = data_drdos_list[["Bwd Segment Size Avg","Bwd Bulk Rate Avg","URG Flag Count","CWR Flag Count","Active Max","Down/Up Ratio","Active Min","Bwd Packet Length Std","Total Length of Bwd Packet"]]
#representation_lddos = data_lddos_list[["Bwd Segment Size Avg","Bwd Bulk Rate Avg","URG Flag Count","CWR Flag Count","Active Max","Down/Up Ratio","Active Min","Bwd Packet Length Std","Total Length of Bwd Packet"]]

representation_array_app = np.array(representation_app)
#representation_array_bot = np.array(representation_bot)
#representation_array_drdos = np.array(representation_drdos)
#representation_array_lddos = np.array(representation_lddos)

'''
rep = np.delete(representation_array_app,34701,0)
rep = np.delete(representation_array_bot,34701,0)
rep = np.delete(representation_array_drdos,34701,0)
rep = np.delete(representation_array_lddos,34701,0)
#print(rep[34703,8]) 
'''
row = 3949
hang = representation_array_app.shape[0]
#hang = representation_array_bot.shape[0]
print(hang)

new_array_app = representation_array_app[~(representation_array_app==0).all(axis=1)]
#new_array_bot = representation_array_bot[~(representation_array_bot==0).all(axis=1)]

print(new_array_app)

hang = new_array_app.shape[0]
print(hang)

def is_numeric_row(row):
    return all(re.match(r'^-?\d+(\.\d+)?$', str(item)) for item in row)

only_numeric_array = [row for row in new_array_app if is_numeric_row(row)]

x = 0
a_mod = 0
b_mod = 0
count = 0

#row = representation_array_bot.shape[0]
#print(row)

for i in range(1000):
    a = only_numeric_array[i,:]
    b = only_numeric_array[i+1,:]
    x = 0
    a_mod = 0
    b_mod = 0   
    for j in range(9):
        x = a[j]*b[j]+x
        a_mod = a[j]*a[j]+a_mod
        b_mod = b[j]*b[j]+b_mod
    a_mod = math.sqrt(a_mod)
    b_mod = math.sqrt(b_mod)
    if b_mod == 0 or a_mod == 0:
         y = 0
    else:
        y = x/(a_mod*b_mod)
    if y >= 0.0000001 or y == 0:
        count = count+1
print(count)
print(count/10000)
    
    

'''
a = representation_array_bot[2625,:]
b = representation_array_bot[2626,:]

print(a)
print(b)

for i in range(8):
    x = a[i]*b[i]+x
    a_mod = a[i]*a[i]+a_mod
    b_mod = b[i]*b[i]+b_mod

a_mod = math.sqrt(a_mod)
b_mod = math.sqrt(b_mod)


if b_mod == 0 or a_mod == 0:
    y = 0
else:
    y = x/(a_mod*b_mod)

print(y)
'''

