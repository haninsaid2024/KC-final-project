import random
number = random.randrange(1,100)
guess= int(input('try to guess number'))
while guess != number:
  if guess > number:
     print("\n inter lower number , try again")
     guess = int(input("try to guess number"))
else:
     print("\n inter higher number , try again")
     guess = int(input("try to guess number"))
print("congratulation you do it")