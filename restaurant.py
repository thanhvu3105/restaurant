num = 0

def main():

    
    
    total = 0
    count = 0
    flag = True
    while(flag):
        price = float(input("Price: "))
        if not price:
            flag = False
        count += 1
        print("Item " + str(count) + " : ",end ='')
        print(price)
        total += price
        print("Total : " + str(total))

    tax = total * 0.0825
    print("TOTAL: ",end = "")
    totalPrice = total + tax
    
    print(totalPrice)
    appendFile = open("exampleFile.txt","a")
    customer = input("Customer name: ")
    appendFile.write("Transaction " + customer + " : $" + str(totalPrice) + " \n")
    appendFile.close()

    go_on = input("Y to continue: ")
    if(go_on == "Y" or go_on == "y"):
        return main()

main()
