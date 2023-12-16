import random, time
e="🟩","🟥"
while True:
 r=random.choice(e)
 n=random.randint(1,48)
 time.sleep(1)
 print(r*n)