# Project Euler
# Problem 17

numbers = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
twenty = 6
thirty = 6
forty = 5
fifty = 5
sixty = 5
seventy = 7
eighty = 6
ninety = 6
hundred = 7

sum1 = 0
onethru19 = 0
temp = 0
sum2 = 0

for i in range(1, 10):  # Sum 1 though 9
    temp += numbers[i]

for i in range(1,20):  # 1 to 19
    onethru19 += numbers[i]

print(onethru19)

sum1 += onethru19 + twenty + twenty*9 + thirty + thirty*9 + forty + forty*9 + fifty + fifty*9 + \
       sixty + sixty*9 + seventy + seventy*9 + eighty + eighty*9 + ninety + ninety*9 + temp*8  #1 thru 99

sum2 += temp + hundred*9 + 99*(numbers[1] + hundred + 3) + sum1 + 99*(numbers[2] + hundred + 3) + sum1 + \
        99*(numbers[3] + hundred + 3) + sum1 + 99*(numbers[4] + hundred + 3) + sum1 + \
        99*(numbers[5] + hundred + 3) + sum1 + 99*(numbers[6] + hundred + 3) + sum1 + \
        99*(numbers[7] + hundred + 3) + sum1 + 99*(numbers[8] + hundred + 3) + sum1 + \
        99*(numbers[9] + hundred + 3) + sum1 + 3 + 8   #100 thru 1000
print(sum2 + sum1)

# Answer: 21124