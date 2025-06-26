import random

difficulty=input("e, m, h: ")

if difficulty=="e":
    
    l=5
    
    for i in range (l):

        print("You are now in level "+str(i+1))
    
        var=["s"]*5
        var[random.randint(0,4)]="d"

        ch=int(input("Choose your option (1-5): "))

        if var[ch-1]=="d":
               print("Wrong option! Bad Luck!")
               print(var)
               print("Game over")
               quit()
        else:
            print("You are safe")
            print(var)
            print("Moving to next level")

elif difficulty=="m":
    
    l=7
    
    for i in range (l):

        print("You are now in level "+str(i+1))
    
        var=["s"]*5
        var[random.randint(0,4)]="d"
        var[random.randint(0,4)]="d"

        ch=int(input("Choose your option (1-5): "))

        if var[ch-1]=="d":
               print("Wrong option! Bad Luck!")
               print(var)
               print("Game over")
               quit()
        else:
            print("You are safe")
            print(var)
            print("Moving to next level")

elif difficulty=="h":

    l=10
    
    for i in range (l):

        print("You are now in level "+str(i+1))
    
        var=["s"]*5
        var[random.randint(0,4)]="d"
        var[random.randint(0,4)]="d"
        var[random.randint(0,4)]="d"

        ch=int(input("Choose your option (1-5): "))

        if var[ch-1]=="d":
               print("Wrong option! Bad Luck!")
               print(var)
               print("Game over")
               quit()
        else:
            print("You are safe")
            print(var)
            print("Moving to next level")

else:

    print("Invalid difficulty")
    quit()


print("You Won!")
