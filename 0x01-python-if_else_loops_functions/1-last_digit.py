import random
number = random.randint(-10000, 10000)

absoluteN = abs(number)
y = absoluteN % 10

if (number < 0):
  y = -y  
if (y > 5):
    print("Last digit of" ,number,"is", y, end=" and is greater than 5")
elif (y < 6) and (y != 0):
    print("Last digit of" ,number,"is", y, end=" and is less than 6 and not 0")
elif (y == 0):
    print("Last digit of" ,number,"is", y, end=" and is 0")
