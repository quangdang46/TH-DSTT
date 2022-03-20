dict_sohoc={2:"A",3:"B",4:"C",5:"D",6:"E",7:"F",8:"G",9:"H",10:"I",11:"J"}
def sumDigits(number):
    return 0 if number == 0 else int(number % 10) + sumDigits(int(number / 10))
# A
cnt=sumDigits(sum([sumDigits(number) for number in map(int,input().split("/"))]))
if cnt>11:
    cnt=sumDigits(cnt)
print(dict_sohoc[cnt])


# B
list_check=list(map(int,input().split("/")))
list_check[-1]=2022
# lst=sumDigits(sum([sumDigits(number) for number in list_check]))
print(dict_sohoc[sumDigits(sum([sumDigits(number) for number in list_check]))])



dict_py={
        "A":1,"J":1,"S":1,
        "B":2,"K":2,"T":2,
        "C":3,"L":3,"U":3,
        "D":4,"M":4,"V":4,
        "E":5,"N":5,"W":5,
        "F":6,"O":6,"X":6,
        "G":7,"P":7,"Y":7,
        "H":8,"Q":8,"Z":8,
        "I":9,"R":9," ":0
}


#C
list_check=[1,2,3,4,5,6,7,8,9,11,22]
name_input=input().upper()
sum_name=sum([dict_py[name_input[i]] for i in range(len(name_input))])
if sum_name  not in list_check:
    sum_name=sumDigits(sum_name)
print(sum_name)



list_vowel=["A", "Ă","Â", "E", "Ê", "I", "O", "Ô", "Ơ", "U", "Ư", "Y"]
name_check=input().upper().split()[-1]

#D
for i in range(len(name_check)):
    if name_check[i] in list_vowel:
        print(dict_py[name_check[i]])
        break
        

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
print(ans)