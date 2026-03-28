

customers={}
unique_id=0


#id generate

def id_generate():
    global unique_id
    unique_id+=1
    return unique_id


#add customer with validation

def add_customer():
    cid = id_generate()

    # Name validation
    while True:
        name = input("Enter name: ")
        if name.replace(" ", "").isalpha():
            break
        else:
            print("Invalid name Use letters only.")

    # Email validation (@gmail.com)
    while True:
        email = input("Enter email: ")
        if email.count("@") == 1 and email.index("@") > 1 and email.endswith("@gmail.com"):
            break
        else:
            print("Invalid email(abc@gmail.com).")

    # Address validation
    while True:
     address = input("Enter address: ")
     if address.replace(" ", "").isalnum(): 
        break
    else:
        print("Invalid address! Use letters and numbers only.")

    # Phone number validation (digits only, 10 digits)
    while True:
        phone = input("Enter phone number: ")
        if phone.isdigit() and len(phone) == 10:
            break
        else:
            print("Invalid phone no.Enter 10 digit number.")

    
    customers[cid] = {
        "name": name,
        "email": email,
        "address": address,
        "phone": phone
    }

    print(f"Customer added successfully with ID: {cid}")

#show customer

def show_customer():
    cid=int(input("id: "))
    if cid in customers:
        print(f"customer id: {cid}")
        print(f"name: {customers[cid]['name']}")
        print(f"email: {customers[cid]['email']}")
        print(f"address: {customers[cid]['address']}")
        print(f"phone: {customers[cid]['phone']}")
    else:
        print("customer not found")

#show all customers

def show_all_customers():
    if not customers:
        print("No customers found")
        return

    for cid, data in customers.items():
        print(f"ID: {cid}")
        print(f"Name: {data['name']}")
        print(f"Email: {data['email']}")
        print(f"Address: {data['address']}")
        print(f"Phone: {data['phone']}")
        print("-" * 20)  



#update customer

def update_customer():
    cid = int(input("Enter customer ID: "))
    
    if cid in customers:
        
        customer = customers[cid]
        
        
        print("Leave if you not want to change a field")
        
        name = input(f"Enter name ({customer['name']}): ")
        email = input(f"Enter email ({customer['email']}): ")
        address = input(f"Enter address ({customer['address']}): ")
        phone = input(f"Enter phone ({customer['phone']}): ")
        
        # Update only if user entered something
        if name.strip() != "":
            customer["name"] = name
        if email.strip() != "":
            customer["email"] = email
        if address.strip() != "":
            customer["address"] = address
        if phone.strip() != "":
            customer["phone"] = phone
        
        print("Customer updated successfully")
        
    else:
        print("Customer not found")
        

# Delete customer

def delete_customer():
    cid=int(input("enter customer id: "))
    if cid in customers:
        del customers[cid]
        print("customer deleted successfully")
    else:
        print("customer not found")



choice=1
while choice!=6:
    print("1. add customer")
    print("2. show customer")
    print("3. show all customers")
    print("4. update customer")
    print("5. delete customer")
    print("6. exit")
    try:
     choice=int(input("enter your choice: "))
    except:
     print("invalid input enter the digits only")
     continue
    
    if choice==1:
        add_customer()
    elif choice==2:
        show_customer()
    elif choice==3:
        show_all_customers()
    elif choice==4:
        update_customer()
    elif choice==5:
        delete_customer()
    elif choice==6:
        break
    else:
        print("invalid choice")
