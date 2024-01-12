import random, time
print("SEVGI GENERATOR")
e="⏳","❤️","💔"

def f():
	p1=input("1 ism: ")
	p2=input("2 ism: ")		
	f1=random.randint(0,100)
	f2=random.randint(0,100)
	
	for i in [10,20,30,40,50,60,70,80,90,100]:
		if i==100:
			print("100 💚")
			break
		time.sleep(1)
		print(i,e[0])
	
	if f1!=0:
		print(f"{p1} {p2} ni {f1}% yaxshi kuradi {e[1]}")
		if f2!=0:
			print(f"{p2} {p1} ni {f2}% yaxshi kuradi {e[1]}")
		else:
			print(f"{p2} {p1} ni yaxshi kurmaydi {e[2]}")
	else:
		print(f"{p1} {p2} yaxshi kurmaydi {e[2]}")
		if f2!=0:
			print(f"{p2} {p1} ni {f2}% yaxshi kuradi {e[1]}")
		else:
			print(f"{p2} {p1} ni yaxshi kurmaydi {e[2]}")
f()