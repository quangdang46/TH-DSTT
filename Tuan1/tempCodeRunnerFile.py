name_check=input().upper().split()[-1]

#E
global index
for i in range(len(name_check)):
    if name_check[i] in list_vowel:
        index=i
        break
list_ip=[]
for i in range(len(name_check)):
    if i==index:
        continue
    else:
        if name_check[i]=="Y":
            list_ip.append(dict_py["I"])
        else:
            list_ip.append(dict_py[name_check[i]])
ans=sumDigits(sum(list_ip))
if ans>11:
    ans=sumDigits(ans)
print(dict_sohoc[ans])