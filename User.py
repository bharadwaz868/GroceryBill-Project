import Product

item_prices = []
while(True):
    print("Would You like to Shopping ")
    inp1 = str(input("Enter Y or N : "))
    if (inp1=="Y"):
        print("Category-1-MilkProducts")
        print("Category-2-Fruits")
        print("Category-3-Vegetables ")
        print(" ")
        print("Please select a Category[1,2,3]")
        inp = int(input("Enter the Category : "))
        if (inp == 1):
            print("Item_Name : ", Product.Item_Name)
            print("Item_Number : ", Product.Item_Number)
            print("Item_Price : ", Product.Price)
            print("Item_Stock : ", Product.Stock)
            item = int(input("Enter the item number : "))
            quant = float(input("Enter the quantity : "))
            def Milk_Products():
                if item in Product.Item_Number:
                       item_index = Product.Item_Number.index(item)
                       if quant <= Product.Stock[item_index]:
                           item_prices.append(float(quant * Product.Price2[item_index]))
                           print(f"{float(quant * Product.Price2[item_index])} INR")
                           Product.Stock[item_index] = Product.Stock2[item_index] - quant
                           print(f"{Product.Stock2[item_index]} LEFT")
                       else:
                           print("No Stock")
                           print(f"{Product.Stock2[item_index]} LEFT")
                else:
                    print("INAVALID INPUT")
            Milk_Products()
            while (True):
                print("Do you Want to add more items")
                A = str(input("Enter Y or N : "))
                if (A == "Y"):
                    item = int(input("Enter the item number : "))
                    quant = float(input("Enter the quantity : "))
                    Milk_Products()
                    continue
                else:
                    break
        elif (inp == 2):
            print("Item_Name : ", Product.Item_Name2)
            print("Item_Number : ", Product.Item_Number2)
            print("Item_Price : ", Product.Price2)
            print("Item_Stock : ", Product.Stock2)
            item = int(input("Enter the item number : "))
            quant = float(input("Enter the quantity : "))
            def Fruits():
                if item in Product.Item_Number2:
                       item_index = Product.Item_Number2.index(item)
                       if quant <= Product.Stock2[item_index]:
                           item_prices.append(float(quant * Product.Price2[item_index]))
                           print(f"{float(quant * Product.Price2[item_index])} INR")
                           Product.Stock[item_index] = Product.Stock2[item_index] - quant
                           print(f"{Product.Stock2[item_index]} LEFT")
                       else:
                           print("No Stock")
                           print(f"{Product.Stock2[item_index]} LEFT")
                else:
                    print("INAVALID INPUT")
            Fruits()
            while (True):
                print("Do you Want to add more items")
                A = str(input("Enter Y or N : "))
                if (A == "Y"):
                    item = int(input("Enter the item number : "))
                    quant = float(input("Enter the quantity : "))
                    Fruits()
                    continue
                else:
                    break

        elif (inp == 3):
            print("Item_Name : ", Product.Item_Name3)
            print("Item_Number : ", Product.Item_Number3)
            print("Item_Price : ", Product.Price3)
            print("Item_Stock : ", Product.Stock)
            item = int(input("Enter the item number : "))
            quant = float(input("Enter the quantity : "))
            def Vegetables():
                if item in Product.Item_Number3:
                       item_index = Product.Item_Number3.index(item)
                       if quant <= Product.Stock3[item_index]:
                           item_prices.append(float(quant * Product.Price3[item_index]))
                           print(f"{float(quant * Product.Price3[item_index])} INR")
                           Product.Stock[item_index] = Product.Stock3[item_index] - quant
                           print(f"{Product.Stock3[item_index]} LEFT")
                       else:
                           print("No Stock")
                           print(f"{Product.Stock3[item_index]} LEFT")
                else:
                    print("INAVALID INPUT")
            Vegetables()
            while (True):
                print("Do you Want to add more items")
                A = str(input("Enter Y or N : "))
                if (A == "Y"):
                    item = int(input("Enter the item number : "))
                    quant = float(input("Enter the quantity : "))
                    Vegetables()
                    continue
                else:
                    break

    elif(inp1=="N"):
        break

total = 0
for x in range(0, len(item_prices)):
        total = total + item_prices[x]
print("Prices Of Purchased Products",item_prices)
print("Total Bill Amount",total,"INR")












