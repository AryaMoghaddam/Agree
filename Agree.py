# agree.py
Boolean function to get a bool response for any field
c = input("Do you agree?")

if c.lower () in ["y", "yes"]:
    print("Agreed.")

elif c.lower() in["n", "N"]:
    print ("Not agreed.")
