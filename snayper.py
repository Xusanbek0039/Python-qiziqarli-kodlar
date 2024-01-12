import random, time

print("SNAYPER O'YINI\n")
ism=input("Ismingizni kiriting: ")
print(ism, "o'yin maydoniga xush kelibsiz")

def f():
	n=random.randint(1,1000)
	print("🔎Raqib qidirilmoqda")
	time.sleep(3)
	print(f"Player {n} ⚔ {ism}")
	print("Jang boshlandi‼️")
	x,y=100,100
	while x>0 and y>0:
		p1=random.randint(1,50)
		p2=random.randint(1,50)
		time.sleep(1)
		print(f"🤖Player {n}: 🔫({p1}) | 🛡({p2})")
		time.sleep(1)
		print(f"👤{ism}: 🔫({p2}) | 🛡({p1})")
		print(x,y)
		x-=p2
		y-=p1
	if x<y:
		print(f"🏆 {ism} yutdi")
	else:
		print(f"🏆 Player {n} yutdi")
f()
