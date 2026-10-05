import json
def save_contact(c):
    with open ("contact_book.json","w")as f:
        json.dump(c,f)

def load_contact():
    try:
        with open ("contact_book.json","r")as f:
            return json.load(f)
            
    except FileNotFoundError:
        print("file not found")
        return []
    except json.JSONDecodeError:
        return []

class contact_book:
    def __init__(self,name,number,gmail):
        self.name=name
        self.number=number
        self.gmail=gmail
    def add_contact(self):
        contacts=load_contact()
        contacts.append({"name":self.name,"number":self.number,"gmail":self.gmail})
        save_contact(contacts)
        return "Contact added succesfully"

        
def vew_contacts():
    contacts=load_contact()
    return contacts

def search_contact(name):
    contacts=load_contact()
    for conatct in contacts:
        if conatct["name"]==name :
            return conatct

    return f"contact of {name} is not found"

def delete_contact(name):
    contacts=load_contact()
    newlist=[]
    for contact in contacts:
        if contact["name"]!=name :
            newlist.append(contact)
            save_contact(newlist)
            return "contact removed successfully"
            
    return f"contact of {name} is not found"

def update_contact(name,number,gmail):
    contacts=load_contact()
    for contact in contacts:
        if contact["name"]==name :

            contact["number"]=number
            contact["gmail"]=gmail 
            
            save_contact(contacts)
            return f"Contact updated successfully"

    return f"contact of {name} is not found"

def menu():
    while True:
        print("----contact manu------")
        print("1.add contact")
        print("2.vew contact")
        print("3.search contacat")
        print("4.delete contact")
        print("5.update contact")
        print("6.Exit")

        try:
            choice=int(input("Enter your choice:"))
        except ValueError:
            print("Invalid choice")
            continue

        if choice==1:
            try:
                name=input("Enter name:")
                number=input("Enter number:")
                gmail=input("Enter gmail")
                n=contact_book(name,number,gmail)
                print(n.add_contact())
            except ValueError:
                print("Enter details correctly")
        elif choice==2 :
            print(vew_contacts())
        elif choice==3 :
            try:
                nams=input("Enter name of the contact:")
                print(search_contact(nams))
            except ValueError:
                print("Invalid name")
        elif choice==4 :
            try:
                nam=input("Enter name of the contact you want to delete:")
                print(delete_contact(nam))
            except ValueError:
                print("Invalid name try again")
        elif choice==5 :
            try:
                na=input("Enter the name you want to update :")
                num=input("Enter number:")
                gm=input("Enter gmail")

                print(update_contact(na,num,gm))
            except ValueError :
                print ("Invalid name try again")
        elif choice==6 :
            print("Thank You !")
            break
        else:
            print("Invalid choice")


menu()






    
        
    