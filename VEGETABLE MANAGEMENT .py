import json

# File path to save and load data
vegetable_data = "vegetable_market_data.json"

# Load data from file
def load_data():
    try:
        with open(vegetable_data, "r") as file:
            data = json.load(file)
            return (
                data.get("vegetable_name", []),
                data.get("vegetable_price", []),
                data.get("vegetable_store", []),
                data.get("bill_name", []),
                data.get("quantity", []),
                data.get("amount", []),
                data.get("total_sum", []),

            )
    except FileNotFoundError:
        return [] , [], [],  [],   [],    [],    []
        
        
# Save data to file
def save_data():
    global vegetable_name, vegetable_price, vegetable_store, bill_name, quantity, amount, total_sum
    data = {
        "vegetable_name\n": vegetable_name,
        "vegetable_price\n": vegetable_price,
        "vegetable_store": vegetable_store,
        "bill_name": bill_name,
        "quantity": quantity,
        "amount": amount,
        "total_sum": total_sum
        
    }
    with open(vegetable_data, "w") as file:
        json.dump(data, file)

# Initialize data
vegetable_name, vegetable_price, vegetable_store, bill_name, quantity, amount, total_sum = load_data()

# Admin function
def admin():
    admin_password = "122333"  # Admin password as a string
    password = input("Enter password: ")

    if password == admin_password:  # Verify admin password
        print("login successful\n")
        while True:
         print("\n--admin menu--\n"
                "1.display\n"
                "2.add vegetable\n"
                "3.delete vegetable\n"
                "4.update\n"
                "5.report\n"
                "6. exit\n")
         try:
          select=int(input("select your choice (1-6) :"))
          if select==1:
            display()
          elif select==2:
            add()
          elif select==3:
             delete_vegetable()
          elif select==4:
            update()
          elif select==5:
            report()
          elif select==6:
            break
         except ValueError:
            print("invalid number.please enter between 1 and 5.")

        
    else:
        print("Incorrect password.")
#function to add vegetable
def add():
   while True:
            adname = input("Enter vegetable name: ").lower()
            if adname in vegetable_name:  # Check if vegetable already exists
                print("Vegetable already exists.")
            else:
                try:
                    adprice = float(input("Enter price per kilogram: "))  # Include price
                    adstock = float(input("Enter stock in kilograms: "))  # Include stock
                    vegetable_name.append(adname)  # Add to vegetable name list
                    vegetable_price.append(adprice)  # Add to price list
                    vegetable_store.append(adstock)  # Add to stock list
                    save_data()  # Save data to file
                    print("Successfully added!")
                except ValueError:  #incorrect value
                    print("Invalid input for price or stock. Please try again.")
                    continue
            #if need add another vegetable
            add = input("Do you need to add another vegetable (yes or no)? ").lower()
            if add == "no":
                break
            elif add != "yes":
                print("Invalid input.")
                break
#update function
def update():
    display()   #available vegetable name,price and stock
    up_index=int(input("enter index no what do you want update : "))   #list index no related update value
    while True:
     print("-- update --\n"
          " 1.vegetable name\n"
          " 2.vegetable price\n"          #display vegetable name,price and stock
          " 3.vegetable stock\n"
          " 4.exit\n")
     try:
      up_input=int(input("what do you need update? (1-4):"))

      if 1<=up_index<=len(vegetable_name):   #check no of list
       if up_input==1:
        value=input("enter update vegetable name: ")  #give modify value
        vegetable_name[up_index-1]=value         #modify vegetable name value
       elif up_input==2:
        value=float(input("enter new price: Rs."))
        vegetable_price[up_index-1]=value
       elif up_input==3:
        value=float(input("enter new stock (kg) : "))
        vegetable_store[up_index-1]=value
       elif up_input==4:
        break
      else:
        print("invalid index")
     except ValueError:
        print("invalid number.please enter between 1 and 4.")
     save_data()
     print("successfully update!")

 #function to display vegetable   
def display():
    print("\nAvailable Vegetables:")
    for i in range (len(vegetable_name)):
        print(f"{i+1}. {vegetable_name[i]} - Price (per Kg): Rs.{vegetable_price[i]}    Stock: {vegetable_store[i]} Kg")
