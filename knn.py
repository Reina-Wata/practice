import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#でーたの読み込みand二次元配列に
iris_data = []
f = open('iris.csv')
reader = csv.reader(f)
    
for row in reader:
    iris_data.append(row)
    
#k近傍法のアルゴリズム
def knn(k,train,test):
    ans =''
    d_sq=[]
    for i in range(150):
        d_sq.append((train[i][0]-test[0])**2+(train[i][1]-test[1])**2+(train[i][2]-test[2])**2)
    
    d = [[0 for i in range(2)] for j in range(150)]   
    for i in range(150):
        d[i][0]=d_sq[i]
        d[i][1]=train[i][4]
        
    
    d_sorted = sorted(d)
    k_ko = d_sorted[1:k+1]
    
    count_a = 0
    count_b = 0
    count_c = 0
    for i in range(k):
        if k_ko[i][1] =='setosa':
            count_a += 1
        if k_ko[i][1] =='versicolor':
            count_b += 1
        if k_ko[i][1] =='virginica':
            count_c +=1
    
    if ((count_a>=count_b) and (count_a>=count_c)):
        ans='setosa'
    if ((count_b>=count_a) and (count_b>=count_c)):
        ans = 'versicolor'
    if ((count_c>=count_a) and (count_b<=count_c)):
        ans = 'virginica'
             
    return ans

for i in range(len(iris_data)):
    iris_data[i][0] = float(iris_data[i][0])
    iris_data[i][1] = float(iris_data[i][1])
    iris_data[i][2] = float(iris_data[i][2])
    iris_data[i][3] = float(iris_data[i][3])
 

seitouritu=[]
for k in range(2,31):
    cl_label=[]
    count=0
    for i in range(150):
        a = iris_data[i]
        l = knn(k,iris_data,a)
        cl_label.append(l)
        if l==iris_data[i][4]:
            count+=1
    seitouritu.append(count/150)