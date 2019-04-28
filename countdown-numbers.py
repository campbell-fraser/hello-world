import random
import time
bigNumbers = [100,75,50,25]
smallNumbers = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
smalltime = False
while smalltime == False:
    big = int(input("How many big numbers would you like? "))
    if big > 4:
        print("Please pick a number between 1 and 4.")
    else:
        numLeft = 6-big
        smalltime = True
numberstime = False
while numberstime == False:
    small = int(input("How many small numbers would you like? You can pick "+str(numLeft)+". "))
    if small > numLeft:
        print("Please pick a number between 1 and "+str(numLeft)+".")
    else:
        numberstime = True
        
selection = []
num = 0
for i in range(0,big):
    bigLength = len(bigNumbers)
    i = random.randint(0,(bigLength-1))
    bigNumber = bigNumbers[i]
    selection.insert(num,bigNumber)
    numberSelected = bigNumbers[i]
    bigNumbers.remove(numberSelected)
    num = num+1
for i in range(0,small):
    smallLength = len(smallNumbers)
    i = random.randint(0,(smallLength-1))
    smallNumber = smallNumbers[i]
    selection.insert(num,smallNumber)
    numberSelected = smallNumbers[i]
    smallNumbers.remove(numberSelected)
    num = num+1
print("Here is your selection: "+str(selection))

operations = [1,2,3,4]
#1 +
#2 -
#3 *
#4 /

num1 = selection[random.randint(0,5)]
selection.remove(num1)
num2 = selection[random.randint(0,4)]
selection.remove(num2)

operation = operations[random.randint(0,3)]
f = open("answer.txt",'w')
if operation == 1:
    ans = num1 + num2
    f.write("("+str(num1)+"+"+str(num2)+")")
if operation == 2:
    ans = num1 - num2
    f.write("("+str(num1)+"-"+str(num2)+")")
if operation == 3:
    ans = num1 * num2
    f.write("("+str(num1)+"*"+str(num2)+")")
if operation == 4:
    ans = num1 / num2
    f.write("("+str(num1)+"/"+str(num2)+")")
f.close()

while len(selection) != 0:
    if len(selection) <= 3:
        break
    num = selection[random.randint(0,(len(selection)-1))]
    selection.remove(num)
    operation = operations[random.randint(0,3)]
    f = open("answer.txt",'a')
    if operation == 1:
        ans = ans + num
        f.write("+"+str(num)+")")
    if operation == 2:
        ans = ans - num
        f.write("-"+str(num)+")")
    if operation == 3:
        ans = ans * num
        f.write("*"+str(num)+")")
    if operation == 4:
        ans = ans / num
        f.write("/"+str(num)+")")
    f.close()
    
goal = ans
print("And the number to get to is... "+str(goal))

ready = input("Press enter to start")

countdown = 30
while countdown > 5:
    if countdown == 30:
        print("30 seconds left.")
    if countdown == 20:
        print("20 seconds left.")
    if countdown == 10:
        print("10 seconds left.")
    time.sleep(1)
    countdown = countdown - 1
while countdown > 0:
    print(countdown)
    time.sleep(1)
    countdown = countdown - 1
playerAns = int(input("Time's up! What did you get? "))

if goal == playerAns:
    print("Wow! That's spot on- 10 points!")
elif (goal - playerAns) < 5:
    print("Congratulations! You get 7 points.")
elif (goal - playerAns) < 10:
    print("Congratulations! You get 5 points.")
if (goal - playerAns) < 10:
    showAns = input("Would you like to see how it's done? ")
    showAns = showAns.lower()
    if showAns == "yes" or showAns == "y":
        f = open("answer.txt",'r')
        print(f.read())
        f.close()
