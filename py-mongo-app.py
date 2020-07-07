import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

database = client['pydb_local']

collection = database['employess'] 


def display_options():
    print ("1. Add a record")
    print ("2. Find a record by name")
    print ("3. Edit a record")
    print ("4. Delete a record")
    print ("5. Exit")

#display_options() just for running to see the result up to this line

    user_opt = input("Enter your option number: ")
    return user_opt

#helper function
def get_record():
    print("") # to have a space 
    name = input("Enter your first name: ")
    last = input("Enter your last name: ")

    try:
        doc = collection.find_one({'first_name':name.lower(), 'last_name':last.lower()})
    except:
        print("Error accessing the database")

    if not doc:
        print("")
        print("Error! No results found.")
   
    return doc

#adding new function to add record in db
def add_record():
    print("")
    name = input("Enter your name ")
    last = input("Enter your last name ")
    email = input("Enter your email ")
    title = input("Enter your job title ")
    salary = float(input("Enter your salary"))


    new_record = {
        "first_name" : name.lower(),
        "last_name" : last.lower(),
        "email" : email.lower(),
        "job_title" : title.lower(),
        "salary" : salary
    }

    try:
        collection.insert_one(new_record)
        print("")
        print("Document inserted")
    
     # The except block lets you handle the error.
    except:
        print("Error accessing the database")

#find function
def find_record():
    record = get_record()
    if record:
        print("")
        for key, value in record.items():
            if key != "_id":
                if (isinstance(value,str)):
                    print(key.capitalize(),":" , value.capitalize())
                else:
                    print(key.capitalize(),":", value)

 #edit function
def edit_record():
    ed = get_record()
    if ed:
        update_doc = {}
        print("")
        for key, value in ed.items():
            if key != "_id":
                update_doc[key] = input(f"{key} [{value}] :").lower()

                if update_doc[key] == "":
                    update_doc[key] = value

        try:
            collection.update_one(ed, {'$set': update_doc})
            print("")
            print("Document updated")
        except:
            print("Error")
#delete function
def delete_record():
    de = get_record()
    if de:
        print("")
        
        for key, value in de.items():
            if (isinstance(value,str)):
                print(key.capitalize(), ": ", value.capitalize())
            else:
                print(key.capitalize(), ": ", value)

        print("")
        confirm = input("Do you want to delete this document? \nY or N: ")
        print("")

        if confirm.lower() == "y":
            try:
                collection.delete_one(de)
                print("")
                print("Document deleted")
            except:
                print("Error accessing Database")
        else:
            print("Document not deleted")

def keep_asking():

    while True:
        print("**********************")
        select = display_options()
        if select == "1":
            print("You select option 1")
            add_record()

        elif select == "2":
            print("You select option 2")
            find_record()

        elif select == "3":
            print("You select option 3")
            edit_record()

        elif select == "4":
            print("You select option 4")
            delete_record()

        elif select == "5":
            client.close()
            break
        else:
            print("not a valid option try again")

#calling the function
keep_asking()

    



