from random import randint

def sort(a: list):
   for i in range(len(a)):
       for j in range(i, len(a)):
           if int(a[i]) > int(a[j]):
               a[i], a[j] = a[j], a[i]
   return a

a = []
s = 'a'
while not s in ['Y', 'N', 'y', 'n']:
   s = input("Do you want Sort?\n\nPlease enter Y or N: ")

while len(a) < 7:
   b = randint(1, 45)
   if not b in a: a.append(str(b))

if s in ["Y", "y"]:
  print(", ".join(sort(a)))

else:
  print(", ".join(a))
