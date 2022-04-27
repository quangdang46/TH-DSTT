import numpy as np 
def req1(A):
	M=np.sum(A, axis=0) 
	list_index=[i for i in range(len(M)) if M[i]==min(M)]
	return list_index
def req2(A):
	list_fibo=[int(np.round((((1 + np.sqrt(5)) / 2)**i/np.sqrt(5)))) for i in range(1,1000)]
	list_result=[A[i][i] for i in range(len(A)) if A[i][i] in list_fibo]
	if len(list_result)==0:
		return None
	return max(list_result)

def req3(A):
	'''
	def most_frequent(List):
		dict = {}
	count, itm = 0, ''
	for item in reversed(List):
		dict[item] = dict.get(item, 0) + 1
		if dict[item] >= count :
			count, itm = dict[item], item
	return(itm)
	'''
	'''
	def most_frequent(List):
        counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
	'''
	def prime(n):
		if n<2:
			return False
		return all([(n % j) for j in range(2, int(n**0.5)+1)])
	C=[A[i][j] for i in range(len(A)) for j in range(len(A)) if prime(A[i][j])]
	x=1000
	if len(C)!=0:
		x=max(set(C), key=C.count)
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
	print(A)
	for row in range(len(A)):
		for col in range(len(A[0])):
			if A[row][col]==1:
				count_element(A,row,col,0)
	return result



A=np.array([[1,3,4,5],
			[2,2,4,3],
			[-1,1,3,-6],
			[0,-4,-3,5]])
print(req4(A,2))