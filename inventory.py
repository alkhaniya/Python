vegList = {"apple":25,"banana":10,"orange":20}

cust_count = input("No of customer: ")

for customer in range(0, cust_count):
    for product in vegList:
        print(product)

    Apple_Qty = input("How many apples do you want? ")
    Banana_Qty = input("How many bananas do you want? ")
    Orange_Qty = input("How many oranges do you want? ")
    Amt = (Apple_Qty * vegList['apple']) + (Banana_Qty * vegList['banana']) + (Orange_Qty * vegList['orange'])
    print('The amount to be paid is: ' + str(Amt))

    print("Hello World")


