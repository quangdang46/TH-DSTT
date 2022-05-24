import scipy.io 
import numpy as np


# print(mat['products'])
# mã                     giá                  tồn kho                 nhóm
'''
[['I1                   ' '10                   ' '5                    ''1                    ']
 ['I2                   ' '20                   ' '2                    ''3                    ']
 ['I3                   ' '20                   ' '10                   ''1                    ']
 ['I4                   ' '30                   ' '0                    ''3                    ']
 ['I5                   ' '10                   ' '10                   ''2                    ']
 ['I6                   ' '10                   ' '4                    ''2                    ']]

'''


# mã giao dịch                     các sản phẩm bán được
'''
[[array(['T100'], dtype='<U4') array(['I1', 'I2', 'I5'], dtype='<U2')]
 [array(['T200'], dtype='<U4') array(['I2', 'I4'], dtype='<U2')]
 [array(['T300'], dtype='<U4') array(['I2', 'I3'], dtype='<U2')]
 [array(['T400'], dtype='<U4') array(['I1', 'I2', 'I4'], dtype='<U2')]
 [array(['T500'], dtype='<U4') array(['I1', 'I3'], dtype='<U2')]
 [array(['T600'], dtype='<U4') array(['I2', 'I3'], dtype='<U2')]
 [array(['T700'], dtype='<U4') array(['I1', 'I3'], dtype='<U2')]
 [array(['T800'], dtype='<U4') array(['I1', 'I2', 'I3', 'I5'], dtype='<U2')]
 [array(['T900'], dtype='<U4') array(['I1', 'I2', 'I3'], dtype='<U2')]
 [array(['T1000'], dtype='<U5') array(['I1', 'I3', 'I2'], dtype='<U2')]]

'''

# Mã khách hàng                     Mã giao dịch
'''
[[array(['U1'], dtype='<U2') array(['T100', 'T400'], dtype='<U4')]        
 [array(['U2'], dtype='<U2') array(['T200', 'T300', 'T700'], dtype='<U4')]
 [array(['U3'], dtype='<U2') array(['T500 ', 'T600 ', 'T1000'], dtype='<U5')]
 [array(['U4'], dtype='<U2') array(['T800'], dtype='<U4')]
 [array(['U5'], dtype='<U2') array(['T900'], dtype='<U4')]]
'''


########## Requirements ######
def req1(transactions):    
    # ["I1","I2","I3","I4","I5","I6"]
    list_I=[]
    for element in transactions:
        for i in element[1]:
            list_I.append(i)
    list_I=list(set(list_I))
    list_I.sort()
    # Dem so lan xuat hien
    list_cnt=[0]*len(list_I)
    # [0,0,0,0,0]
    for element in transactions:
        for i in element[1]:
            list_cnt[list_I.index(i)]+=1
    # [7, 8, 7, 2, 2]
    max_value=max(list_cnt)
    min_value=min(list_cnt)
    list_max_value=[]
    list_min_value=[]
    for i in range(len(list_cnt)):
        if(list_cnt[i]==max_value):
            list_max_value.append(list_I[i])
        if(list_cnt[i]==min_value):
            list_min_value.append(list_I[i])

    return list_max_value,list_min_value


def req2(products):
    list_I=[]
    for element in products:
        list_I.append(element[0].strip())
    # sort,set
    list_cnt=[0]*len(list_I)
    for element in products:
        list_cnt[list_I.index(element[0].strip())]+=int(element[2])
    max_value=max(list_cnt)
    min_value=min(list_cnt)
    list_max_value=[]
    list_min_value=[]
    for i in range(len(list_cnt)):
        if(list_cnt[i]==max_value):
            list_max_value.append(list_I[i])
        if(list_cnt[i]==min_value):
            list_min_value.append(list_I[i])
    return list_max_value,list_min_value


def req3(transactions, products):
    # list sp dung
    # ["I1","I2","I3","I4","I5"]
    list_I=[]
    for element in transactions:
        for i in element[1]:
            list_I.append(i)
    list_I=list(set(list_I))
    list_I.sort()
    # Dem so lan xuat hien
    list_cnt=[0]*len(list_I)
    # [0,0,0,0,0]
    for element in transactions:
        for i in element[1]:
            list_cnt[list_I.index(i)]+=1
    # [7, 8, 7, 2, 2]
    # tao dict chua don gia cac mat hang trong cua hang
    dict_gia={}
    for element in products:
        dict_gia[element[0].strip()]=int(element[1])
    # list_sum=sum([dict_gia[k]*list_cnt[list_I.index(k)] for k in list_I])

    # todo
    list_sum=[]
    for k in list_I:
        list_sum.append(dict_gia[k]*list_cnt[list_I.index(k)])
    return list_sum

