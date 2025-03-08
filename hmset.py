sentence = input("What is your sentence?")
numbers = [0,1,2,3,4,5,6,7,8,9]
setnum = set(numbers)
print(setnum)
count = 0

for i in numbers:
    if str(i) in sentence:
        count += 1
print(count)
    
# if numbers in sentence:
#     panagram = True
#     print("its a panagram!")
# else:
#     panagram = False
#     print("its not a panagram")
    
"""numcount = {
        '0': 0,
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9':0
        
    }
    for s in sentence:
        if s in numcount:
            numcount[s] += 1
    panagram = True
    for s in numcount.values():
        if s == 0:
            panagram = False
    if panagram:
        print("It's a panagram!")
    else:
        print("It's not a panagram :(")
    print(numcount)"""
    