import math

coins = ["one pence", "two pence", "five pence", "ten pence", "twenty pence", "fifty pence","one pound", "two pound"]
value = [0.01,0.02,0.05,0.1,0.2,0.5,1,2]

pound2 = ""
pound1 = ""
p50 = ""
p20 = ""
p10 = ""
p5 = ""
p2 = ""
p1 = ""

end = [pound2,pound1,p50,p20,p10,p5,p2,p1]

total = 0
index = 0
while index < 8:
    print ("How many", coins[index], " coins do you have?")
    no_coins = int(input())
        
    number = no_coins * value[index]
    total = total + number
    index = index + 1
    print (total)


total = round(total,2)
print ("Your total is £", total)

spend = int(input("How much would you like to spend?"))
if spend > total:
    print ("You do not have enough coins to spend that amount")
    left = spend - total

elif spend < total:
    total = total - spend
    total = round(total, 2)
    print ("£", spend, "has been spent")
    print ("Your now have £", total, "left")

index2 = 7
index3 = 0
count = 0
done = False

while done == False:
    while total >= 0:
        count = 0
        total = total - value[index2]
        count = count + 1
        if total <= 0:
            end[index3] = count - 1
            index3 = index3 + 1
            total = total + value[index2]

            print (total)
            print ("hello")
            index2 = index2 - 1
            print (end)

