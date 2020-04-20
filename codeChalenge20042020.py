# This program is for the codeChallenge held on 20-04-2020

n = int(input("Enter the number: "))
print("Enter the position")

userInputPos = []
userInputStr = []

#Enter the positions
for j in range(n):    
    userInputPos.append(int(input()))

#Enter the strings
for i in range(n):
    userInputStr.append(str(input()))

for i in range(n):
    if userInputPos[i] == i+1:
        continue 
    elif len(userInputStr[i]) == userInputPos[i]:
        userInputStr[i]=userInputStr[i].upper()
        i+=1    
    else:
        userInputStr[i]=userInputStr[i].lower()

#Resulting Array
result = []
i =1

for i in range(1,n+1) :
    for j in range(n):
        if i == userInputPos[j]:
            result.append(userInputStr[j])
    i+=1

print('\n Your Answer is:')
for i in result:
    print(i)