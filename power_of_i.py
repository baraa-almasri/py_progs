print("Program is terminated by E.O.F!")
while True:
    power = int(input("Enter the desierd power of i:\t"))
    if power % 4 == 0:
        print("i^",power," = " , "1")
    elif power % 4 == 1:
        print("i^",power," = " , "i")
    elif power % 4 == 2:
        print("i^",power," = " , "-1")
    elif power % 4 == 3:
        print("i^",power," = " , "-i")
