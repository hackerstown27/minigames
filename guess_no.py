from random import randint

num = randint(1, 100)
user_num = [0]
chance = 0
print('''
Procedure : \n
1. You Have To Guess A No. Between 1 to 100\n
2. If You Get The No. Close To The Range Of 10,You Will Get Warmer Message\n 
''')
while True:
    user_num.append(int(input("Enter a No...  ")))
    if user_num[-1] == num:
        print("You Have Guessed Right! ")
        break
    elif abs(user_num[-1] - num) <= 10:
        print("Warm")
        while True:
            chance += 1
            user_num.append(int(input("Enter a No...  ")))
            if user_num[-1] == num:
                print("You Have Guessed Right! in Chances: {} ".format(chance))
                quit()
            elif abs(user_num[-1] - num) < abs(user_num[-2] - num):
                print("Warmer")
            else:
                print("Colder")
    else:
        print("Cold")
    chance += 1