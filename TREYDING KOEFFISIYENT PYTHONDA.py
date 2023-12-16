import time, random
k=0
koef=[]
while k<=10:
 k+=0.01
 koef.append(k)
while True:
 time.sleep(0.5)
 t_p="🔺","🔻"
 a_koef=random.choice(koef)
 asosiy=random.choice(t_p)
 if asosiy==t_p[0]:
  print(t_p[0],a_koef)
 else:
  print(t_p[1],-a_koef)