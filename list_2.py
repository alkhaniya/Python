arr=[1,4,55,33,88,66,50]
arr2=[]

for i in arr:
    print(i*2)
    i+=1

print("reverse")
for i in range(len(arr),0,-1):
    print(arr[i-1]*2)
    arr2.append(arr[i-1])

print("Updation")
for i in range(len(arr)):
    arr[i]*=2



print(arr2)
# print("reverse updation")
# for i in range(len(arr)):
#     arr[i]=arr[]

