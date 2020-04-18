#This is to practice lists in Python

fruits=['apple','banana','cucumber','dates']

print(len(fruits))

for i in fruits:
    print(i)

print("This is reverse using for")
for i in range(len(fruits)-1,-1,-1):
    print(fruits[i])

i=0
while i<len(fruits):
    print(fruits[i])
    i+=1
    
print("This is reverse using while")
i=len(fruits)-1
while i>=0:
    print(fruits[i])
    i-=1

