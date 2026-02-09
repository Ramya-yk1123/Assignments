filename=input("Enter file name:")
try:
    with open(filename,"r") as file:
        data=file.read()
        print("\n Fike content:\n")
        print(data)
except FileNotFoundError:
    print("Oops! That file doesn't exist yet")        