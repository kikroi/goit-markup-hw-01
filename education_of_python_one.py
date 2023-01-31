
'''
import random
r = int(random.randrange(1, 10000000000))
t = float(random.randrange(1, 10))
print(r)
print(t)
'''

#txt = "The best things in life are free!"
#print ("Tha" in txt)



import random
rand = (random.randrange(1, 10))
txt = "you'r random number is {}" 
print (txt.format(rand))
finish = ("you win", "you lose", "try again")

c = 5
if rand > c:
  print(finish[0])
if rand < c:
  print(finish[1])
if rand == c:
  print(finish[2])