def req4(transactions, products):
    # list sp dung
    # ["I1","I2","I3","I4","I5"]
    list_I=[]
    for element in transactions:
        for i in element[1]:
            list_I.append(i)
    list_I=list(set(list_I))
    list_I.sort()
    # Dem so lan xuat hien
    list_cnt=[0]*len(list_I)
    # [0,0,0,0,0]
    for element in transactions:
        for i in element[1]:
            list_cnt[list_I.index(i)]+=1
    # [7, 8, 7, 2, 2]
    # tao dict chua don gia cac mat hang trong cua hang
    dict_gia={}
    for element in products:
        dict_gia[element[0].strip()]=int(element[1])
    # list chua cac doanh thu cua tung mat hang
    # list_result=[dict_gia[k]*list_cnt[list_I.index(k)] for k in list_I]
    
    
    # todo
    list_result=[]
    for k in list_I:
        list_result.append(dict_gia[k]*list_cnt[list_I.index(k)])
    max_value=max(list_result)


    # todo
    list_kq=[]
    for element in list_result:
        if(element==max_value):
            list_kq.append(list_I[list_result.index(element)])
    # list_kq=[list_I[list_result.index(element)] for element in list_result if element==max_value]

    return list_kq

def req5(history, k):
    dict_result={}
    for element in history:
        dict_result[element[0][0]]=len(element[1])
    # # ("u1":1)
    # def sz(x):
    #     return x[1]
    list_kq=sorted(dict_result.items(), key=lambda x: x[1], reverse=True)

    # todo
    list_vector=[]
    for i in range(k):
        list_vector.append(list_kq[i][0])
    # list_vector=[list_kq[i][0] for i in range(k)]
    return list_vector

def req6(transactions, history, k):
    # list sp dung
    # ["I1","I2","I3","I4","I5"]
    list_I=[]
    for element in transactions:
        for i in element[1]:
            list_I.append(i)
    list_I=list(set(list_I))
    list_I.sort()
    # tao list chua ma giao dich cua thg k
    list_id=[]
    for element in history:
        if k==element[0]:
            for i in element[1]:
                list_id.append(i)
    list_cnt=[0]*len(list_I)

    # duyet qua tung ma giao dich
    for element in list_id:
        list_tmp=[]
        for i in transactions:
            if element==i[0]:
                for sz in i[1]:
                    list_tmp.append(sz)

        for cz in list_tmp:
            list_cnt[list_I.index(cz)]+=1
    max_value=max(list_cnt)
    list_kq=[]
    for i in range(len(list_cnt)):
        if list_cnt[i]==max_value:
            list_kq.append(list_I[i])
    return list_kq
# mã giao dịch                     các sản phẩm bán được
'''
[[array(['T100'], dtype='<U4') array(['I1', 'I2', 'I5'], dtype='<U2')]
 [array(['T200'], dtype='<U4') array(['I2', 'I4'], dtype='<U2')]
 [array(['T300'], dtype='<U4') array(['I2', 'I3'], dtype='<U2')]
 [array(['T400'], dtype='<U4') array(['I1', 'I2', 'I4'], dtype='<U2')]
 [array(['T500'], dtype='<U4') array(['I1', 'I3'], dtype='<U2')]
 [array(['T600'], dtype='<U4') array(['I2', 'I3'], dtype='<U2')]
 [array(['T700'], dtype='<U4') array(['I1', 'I3'], dtype='<U2')]
 [array(['T800'], dtype='<U4') array(['I1', 'I2', 'I3', 'I5'], dtype='<U2')]
 [array(['T900'], dtype='<U4') array(['I1', 'I2', 'I3'], dtype='<U2')]
 [array(['T1000'], dtype='<U5') array(['I1', 'I3', 'I2'], dtype='<U2')]]

'''

