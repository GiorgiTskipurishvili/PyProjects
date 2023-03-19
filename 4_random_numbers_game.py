import random
while True:
    comp_numb = random.randint(1,36)
    n = int(input("Guess the number from 1 to 36: "))
    if n == comp_numb:
        print("Congrulation, you guess! ")
        break
    elif n <comp_numb:
        print("Your number is lower!")
    else:
        print("Your number is Higher")
