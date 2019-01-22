from random import randrange
cont = 1
while cont == 1:
    print("Roll dice: ", randrange(1,7,1))
    cont = int(input("Continue? 0/1 "))
    while cont != 0 and cont != 1:
        print("Input invalid")
        cont = int(input("Continue? 0/1 "))
