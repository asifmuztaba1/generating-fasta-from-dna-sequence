import numpy as np
with open("temp.fasta", "r") as f:
    data=f.read()
res=[int(i) for i in data.split()]
sum1=0.00
#li=[-2,-3,7,-2,-5,-3,-4,-2,4,-6,-6,-3,-1,-4,-5,3,-2,-7,-3,-4]
#li=[3 , -4  ,-3 , -4 , -3  ,-3 , -3 , -3  ,-4  ,-2  ,-3 , -3 , -3,  -4,  -4  , 2  , 3 , -5 , -4 ,  4 ]
counter=0
i=1
result=[]
for l in res:
    sig=1/(1+2.718281828459045**l)
    sum1=sum1+(sig*np.log(sig))
    counter=counter+1
    if(counter==20):
        re = 1 / (1 + 2.718281828459045 ** sum1)
        result.append(re)
        counter=0
        sum1=0.00
        i=i+1
print(len(result))
print(result)