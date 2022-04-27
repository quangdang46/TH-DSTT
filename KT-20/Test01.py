import numpy as np 


def req1(A):
	M=np.sum(A, axis=1) 
	max_value=max(M)
	list_index=[]
	for i in range(len(M)):
		if M[i]==max_value:
			list_index.append(i)
	return list_index
def req2(A):
	list_fibo=[int(np.round((((1 + np.sqrt(5)) / 2)**i/np.sqrt(5)))) for i in range(1,10000)]
	M_main=np.diag(A)
	total=np.sum([element for element in M_main if element in list_fibo])
	return total


def req3(A):
	def most_frequent(C):
		C=list(C)
		return max(set(C), key=C.count)
	M=A.reshape(1,A.shape[0]*A.shape[1])
	C=M[M%2!=0]
	x=1000
	if len(C)!=0:
		x=most_frequent(C)
	A=np.where(A<0,x,A)
	return A




# def req4(A, threshold):
# 	def count_element(A,row,col):
# 		# kiểm tra dk không hợp lệ
# 		if row<0 or col<0 or row>=len(A) or col>=len(A):
# 			return 0
# 		# kiểm tra =0 loại
# 		if A[row][col]==0:
# 			return 0
# 		# sau khi kiểm tra xong gán =0 để bỏ qua
# 		A[row][col]=0
# 		max_cnt=1
# 		# đệ qui tới các phần tử bao xung quanh
# 		for i in range(row-1,row+1+1):
# 			for j in range(col-1,col+1+1):
# 				if any([i!=row,j!=col]):
# 					max_cnt+=count_element(A,i,j)
# 		return max_cnt

# 	# solve
# 	A=np.where(A>threshold,1,0)
# 	result=0
# 	for row in range(len(A)):
# 		for col in range(len(A[0])):
# 			if A[row][col]==1:
# 				tmp=count_element(A,row,col)
# 				result=max(result,tmp)
# 	return result

def req4(A, threshold):
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
		result=max(tmp,result)
		A[row][col]=0
		count_element(A,row-1,col,tmp)
		count_element(A,row,col+1,tmp)
		count_element(A,row+1,col,tmp)
		count_element(A,row,col-1,tmp)
		A[row][col]=1


	# solve
	A=np.where(A>threshold,1,0)
	for row in range(len(A)):
		for col in range(len(A[0])):
			if A[row][col]==1:
				count_element(A,row,col,0)
	return result




A=np.array([[1,1,0,1,0,0,1,0,0,0],
			[1,1,0,1,0,0,0,1,1,1],
			[0,0,1,1,1,0,0,0,0,0],
			[0,0,1,1,1,0,0,1,1,1],
			[0,0,0,0,0,0,0,1,1,0],
			[1,1,1,1,1,1,1,0,0,0]])