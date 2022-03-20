import numpy as np
x=np.array([3 ,11, -9, -131, -1 ,1, -11, 91, -6 ,407, -12, -11, 12, 153, 371])
# max array
print(np.max(x))

# min array
print(np.min(x))

# find x[i]>10
z=np.where(x>10)
print()

# reversed array
print(np.flip(x))

# sort array
print(np.sort(x))

#  to sort x vector in descending order
print(np.sort(x)[::-1])


cnt=0
for i in range(len(x)-1):
    for j in range(i+1,len(x)):
        if x[i]+x[j]==0:
            cnt+=1


y=[]
for i in range(len(x)):
    y.append(x[i]+x[len(x)-i-1])


# find Amstrong in x
y=[x[i] for i in range(len(x)) if x[i]>0 and x[i]==sum([int(j)**len(str(x[i])) for j in str(x[i])])]


# delete x[i]<0
print(np.delete(x,np.where(x<0)))

# find median value
print(np.median(x))

# sum of all values which are less than mean value in x
print(np.sum(x[x<np.mean(x)]))

# create a new vector which each negative value is replaced by its absolute value
print(np.abs(x))