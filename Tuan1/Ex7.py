day,month=map(int,input().split("/"))
if(day>=21 and day<= 31 and month==3):
  print("Aries(Ram)")
elif(day>=1 and day<= 19 and month==4):
  print("Aries(Ram)")
elif(day>=20 and day<= 30 and month==4):
  print("Taurus(Bull)")
elif(day>=1 and day<= 20 and month==5):
  print("Taurus(Bull)")
elif(day>=21 and day<= 31 and month==5):
  print("Gemini(Twins)")
elif(day>=1 and day<=21 and month==6):
  print("Gemini(Twins)")
elif(day>=22 and day<= 30 and month==6):
  print("Cancer(Crab)")
elif(day>=1 and day<= 22 and month==7):
  print("Cancer(Crab)")
elif(day>=23 and day<= 31 and month==7):
  print("(Lion) ")
elif(day>=1 and day<= 22 and month==8):
  print("(Lion) ")
elif(day>=23 and day<= 31 and month==8):
  print("(Virgin) ")
elif(day>=1 and day<= 22 and month==9):
  print("Virgo (Virgin) ")
elif(day>=23 and day<= 30 and month==9):
  print("Libra (Balance)")
elif(day>=1 and day<= 23 and month==10):
  print("Libra (Balance)")
elif(day>=24 and day<= 31 and month==10):
  print("Scorpius (Scorpion)")
elif(day>=1 and day<= 21 and month==11):
  print("Scorpius (Scorpion)")
elif(day>=22 and day<= 30 and month==11):
  print("Sagittarius (Archer)")
elif(day>=1 and day<= 21 and month==12):
  print("Sagittarius (Archer)")
elif(day>=22 and day<= 31 and month==12):
  print("Capricornus (Goat)")
elif(day>=1 and day<= 19 and month==1):
  print("Capricornus (Goat)")
elif(day>=20 and day<= 31 and month==1):
  print("Aquarius (Water Bearer)")
elif(day>=1 and day<= 18 and month==2):
  print("Aquarius (Water Bearer)")
elif(day>=19 and day<= 29 and month==2):
  print("Pisces (Fish)")
elif(day>=1 and day<= 20 and month==3):
  print("Pisces (Fish)")
else:
  print("ngay sinh khong ton tai")
