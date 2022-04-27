import numpy as np 
def req1(A):
	M=np.sum(A, axis=1) 
	list_index=[i for i in range(len(M)) if M[i]==min(M)]
	return list_index
	
def req2(A):
    def prime(n):
        if n<2:
            return False
        return all([(n % j) for j in range(2, int(n**0.5)+1)])
    list_result=[A[i][i] for i in range(len(A)) if prime(A[i][i])]
    if len(list_result)==0:
        return None
    return min(list_result)

def req3(A):
	list_fibo=[int(np.round((((1 + np.sqrt(5)) / 2)**i/np.sqrt(5)))) for i in range(1,1000)]
	list_sum=[]
	for i in range(len(A)):
		tmp=[]
		for j in range(len(A)):
			if A[i][j] in list_fibo:
				tmp.append(A[i][j])
		list_sum.append(max(tmp))
	x=1000
	if len(list_sum)!=0:
		x=sum(list_sum)
	A=np.where(A>0,x,A)
	return A

def req4(A, threshold):
	if len(A[A<0])!=0:
		result=1
	else:
		result=0
	def count_element(A,row,col,tmp):
		nonlocal result
		# kiểm tra dk không hợp lệ
		if row<0 or col<0 or row>=len(A) or col>=len(A):
			return 0
		# kiểm tra =0 loại
		if A[row][col]==0:
			return 0
		tmp+=1
		result=min(tmp,result)
		A[row][col]=0
		count_element(A,row-1,col,tmp)
		count_element(A,row,col+1,tmp)
		count_element(A,row+1,col,tmp)
		count_element(A,row,col-1,tmp)
		A[row][col]=1


	# solve
	A=np.where(A<threshold,1,0)
	for row in range(len(A)):
		for col in range(len(A[0])):
			if A[row][col]==1:
				count_element(A,row,col,0)
	return result

