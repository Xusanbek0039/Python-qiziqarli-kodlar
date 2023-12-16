from turtle import*
bgcolor("black")
speed(0)
pensize(5)
for i in range(1000):
 for c in "red","green","orange":
  color(c)
  circle(i+18)
  forward(i+7)
  right(i+10)