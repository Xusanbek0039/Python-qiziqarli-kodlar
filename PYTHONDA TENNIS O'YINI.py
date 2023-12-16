import time, random
p1=input("Player 1: ")
p2=input("Player 2: ")
p=p1,p2
b1,b2=0,0
def f():
 global b1,b2
 for i in p:
  time.sleep(1)
  b=random.choice(p)
  print(i,"zarba berdi⚡️ | 🏓🟦🏓")
  if b==p1:
   print(p1,"(+1) ball")
   b1+=1
  else:
   print(p2,"(+1) ball")
   b2+=1
 w=max(b1,b2)
 if b1>=11 or b2>=11:
  if w==b1:
   print(p1,"yutdi🏆")
   exit()
  elif w==b2:
   print(p2,"yutdi🏆")
   exit()
  else:
   print("Durrang")
   exit()
 f()
f()