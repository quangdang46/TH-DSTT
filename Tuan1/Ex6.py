dict_val={"km":1000,"m":1,"cm":0.01,"mm":0.001}
val=input().split();
ans=float(val[0])*dict_val[val[1]]
print(f"{val[0]} {val[1]} = {ans} m")