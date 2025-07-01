contacts={"yassin":"01101181013","ahmed":"0105011123","tamer":"01003433493"}
print(contacts)
for name in contacts:
    print (name)
search=input("enter the name")
if search in contacts:
    print(f"phone number of {search} is {contacts [search]}")
