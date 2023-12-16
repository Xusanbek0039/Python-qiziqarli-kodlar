import random,time
p1=input("Jangchi 1: ")
p2=input("Jangchi 2: ")
p=p1,p2
a,b=100,100
while (a or b)>=0:
 for i in p:
  time.sleep(2)
  x=random.randint(0,100)
  print(i,"zarba berdi🥊")
  print("⚡️Zarba kuchi:",x)
  if i==p1:
   b-=x
   print("❤️",p1,":",a)
   print("❤️",p2,":",b)
  else:
   a-=x
   print("❤️",p1,":",a)
   print("❤️",p2,":",b)
w=min(a,b)
if w==a:
 print(p2,"yutdi🏆")
else:
 print(p1,"yutdi🏆")