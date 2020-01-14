n=18
n_of_guesses=9
while(True):
    a=int(input("Try"))
    if a>n:
        print("ans is lesser ")
    elif a==n or n_of_guesses==0:
        break
    else:
        print("ans is greater")
    print("no. of guesses left are", n_of_guesses - 1)
    n_of_guesses=n_of_guesses - 1



if(a==n):
    print("guess ia right")
else:
    print("you ran out of tres")
