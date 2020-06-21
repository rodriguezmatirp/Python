import re

def calsum(list):
    return sum([int(i) for i in list])

nums=[]

file=open('regex_sum_591446.txt')
for line in file:
    for word in line.split():
        y = re.findall('[0-9]+',word)
        if(len(y)>0):
            nums.extend(y)

Sum = calsum(nums)
print(Sum)

        