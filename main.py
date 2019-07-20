print("Welcome To Mini Games")
print("           Created By Varun Bhardwaj")

while True:
    try:
        print("1. Black Jack\n"
              "2. Guess A No.\n"
              "3. Rock, Paper & Scissors\n"
              "4. Tic Tak Toe\n")
        user_input = int(input("\nPlease Choose A No. From The Given List ....   "))
        if user_input not in [1, 2, 3, 4]:
            raise Exception
    except:
        print("\nPlease Provide With A Valid Argument !")
    else:
        if user_input == 1:
            import black_jack
        elif user_input == 2:
            import guess_no
        elif user_input == 3:
            import rock_paper
        elif user_input == 4:
            import tictaktoe
        break