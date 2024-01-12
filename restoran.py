menyu = {"chuchvara": 15000,
"mastava": 16000,
"manpar": 16000,
"shurva": 18000,
"norin": 16000,
"osh": 20000,
"qozon kobob": 40000,
"halim": 22000,
"dulma": 28000}

for taom in menyu:
	print(f"{taom}: {menyu.get(taom)} sum")
	
taom=input("Nima yemoqchisiz: ")
print(f"Yegan narsangiz: {taom}\nHisob: {menyu.get(taom)} sum")