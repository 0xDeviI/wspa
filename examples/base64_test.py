import base64

operation = input("What do you need (e/d): ").lower()
if (operation == 'e'):
    data = input("Enter data: ")
    try:
        print(base64.b64encode(data.encode()).decode())
    except:
        print("There was an error!")
elif (operation == 'd'):
    data = input("Enter base64-data: ")
    try:
        print(base64.b64decode(data.encode()).decode())
    except:
        print("There was an error!")
else:
    print("Bad operation!")