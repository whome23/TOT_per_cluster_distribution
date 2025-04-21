import h5py 
import numpy as np 
import matplotlib.pyplot as plt 
import sys
import re
import os
# import pandas as pd
# import tables
# import nexusformat.nexus as nx

# saved_dir="./Analyzed_data/spectrum/"
args = sys.argv

filename = sys.argv[1]
save_Fig_dir=args[2]
Run_number=args[3]

with h5py.File(filename) as h5f:
    # x = h5f["neutrons/x"][:]
    # y = h5f["neutrons/y"][:]
    tot = h5f["neutrons/tot_ns"][:]
    # nhits = h5f["neutrons/nHits"][:]

# print(nhits)

Max_tot=int(tot.max())
# print(Max_nhit)

xaxis_LiFneutron=plt.hist(tot, int(Max_tot/25),range=[0, Max_tot],alpha = 0.2, label='Neutron' )[1]
yaxis_LiFneutron=plt.hist(tot, int(Max_tot/25),range=[0, Max_tot],alpha = 0.2, label='Neutron' )[0]
plt.close()

xaxis_LiFneutron_1=xaxis_LiFneutron[:-1]
sum_for_hits_times_clustersize=np.sum(xaxis_LiFneutron_1*yaxis_LiFneutron)
sum_for_hits=np.sum(yaxis_LiFneutron)

average_cluster_size=sum_for_hits_times_clustersize/sum_for_hits
average_cluster_size=round(average_cluster_size,3)

std_dev=np.std(tot)
# print(std_dev)
# print(int(filename.split(':')[1]))
# numbers=[]
# for char in filename:
#     if char.isdigit():
#         numbers.append(int(char))
        
# print(int(list(filter(str.isdigit, filename)))[0])
m = re.findall(r'\d+', filename)  # 文字列から数字にマッチするものをリストとして取得
# print(m)  # ['2021', '03', '12', '15', '30']
# print(m[1]) 

# Data_out=str(filename)+"\t"+str(m[2])+"\t"+str(m[3])+"\t"+str(m[4])+"\t"+str(average_cluster_size)+"\t"+str(sum_for_hits)
# print(str(Data_out))

saved_data=np.array([xaxis_LiFneutron_1,yaxis_LiFneutron]).transpose()
# filename1= os.path.splitext(filename)[0] + '_Cluster_size.txt'

int_average_cluster_size=int(average_cluster_size)
# print(int_average_cluster_size)

# numberofneutron=np.sum(np.delete(yaxis_LiFneutron, [0,int_average_cluster_size ], axis=0))
# print(numberofneutron)
# removed=np.delete(yaxis_LiFneutron, [:int_average_cluster_size],axis=0)
# print(removed)
# conditional_sum = np.sum(np.where(yaxis_LiFneutron > (average_cluster_size+1), yaxis_LiFneutron, 0))
# print(np.where(yaxis_LiFneutron > (average_cluster_size+1), yaxis_LiFneutron, 0))
# os.path.splitext(os.path.basename())[0]
np.savetxt(f'{save_Fig_dir}/Run_{Run_number}_tot_distribution.txt', saved_data, delimiter="\t", header="Sum of TOT per cluster (Charge) [ns], Events"+", <Run: "+Run_number+", Sum of TOT per cluster (Charge) (Ave., StdDev): (" + str(average_cluster_size)+", " + str(round(std_dev,3)) +")>", fmt="%i")

# filename_2=os.path.splitext(filename)[0] + '_Cluster_size.png'
# print(Data_out)
# print(Run_number)
plt.title("Run: "+Run_number+", Sum of TOT per cluster (Ave., StdDev): (" + str(average_cluster_size)+", " + str(round(std_dev,3))+")", fontsize=10)
plt.errorbar(xaxis_LiFneutron_1, yaxis_LiFneutron, yerr=yaxis_LiFneutron**(1/2), fmt='o', label='')
# plt.vlines(average_cluster_size,yaxis_LiFneutron.min(), yaxis_LiFneutron.max(), color='b', linestyles='dotted')
plt.yscale('log')
plt.grid()
# plt.legend(loc='upper right',)
plt.xlabel("Sum of TOT per cluster (Charge) [ns]")
plt.ylabel("Events")
plt.savefig(f'{save_Fig_dir}/Run_{Run_number}_tot_distribution.png')