#sepal length in cm
#   2. sepal width in cm
#   3. petal length in cm
#   4. petal width in cm
#   5. class: 
#      -- Iris Setosa
#      -- Iris Versicolour
#      -- Iris Virginica
      
import numpy as np
import statistics
import matplotlib.pyplot as plt
from scipy import stats
f=open("Iris.txt","r")
a=f.readlines()
b=[]
sepal_width=[]
petal_width=[]
sepal_length=[]
petal_length=[]
classs=[]
for i in range(len(a)):
    b.append(list(a[i].split(',')))
for i in range(len(b)):
    sepal_length.append(float(b[i][0]))
    sepal_width.append(float(b[i][1]))
    petal_length.append(float(b[i][2]))
    petal_width.append(float(b[i][3]))
    classs.append(b[i][4].strip('\n'))

print("Mean sepal length=",np.mean(sepal_length))

print("Mean petal length=",np.mean(petal_length))

print("Mean sepal width=",np.mean(sepal_width))

print("Mean petal width=",np.mean(petal_width))   

print("Median sepal length=",np.median(sepal_length))

print("Median petal length=",np.median(petal_length))

print("Median sepal width=",np.median(sepal_width))

print("Median petal width=",np.median(petal_width))    


print("Mode sepal length=",stats.mode(sepal_length))

print("Mode petal length=",stats.mode(petal_length))

print("Mode sepal width=",stats.mode(sepal_width))

print("Mode petal width=",stats.mode(petal_width))


print("Standard Dev sepal length=",np.std(sepal_length))

print("SD petal length=",np.std(petal_length))

print("SD sepal width=",np.std(sepal_width))

print("SD petal width=",np.std(petal_width))


print("Variance of sepal length=",np.var(sepal_length))

print("Variance of petal length=",np.var(petal_length))

print("Variance of sepal width=",np.var(sepal_width))

print("Variance of petal width=",np.var(petal_width))


print("Min sepal length=",min(sepal_length))

print("Min petal length=",min(petal_length))

print("Min sepal width=",min(sepal_width))

print("Min petal width=",min(petal_width))            

print("Max sepal length=",max(sepal_length))

print("Max petal length=",max(petal_length))

print("Max sepal width=",max(sepal_width))

print("Max petal width=",max(petal_width))            
setosa_SL=[]
virginica_SL=[]
versicolor_SL=[]
setosa_PL=[]
virginica_PL=[]
versicolor_PL=[]
setosa_SW=[]
virginica_SW=[]
versicolor_SW=[]
setosa_PW=[]
virginica_PW=[]
versicolor_PW=[]
y=[]
for i in range(len(b)):
    if(classs[i]=='Iris-setosa'):
        setosa_SL.append(sepal_length[i])
        setosa_PL.append(petal_length[i])
        setosa_PW.append(petal_width[i])
        setosa_SW.append(sepal_width[i])
        y.append(0)
    if(classs[i]=='Iris-virginica'):
        virginica_SL.append(sepal_length[i])
        virginica_PL.append(petal_length[i])
        virginica_PW.append(petal_width[i])
        virginica_SW.append(sepal_width[i])
        y.append(1)
    if(classs[i]=='Iris-versicolor'):
        versicolor_SL.append(sepal_length[i])
        versicolor_PL.append(petal_length[i])
        versicolor_PW.append(petal_width[i])
        versicolor_SW.append(sepal_width[i])
        y.append(2)
#labels=( 'Iris Setosa','Iris Versicolour','Iris Virginica')
#labels1=np.arange(len(sepal_length))
#xx=np.arange(len(labels))
#plt.plot(setosa_SL,'r')
#plt.plot(virginica_SL,'b')
#plt.plot(versicolor_SL,'y')
#
#plt.xlabel("frequency")
#plt.ylabel("Sepal_Length")
#plt.legend(labels)
#plt.figure()
#
#plt.plot(setosa_PL,'r')
#plt.plot(virginica_PL,'b')
#plt.plot(versicolor_PL,'y')
#
#plt.xlabel("frequency")
#plt.ylabel("Petal_Length")
#plt.legend(labels)
#plt.figure()
#
#
#plt.plot(setosa_SW,'r')
#plt.plot(virginica_SW,'b')
#plt.plot(versicolor_SW,'y')
#
#plt.xlabel("frequency")
#plt.ylabel("Sepal_Width")
#plt.legend(labels)
#plt.figure()
#
#plt.plot(setosa_PW,'r')
#plt.plot(virginica_PW,'b')
#plt.plot(versicolor_PW,'y')
#plt.xlabel("frequency")
#plt.ylabel("Petal_width")
#plt.legend(labels)


n=150
x=[[1 for i in range(n)],sepal_length,sepal_width,petal_length,petal_width]
x=np.transpose(x)
print(x)
xt=np.transpose(x)
a=np.matmul(xt,x)
b=np.linalg.inv(a)
c=np.matmul(xt,y)
beeta=np.matmul(b,c)
print('Beta=',beeta)
b0=beeta[0]
b1=beeta[1]
b2=beeta[2]
b3=beeta[3]
b4=beeta[4]
#y_pred =[ int(b0 + b1*sepal_length[i] +b2*sepal_width[i] +b3*petal_length[i] +b4*petal_width[i]) for i in range(n)]
#print((y_pred))
#plt.plot(y_pred,'b')
#plt.plot(y,'g')

y_pred=b0+b1*7.7+b2*3.0+b3*6.1+b4*2.3
print(y_pred)
