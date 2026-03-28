

customers={}
unique_id=0


#id generate

def id_generate():
    global unique_id
    unique_id+=1
    return unique_id


#add customer

def add_customer():
    cid=id_generate()
    name=input("enter name: ")
    email=input("enter email: ")
    city=input("enter city name: ")
    customers[cid]={
    "name":name,
    "email":email,
    "city":city
    }
    print("customer added successfully")
add_customer()


#show customer

def show_customer():
    cid=int(input("id: "))
    if cid in customers:
        print(f"customer id: {cid}")
        print(f"name: {customers[cid]['name']}")
        print(f"email: {customers[cid]['email']}")
        print(f"city: {customers[cid]['city']}")
    else:
        print("customer not found")
show_customer()


#update customer

def update_customer():
    cid=int(input("enter customer id: "))
    if cid in customers:
        name=input("enter name: ")
        email=input("enter email: ")
        city=input("enter city name: ")
        customers[cid]={"name":name,"email":email,"city":city}
        print("customer updated successfully")
    else:
        print("customer not found")
        

update_customer()