# Mã khách hàng                     Mã giao dịch
'''
[[array(['U1'], dtype='<U2') array(['T100', 'T400'], dtype='<U4')]        
 [array(['U2'], dtype='<U2') array(['T200', 'T300', 'T700'], dtype='<U4')]
 [array(['U3'], dtype='<U2') array(['T500 ', 'T600 ', 'T1000'], dtype='<U5')]
 [array(['U4'], dtype='<U2') array(['T800'], dtype='<U4')]
 [array(['U5'], dtype='<U2') array(['T900'], dtype='<U4')]]
'''

# print(mat['products'])
# mã                     giá                  tồn kho                 nhóm
'''
[['I1                   ' '10                   ' '5                    ''1                    ']
 ['I2                   ' '20                   ' '2                    ''3                    ']
 ['I3                   ' '20                   ' '10                   ''1                    ']
 ['I4                   ' '30                   ' '0                    ''3                    ']
 ['I5                   ' '10                   ' '10                   ''2                    ']
 ['I6                   ' '10                   ' '4                    ''2                    ']]

'''


def req9(transactions, history, products):
    list_I=[]
    for element in products:
        list_I.append(element[0].strip())
    list_ban=[]
    for element in transactions:
        for i in element[1]:
            list_ban.append(i)
    list_ban=list(set(list_ban))
    list_ban.sort()
    list_result=[]
    for element in list_I:
        if element not in list_ban:
            list_result.append(element)
    return list_result

# mã giao dịch                     các sản phẩm bán được
'''
[[array(['T100'], dtype='<U4') array(['I1', 'I2', 'I5'], dtype='<U2')]
 [array(['T200'], dtype='<U4') array(['I2', 'I4'], dtype='<U2')]
 [array(['T300'], dtype='<U4') array(['I2', 'I3'], dtype='<U2')]
 [array(['T400'], dtype='<U4') array(['I1', 'I2', 'I4'], dtype='<U2')]
 [array(['T500'], dtype='<U4') array(['I1', 'I3'], dtype='<U2')]
 [array(['T600'], dtype='<U4') array(['I2', 'I3'], dtype='<U2')]
 [array(['T700'], dtype='<U4') array(['I1', 'I3'], dtype='<U2')]
 [array(['T800'], dtype='<U4') array(['I1', 'I2', 'I3', 'I5'], dtype='<U2')]
 [array(['T900'], dtype='<U4') array(['I1', 'I2', 'I3'], dtype='<U2')]
 [array(['T1000'], dtype='<U5') array(['I1', 'I3', 'I2'], dtype='<U2')]]

'''

# Mã khách hàng                     Mã giao dịch
'''
[[array(['U1'], dtype='<U2') array(['T100', 'T400'], dtype='<U4')]        
 [array(['U2'], dtype='<U2') array(['T200', 'T300', 'T700'], dtype='<U4')]
 [array(['U3'], dtype='<U2') array(['T500 ', 'T600 ', 'T1000'], dtype='<U5')]
 [array(['U4'], dtype='<U2') array(['T800'], dtype='<U4')]
 [array(['U5'], dtype='<U2') array(['T900'], dtype='<U4')]]
'''


def req7(transactions, history):
    # ["I1","I2","I3","I4","I5","I6"]
    list_I=[]
    for element in transactions:
        for i in element[1]:
            list_I.append(i)
    list_I=list(set(list_I))
    list_I.sort()
    # Dem so lan xuat hien
    list_cnt=[0]*len(list_I)

    # tim khach hang it giao dich nhat
    list_min_len=[]
    for element in history:
        list_min_len.append(len(element[1]))
    list_T=[]
    for element in history: 
        if len(element[1])==min(list_min_len):
            for i in element[1]:
                list_T.append(i)
    for element in transactions:
        if element[0] in list_T:
            for i in element[1]:
                list_cnt[list_I.index(i)]+=1
    max_value=max(list_cnt)
    list_result=[list_I[i] for i in range(len(list_I)) if list_cnt[i]==max_value]
    return list_result



def req10(history, transactions, products, k):
    list_category=[0]*4
    list_T=[]
    list_I=[]
    for element in history:
        if element[0]==k:
            for i in element[1]:
                list_T.append(i)

    for element in transactions:
        if element[0] in list_T:
            for i in element[1]:
                list_I.append(i)

    for element in list_I:
        for x in products:
            if element==x[0].strip():
                list_category[int(x[3])]+=1
    return list_category.index(max(list_category))



mat=scipy.io.loadmat('data.mat')

def req8(transactions, history, k):
    return None    
print(req5(mat['history'],3))
