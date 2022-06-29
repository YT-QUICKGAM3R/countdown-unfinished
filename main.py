
import random
import os
import time

x = 0

import loading

number = random.randint(100,999)

numbers = []

while x <= 5:
  os.system('clear')
  print("The number you have to make is " +str(number))
  choice = input("Choose a big or small number\nB for big and S for small: ")

  big = random.randint(10, 99)
  small = random.randint(1, 9)

  time.sleep(1)

  os.system('clear')
  
  if choice == 'B' or choice == 'b':
    print("You chose a big number:\nYour number is: "+str(big))
    numbers.append(big)
    time.sleep(1)
    if input:
      os.system('clear')
      print("The numbers you have chosen so far are:")
      print(*numbers, sep=", ")
      time.sleep(1)

  elif choice == 'S' or choice == 's':
    print("You chose a small number:\nYour number is: "+str(small))
    x=x+1
    numbers.append(small)
    time.sleep(1)
    if input:
      os.system('clear')
      print("The numbers you have chosen so far are:")
      print(*numbers, sep=", ")
      time.sleep(1)
  x=x+1

os.system('clear')
print("Lets play")
os.system('clear')
print("You have 30 seconds to make "+int(number)+" from these "+int(numbers)+" numbers!\nGood Luck and have fun!")
x=0
