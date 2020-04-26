n = int(input())
#Factorial function
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("The factorial of " + str(n) + " is: " + str(fact))

factorial(n)
#Sum of n natural no:
def sum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    print("The sum of " + str(n) + " natural no is: " + str(sum))

sum(n)

#Fibonacci Series
def fibonacci(n):
    a=0
    b=1
    print("Print Fibonacci series: "),
    print(a,",",b, end =", "),
    for i in range(2,n+1):
        next=a+b
        print(next, end =", "),
        a=b
        b=next

fibonacci(n)

#Sum of n natural no. using recursion
def SumRec(n):
    if n==0:
        return 0
    else:
        return n + SumRec(n-1)
        

print(SumRec(n))
SumRec(n)

#Factorial using recursion
def Fact(n):
    if n == 1:
        return 1
    else:
        return n*Fact(n-1)

print(Fact(n))
Fact(n)
        