quantity_s=[]
amount_s=[]
bill_s=[]
# Function to create an order
def order():
    while True:
        print("\nAvailable Vegetable Names:")
        for i in range(len(vegetable_name)):
         print(f"{i + 1}. {vegetable_name[i].capitalize()}")
        if not vegetable_name:
          print("No vegetables available.")
          return
    
    
     
        index= int(input("Enter vegetable index no: "))
        if 1 <= index <= len(vegetable_name):
            print(f"You choose {vegetable_name[index-1]}")

            unit = input("Choose your measure (Kg or g): ").lower()

            try:
                weight = float(input("How much do you need? "))
                if unit == "kg":
                    required_stock = weight
                elif unit == "g":
                    required_stock = weight / 1000
                else:
                    print("Invalid measurement unit.")
                    continue

                if required_stock > vegetable_store[index-1]:
                    print("Sorry, not enough stock available.")
                    continue

                price = vegetable_price[index-1] * required_stock
                vegetable_store[index-1] -= required_stock
                quantity.append(f"{weight}{unit}")
                amount.append(price)
                bill_name.append(vegetable_name[index-1])
                quantity_s.append(f"{weight}{unit}")
                amount_s.append(price)
                bill_s.append(vegetable_name[index-1])
                save_data()
            except ValueError:
                print("Invalid weight. Please enter a numeric value.")
                continue
        else:
            print("Vegetable not found.")
            continue

        stop = input("Do you need to stop ordering? (yes or no): ").lower()
        if stop == "yes":
            break
        elif stop != "no":
            print("Invalid input. Stopping order.")
            break
  
    print("Your order was successful!")
    print("\n --bill--")
    tot=0
    if len(bill_s) == len(quantity_s) == len(amount_s):
      for i in range(len(bill_s)):
        
         print(f"{i+1}  Name: {bill_s[i]}   Quantity: {quantity_s[i]}  Price: Rs.{amount_s[i]:.2f}")
         tot=tot+amount_s[i]
        
      print(f"total bill amount is Rs.{tot}")
    else:
        print("error")
#generate report function
def report():
    tot=0
    while True:
     print("\n--vegetable report--\n"
             "1.stock report\n"
             "2.bill report\n"
             "3.exit")
     try:
        choice=int(input("enter your choice (1-3) : "))
        if choice==1:
         print("Stock Report:")
         for i in range(len(vegetable_name)):
           print(f"{i+1}  Name: {vegetable_name[i]} -   stock: {vegetable_store[i]} Kg")  
                
          
        elif choice==2:
         for i in range(len(bill_name)):
          print(f"{i+1}  Name: {bill_name[i]}   Quantity: {quantity[i]}  Price: Rs.{amount[i]:.2f}")        
          tot=tot+amount[i]
         save_data()
         print(f"total price is Rs.{tot}")
        elif choice==3:
            break
     except ValueError:
        print("invalid number.please enter between 1 and 3.")

def delete_vegetable():
 while True:
   print("\nAvailable Vegetable Names:")
   for i in range(len(vegetable_name)):
      print(f"{i + 1}. {vegetable_name[i].capitalize()}")
   if not vegetable_name:
        print("No vegetables available.")
        return
    
   else:

        try:
         v_index= int(input("Enter delete vegetable index no: "))
         if 1 <= v_index <= len(vegetable_name):
            print(f"You choose {vegetable_name[v_index-1]}")
            del(vegetable_name[v_index-1])
            del(vegetable_price[v_index-1])
            del(vegetable_store[v_index-1])
            print("delete successfully!")
            save_data()
         else:
            print("Invalid input.")
            break

         stop = input("Do you need to delete another order? (yes or no): ").lower()
         if stop == "no":
                break
         elif stop != "yes":
                print("Incorrect value.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
            break
   

#bill delete function
def delete():
    while True:
        if not bill_s:
            print("No order bills available.")
            break
        
        tot = 0
        for i in range(len(bill_s)):
            print(f"{i+1}  Name: {bill_s[i]}   Quantity: {quantity_s[i]}  Price: Rs.{amount_s[i]:.2f}")
            tot += amount_s[i]
        print(f"Total price is Rs. {tot:.2f}")

        try:
            x = int(input("Enter the bill number you want to delete: "))
            if 0 < x <= len(bill_name):
                del bill_s[x-1]
                del quantity_s[x-1]
                del amount_s[x-1]
                del bill_name[x-1]
                del quantity[x-1]
                del amount[x-1]
                print("Delete successful.")
                save_data()
            else:
                print("Invalid input.")
                break
            #if want delete again
            stop = input("Do you need to delete another order? (yes or no): ").lower()
            if stop == "no":
                break
            elif stop != "yes":
                print("Incorrect value.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
            break

# Main menu loop
check = True
while check:
    print("\n---Vegetable Market---\n"
          "1. Display Vegetables\n"
          "2. Create Order\n"
          "3. Delete Order\n"
          "4. Admin\n"
          "5. Exit")
    try:
        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
            display()
        elif choice == 2:
            order()
        elif choice == 3:
            delete()
        elif choice == 4:
            admin()
        elif choice == 5:
            print("Thank you.")
            check = False
        else:
            print("Invalid value. Please choose a number between 1 and 5.")
    #if incorrect addedvalue
    except ValueError:
        print("Invalid input.")
