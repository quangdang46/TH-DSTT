import numpy as np
E= np.array([[80,98,99,85,106,94],[71,92,76,95,100,92],[124,163,140,160,176,161]])
A= np.array([[1,2,3],[2,1,2],[3,2,4]])
D=np.linalg.inv(A)@E
LT=[chr(i) for i in range(ord('A'),ord('Z')+1)]
LT.append(' ')
shift=3
'''
[[18. 21. 12. 30. 24. 23.] 
 [19.  4. 18.  5.  8.  4.] 
 [ 8. 23. 17. 15. 22. 21.]]
'''
dict_LT=dict(zip(range(1+shift,len(LT)+1+shift),LT))
D=D.reshape(1,D.size)
text=''
for i in range(D.size):
    try:
        text+=dict_LT[int(D[0][i])]
    except:
        pass
print(text)



