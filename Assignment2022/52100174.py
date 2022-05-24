import scipy.io 
import numpy as np


########## Requirements ######
def req1(transactions):
    dict_transactions = {}
    for i in range(len(transactions)):
        for k in (transactions[i][1]):
            if k.strip() not in dict_transactions:
                dict_transactions[k.strip()] = 1
            else:
                dict_transactions[k.strip()] +=1
        # find max value in dict_transactions
        max_value = max(dict_transactions.values())
        min_value = min(dict_transactions.values())
        # find key of max value
        list_min=[]
        list_max=[]
        for key, value in dict_transactions.items():
            if value == max_value:
                list_max.append(key)
            elif value == min_value:
                list_min.append(key)
    list_min.sort()
    list_max.sort()
    return list_max,list_min
 
def req2(products):
    list_name=[]
    list_values=[]
    list_min=[]
    list_max=[]
    for k in products:
        list_name.append(k[0].strip())
        list_values.append(int(k[2]))
    min_value=min(list_values)
    max_value=max(list_values)
    for key,value in zip(list_name,list_values):
        if value==max_value:
            list_max.append(key)
        elif value==min_value:
            list_min.append(key)
    list_min.sort()
    list_max.sort()
    return list_max,list_min

def req3(transactions, products):
    dict_transactions = {}
    dict_products = {}
    for i in range(len(transactions)):
        for k in (transactions[i][1]):
            if k not in dict_transactions:
                dict_transactions[k] = 1
            else:
                dict_transactions[k] +=1
    for k in (products):
        if k[0].strip() not in dict_products:
            dict_products[k[0].strip()] = float(k[1])
        else:
            dict_products[k[0].strip()] += float(k[1])
    '''
    {'I1': 7, 'I2': 8, 'I5': 2, 'I4': 2, 'I3': 7}
    {'I1': 10, 'I2': 20, 'I3': 20, 'I4': 30, 'I5': 10, 'I6': 10}
    '''
    total_revenue=sum([dict_transactions[key]*dict_products[key] for key in dict_transactions])
    return np.round(total_revenue,1)

def req4(transactions, products):
    dict_transactions = {}
    dict_products = {}
    for i in range(len(transactions)):
        for k in (transactions[i][1]):
            if k not in dict_transactions:
                dict_transactions[k] = 1
            else:
                dict_transactions[k] +=1
    for k in (products):
        if k[0].strip() not in dict_products:
            dict_products[k[0].strip()] = float(k[1])
        else:
            dict_products[k[0].strip()] += float(k[1])
    '''
    {'I1': 7, 'I2': 8, 'I5': 2, 'I4': 2, 'I3': 7}

    # vị trí không thay đổi
    {'I1': 10, 'I2': 20, 'I3': 20, 'I4': 30, 'I5': 10, 'I6': 10}
    '''
    list_total=[dict_transactions[key]*dict_products[key] for key in dict_transactions]
    max_value=max(list_total)
    list_result=[]
    for key,value in zip(dict_transactions,list_total):
        if value==max_value:
            list_result.append(key)
    return list_result
            


def req5(history, k):
    dict_check={}
    list_result=[]

    if k<=0 or k>len(history):
        return list_result

    for element in history:
        if element[0][0] not in dict_check:
            dict_check[element[0][0]]=len(element[1])
        else:
            dict_check[element[0][0]]+=len(element[1])
    dict_check = sorted(dict_check.items(), key=lambda kv: kv[1], reverse=True)
    # đã chuyển đổi sang dạng list
    for i in range(k):
        list_result.append(dict_check[i][0])
    return list_result

def req6(transactions, history, k):
    check_tmp=False
    tmp=[]

    for element in history:
        if element[0][0].strip()==k:
            check_tmp=True
            for i in element[1]:
                tmp.append(i.strip())

    if check_tmp==False:
        return []

    dict_cnt={}
    for element in tmp:
        for v in transactions:
            if element==v[0][0].strip():
                for x in v[1]:
                    if x not in dict_cnt:
                        dict_cnt[x]=1
                    else:
                        dict_cnt[x]+=1
    max_value=max(dict_cnt.values())
    list_result=[]
    for k,v in dict_cnt.items():
        if v==max_value:
            list_result.append(k)
    return list_result


