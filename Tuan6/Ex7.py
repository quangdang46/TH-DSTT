import numpy as np


E= np.array([[80,98,99,85,106,94],[71,92,76,95,100,92],[124,163,140,160,176,161]])
A= np.array([[1,2,3],[2,1,2],[3,2,4]])
D=np.linalg.inv(A)@E
dict_check={4:"A",5:"B",6:"C",7:"D",8:"E",9:"F",10:"G",11:"H",12:"I",13:"J",14:"K",15:"L",16:"M",17:"N",18:"O",19:"P",20:"Q",21:"R",22:"S",23:"T",24:"U",25:"V",26:"W",27:"X",28:"Y",29:"Z",30:" "}



D=D.reshape(1,D.size)
for i in range(D.size):
    print(dict_check[int(D[0][i])],end="")

