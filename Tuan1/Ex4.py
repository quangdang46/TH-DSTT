S1={1,2,3,4,5,6}
S2={3,4,5,6,7}
#a giao hai tap s1 va s2
print(S1.intersection(S2))

#b hop hai tap s1 va s2
print(S1.union(S2))

#them mot gia tri x vao S2
S2.add(int(input()))

#Xoa mot gia tri trong tap s2
try:
    S2.remove(int(input()))
except:
    print("Khong co gia tri nao trong tap s2")
