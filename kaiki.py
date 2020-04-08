import csv
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#でーたの読み込みand二次元配列に
auto_mpg = []
f = open('auto-mpg.csv')
reader = csv.reader(f)


for row in reader:
    auto_mpg.append(row)
    for s in range(len(row[0])):
        float(row[s])
        
mpg = [float(row[0]) for row in auto_mpg]
housepower = [float(row[3]) for row in auto_mpg] 
weight = [float(row[4]) for row in auto_mpg]

def show_data(ax, x0, x1, t):
    
    ax.plot(x0, x1, t, 'o',color = 'blue', markersize = 1,)
    ax.view_init(elev=35, azim=-75)
    
def mul_list(a,b):
    c=[]
    for s in range(len(a)):
        c.append(a[s]*b[s])
    return c

def plane(x0,x1,t):
    
    c_tx0 = np.mean(mul_list(t,x0)) - np.mean(t)*np.mean(x0)
    c_tx1 = np.mean(mul_list(t,x1)) - np.mean(t)*np.mean(x1)
    c_x0x1 = np.mean(mul_list(x0,x1)) - np.mean(x0)* np.mean(x1)
    v_x0 = np.var(x0)
    v_x1 = np.var(x1)
    w0 = (c_tx1 * c_x0x1 - v_x1 * c_tx0)/(c_x0x1**2 - v_x0 * v_x1)
    w1 = (c_tx0 * c_x0x1 - v_x0 * c_tx1)/(c_x0x1**2 - v_x0 * v_x1)
    w2 = -w0 * np.mean(x0) - w1*np.mean(x1) + np.mean(t)
    return np.array([w0,w1,w2])

def show_plane(ax,w):
    px0 = np.linspace(0,250,2)
    px1 = np.linspace(1500,5000,2)
    px0, px1 = np.meshgrid(px0,px1)
    y = w[0]*px0 + w[1]*px1 + w[2]
    ax.plot_surface(px0,px1,y,rstride = 1,cstride=1,alpha=0.3,color='blue',edgecolor='black')

plt.figure(figsize=(6,5))
ax = plt.subplot(1,1,1,projection = '3d')
W = plane(housepower,weight,mpg)
print("w0={0:.1f}, w1={1:.1f}, w2={2:.1f}".format(W[0],W[1],W[2]))
show_plane(ax,W)
show_data(ax,housepower,weight,mpg)
plt.show()