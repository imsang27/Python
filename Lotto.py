import random

print("Do you want to Sort?\n")
Y = 'Y', 'y'
N = 'N', 'n'
YN = input("Please enter Y or N.\n\n")
Lotto = []


if YN == Y :
  while len(Lotto) < 7 :
    num = random.randint(1, 46)
    print(sorted(num))


elif YN == N :
  while len(Lotto) < 7 :
    num = random.randint(1, 46)
    print(num)

if YN != Y or N :
  print('Please enter Y or N only.')
 
