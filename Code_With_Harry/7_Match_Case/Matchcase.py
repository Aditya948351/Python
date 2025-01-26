x = int(input("Enter a number:  "))
print(x)

match x:
    case 0:    
        print("0")
    case 1:
        print("1")
    case _ if x=5:
        print("Hello")
    case _ if x=9:
        print("World")
