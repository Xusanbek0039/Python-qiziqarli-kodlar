import random, time

c1=[]
e="Player "
player=input("Sizning ismingiz: ")
c1.append(e+player)
for i in range(3):
	n=random.randint(100,1000)
	c1.append(e+str(n))

c2=[]
e="Player "
for i in range(4):
	n=random.randint(100,1000)
	c2.append(e+str(n))

print("\n🔫TDM BOSHLANDI🏁\n")

x=0
for i in range(4):
	print("🟢"+c1[x]+" 🔴"+c2[x])
	x+=1

for i in range(-3,0):
	time.sleep(1)
	print(abs(i))
print("Match\n")

s1=0
s2=0
ps1=[[],[],[],[]]
ps2=[[],[],[],[]]
while True:
	c=c1,c2
	d=random.choice(c)
	k=random.choice(d)
	time.sleep(1)
	if k in c1:
		if s1==40 or s2==40:
			break
		t1=c1.index(k)
		ps1[t1].append(1)
		kd=random.choice(c2)
		print("😎Sizning komandangiz: 🟢"+k+" 🔫☠ 🔴"+kd)
		s1+=1
	else:
		if s1==40 or s2==40:
			break
		t2=c2.index(k)
		ps2[t2].append(1)
		kd=random.choice(c1)
		print("🥶Sizga qarshi komanda: 🔴"+k+" 🔫☠ 🟢"+kd)
		s2+=1

n1=[]
for i in ps1:
	z=sum(i)
	n1.append(z)

n2=[]
for i in ps2:
	z=sum(i)
	n2.append(z)

print("\n〽️Statistika\n")
x=0
for i in range(4):
	time.sleep(1)
	print("🟢"+c1[x]+": "+str(n1[x])+" 🔴"+c2[x]+": "+str(n2[x]))
	x+=1

if s1>s2:
	print("🏆🟢Sizning komandangiz yutdi:",s1,":",s2)
	mvp=max(n1)
	m=n1.index(mvp)
	print("\n🚀😱MVP player:",c1[m],mvp,"kills")
else:
	print("🏆🔴Sizga qarshi komanda yutdi:",s2,":",s1)
	mvp=max(n2)
	m=n2.index(mvp)
	print("\n🚀😱MVP player:",c2[m],mvp,"kills")

	
