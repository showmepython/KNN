
from sklearn import datasets

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


iris = datasets.load_iris()

iris_data  = np.array(iris.data) 
iris_target= np.array(iris.target)[:,np.newaxis]
All_Data = np.hstack((iris_data,iris_target))




                     
def dist(a,b):
    
    res=np.array([])
    for i in range(150):
       
        res = np.append(res,np.sqrt(np.square(a[0]-b[i][0]) + np.square(a[1]-b[i][1]) + np.square(a[2]-b[i][2]) + np.square(a[3]-b[i][3])  )  )
    return res



def bubble_sort(list):
    for i in range(0,len(list)-1): 
        for j in range(0,len(list)-1-i):
            if list[j] > list[j+1]: 
                list[j],list[j+1]=list[j+1],list[j]
    return list





def Linear_Compare(D1,D2,K):
    D2_len=D2.size
    res=np.array([])
    for i in range (0,K):
        for j in range (0,D2_len):
            if(D1[i]==D2[j]):
                res = np.append(res,j)
               
    return res            




def Decide_target(Data_No,K):
    Final_Res=np.array([])
    for i in range (0,K):       
        x=int(Data_No[i])     
        Final_Res=np.append(Final_Res,All_Data[x,4])
    print(Final_Res)
    
    
    y=Final_Res.size
    t0=t1=t2=0
    for j in range (0,y):
        if(int(Final_Res[j])==0):
            t0=t0+1
        elif (int(Final_Res[j])==1):
            t1=t1+1
        elif (int(Final_Res[j])==2):
            t2=t2+1
    total=np.array([t0,t1,t2])   
    print('{0} {1}'.format("各類個數:", total))
    
   
    target=-1
    for p in range (0,3):
        if( target < total[p]):
            target=p
             
    return target    

def main():
    a=np.array([5.9,3,5.1,1.8  ])
    Dist_Oped=np.array(bubble_sort(dist(a,All_Data)))
    Data_No=Linear_Compare(Dist_Oped,dist(a,All_Data),10)
    answer=Decide_target(Data_No,10)
    print('分類為第{0:d}類'.format(answer))

if __name__ == "__main__":
  
    main()


