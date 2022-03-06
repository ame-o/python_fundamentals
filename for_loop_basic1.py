# 1. Basic - Print all integers from 0 to 150.
# count = 0
# while count < 150:
#     count += 1
#         # print(count)

# #2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
# x= 5
# for x in range(5, 1000, 5):
# print(x)

#3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for y in range(1,101):
    if y%10==0:
        print("Coding Dojo")
    elif y%5==0:
        print("Coding")
    else:
        print(y)


# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

sum = 0
for z in range(0,50000):
    if z % 2 == 1:
        sum += z
print(sum)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for j in range(2018,0,-4):
    print(j)

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 2
highNum = 9
mult = 3
while lowNum < highNum:
    lowNum += 1
    if lowNum%mult ==0:
        print(lowNum)
