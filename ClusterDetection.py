import tkinter as tk 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN
from collections import Counter
from sklearn.preprocessing import StandardScaler
from pylab import rcParams
rcParams['figure.figsize'] = 14, 6



#Determine del clusters[0]


############## Possible parameters #####################
# ROI,Top-Level ROI
# Ion(s),Al,Rn,Mn,Fe,Cr,C,Ni,C4,C3,C2,NiH,Cu
# d-max (nm),0.6000
# Order (ions),1
# N-min (ions),10
# L (nm),0.6000
# d-erosion (nm),0.0000



#db = DBSCAN(eps = 0.12, min_samples = 10).fit(data))
# 0 = x, 1 = y, 2 = z, 3 = Da
# KNN for 27 Da line (5 in range)

############## Read CSV File with Geographical Data #################
filename = input("What is your POS-converteed CSV filepath?")
df = pd.read_csv(filename)
data = df.head(10000)

############## Show info about Database #############################
data.info()

#################### Generate Plot #############################
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#
#for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
#    xs = data["0"]
#    ys = data["1"]
#    zs = data["2"]
#    ax.scatter(xs, ys, zs, s=1, marker= 'o')
#
#ax.set_xlabel('x (nm)')
#ax.set_ylabel('y (nm)')
#ax.set_zlabel('z (nm)')
#
#plt.show()

################# Prepare DBSCAN Model ###############
#dbscan_data = data[['0', '1', '2', '3']]
dbscan_data = data[['0', '1', '2', '3']]

dbscan_data = dbscan_data.values.astype('float32', copy = False)


################# Normalize Data #######################
dbscan_data_scaler = StandardScaler().fit(dbscan_data)
dbscan_data = dbscan_data_scaler.transform(dbscan_data)

############### Construct Model ########################
model = DBSCAN(eps = 0.6, min_samples=10, metric = 'euclidean').\
    fit(dbscan_data)


################# Visualize Results ###################
outliers_df = data[model.labels_ == -1]
print(model.labels_)
clusters_df = data[model.labels_ != -1] # HERE
colors = model.labels_
colors_clusters = colors[colors != -1]
color_outliers = 'black'

clusters = Counter(model.labels_)
print(clusters)

print("Number of Clusters = {}".format(len(clusters)-1))

########### Check results with plotted figure ##########
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(clusters_df["0"], clusters_df["1"],clusters_df["2"], c = colors_clusters, edgecolors = "black", s = 50)
# ax.scatter(outliers_df["0"], clusters_df["1"],clusters_df["2"], c = color_outliers, edgecolors = "black", s = 50)
# 
# ax.set_xlabel("x (nm)")
# ax.set_ylabel("y (nm)")
# ax.set_zlabel("z (nm)")
# 
# plt.title("Cluster Detection")
# 
# plt.grid(which = "major", color = "cccccc", alpha = 0.45)
# plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for m, zlow, zhigh in [('.', -50, -25), ('^', -30, -5)]:
    xs = clusters_df["0"]
    ys = clusters_df["1"]
    zs = clusters_df["2"]
    ax.scatter(xs, ys, zs, c = colors_clusters, s = 50, marker= '.') #edgecolors = "black", 

ax.set_xlabel('x (nm)')
ax.set_ylabel('y (nm)')
ax.set_zlabel('z (nm)')

# print(clusters) 
del clusters[0]
# print(clusters)

plt.show()


