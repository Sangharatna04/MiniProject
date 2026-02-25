import random
target=random.randint(0,100)
while True:
    userchoise=int(input("choose a number:"))
    if(target==userchoise):
        print("congratulation you win")
        break
    elif(userchoise<target):
        print("you choose very small numbe--->>  choose greter numger of ",userchoise)

    else:
        print("you choose very large number choose lower number of ",userchoise)

print("----------WELCOME GAME IS OVER-----------")
print(("That Number is {}").format(target))