def req7(transactions, history):
    list_len=[]
    list_tmp=[]
    # it giao dich nhat
    for element in history:
        list_len.append(len(element[1]))
    min_buy=min(list_len)
    for element in history:
        if len(element[1])==min_buy:
            for sz in element[1]:
                list_tmp.append(sz)
    # mua it nhat
    dict_tmp={}
    list_cnt_gd=[]
    for element in transactions:
        if element[0][0] in list_tmp:
            for i in element[1]:
                list_cnt_gd.append(i)
    for element in list_cnt_gd:
        if element not in dict_tmp:
            dict_tmp[element]=1
        else:
            dict_tmp[element]+=1
    max_value=max(dict_tmp.values())
    list_result=[k for k,v in dict_tmp.items() if v==max_value]
    return list_result





    
def req9(transactions, history,products):
    set_check=[]
    set_tmp=[]
    for element in products:
       set_check.append(element[0].strip())
    for element in transactions:
        for sz in element[1]:
            set_tmp.append(sz.strip())
    list_result=list(set(set_check)-set(set_tmp))
    list_result.sort()
    return list_result


def req8(transactions, history, k):
    # def cosine_similarity(u,v):
    #     try:
    #         return np.sum(u*v)/(np.linalg.norm(u)*np.linalg.norm(v))
    #     except:
    #         return 0
    def cosine_similarity(v1,v2):
        sumxx, sumxy, sumyy = 0, 0, 0
        for i in range(len(v1)):
            x = v1[i]; y = v2[i]
            sumxx += x*x
            sumyy += y*y
            sumxy += x*y
        if sumxx == 0 or sumyy == 0:
            return 0
        return sumxy/np.sqrt(sumxx*sumyy)
    list_U=[]
    for element in history:
        list_U.append(element[0][0])
    
    if k not in list_U:
        return []



    # List I
    list_tmp=[]
    for element in transactions:
        for i in element[1]:
            list_tmp.append(i)   
    list_tmp=list(set(list_tmp))
    list_tmp.sort()
    # ["I1", "I2", "I3", "I4", "I5", "I6"]
    # np array list k
    list_buy_k=[]
    for element in history:
        if element[0][0]==k:
            for i in element[1]:
                list_buy_k.append(i) 
    # list chứa mã hàng mà k đã đặt
    # tạo dictionary k
    # tạo def truyền vào 1 cai list mã giao dich
    def solve(list_k):
        dict_k={}
        for element in list_k:
            list_new=[]
            for sz in transactions:
                if element == sz[0][0]:
                    for i in sz[1]:
                        list_new.append(i)
            # list new sẽ chứa các ma hàng đã mua
            # tạo dict chứ số lượng các mặt hàng đã mua
            for i in list_tmp:
                if i not in list_new:
                    dict_k[i]=0
                else:
                    if i not in dict_k:
                        dict_k[i]=1
                    else:
                        dict_k[i]+=1
        return list(dict_k.values())


    # vK=np.array(solve(list_buy_k))
    vK=solve(list_buy_k)
    v=[]
    for element in history:
        list_kz=[]
        for i in element[1]:
            list_kz.append(i.strip())
        v.append(solve(list_kz))
    # v=np.array(v)

    # TODO:cần tìm ra vị trí của k truyền vào,để loại bỏ độ chính xác
    
    # NOTE
    global idx_k
    #NOTE 
    list_name=[element[0][0].strip() for element in history]
    for i in range(len(list_name)):
        if k==list_name[i]:
            idx_k=i
            break

    # kiểm tra độ chính xác từ v và vK
    #TODO
    list_cosin=[0]*len(v)
    for i in range(len(v)):
        if i==idx_k:
            list_cosin[i]=0
        else:
            list_cosin[i]=cosine_similarity(v[i],vK)
    max_cosin=max(list_cosin)
    list_result=[list_name[i] for i in range(len(list_cosin)) if list_cosin[i]==max_cosin]
    list_result.sort()
    if sum(list_cosin)!=0:
        return list_result
    # TODO:trả ra vector
    return []


def req10(history, transactions, products, k):
    list_U=[]
    for element in history:
        list_U.append(element[0][0])
    
    if k not in list_U:
        return None



    # dict chua cap do
    dict_category={}
    for element in products:
        dict_category[element[0].strip()]=int(element[3])


    # 
    list_tmp= []
    for element in history:
        if element[0][0].strip()==k:
            for i in element[1]:
                list_tmp.append(i.strip())
    

    
    # lay cac san pham ban
    list_I=[]
    for element in transactions:
        if element[0][0].strip() in list_tmp:
            for i in element[1]:
                list_I.append(i.strip())
    if len(list_I)==0:
        return None

    max_category=max(dict_category.values())
    list_cnt=[0]*(max_category+1)
    
    for element in list_I:
        list_cnt[dict_category[element]]+=1
    
    max_value_buy=max(list_cnt)
    max_index_buy=list_cnt.index(max_value_buy)
    return max_index_buy
