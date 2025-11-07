import random

jackpot= random.randint(1,100)

guess_num =int(input("Enter your guess number:"))

counter =1
while guess_num != jackpot: 

    if guess_num < jackpot:
        print("wrong! please guess higher:")

    else:
        print("wrong! please guess lower:") 

    guess_num =int(input("Enter your guess number:"))
    counter += 1 

else:
    print("corrent guess ")
    print("your attempt is:",counter)
