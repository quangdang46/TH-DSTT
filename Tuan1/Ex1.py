list_new=[1, 4, 6, 8, 22, 11, 10, 3,6]
#A tuple
new_tuple=tuple(list_new)
#b set
new_set=set(list_new)

#c dict
dict_new={i:list_new[i] for i in range(len(list_new))}