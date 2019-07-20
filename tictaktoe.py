from colorama import init, Fore, Style
init()


def board(flag, sym):
    global c1, c2, c3, c4, c5, c6, c7, c8, c9
    if flag == 1:
        c1 = Fore.RED+Style.BRIGHT+sym+Fore.RESET+Style.RESET_ALL
    elif flag == 2:
        c2 = Fore.RED+Style.BRIGHT+sym+Fore.RESET+Style.RESET_ALL
    elif flag == 3:
        c3 = Fore.RED+Style.BRIGHT+sym+Fore.RESET+Style.RESET_ALL
    elif flag == 4:
        c4 = Fore.RED+Style.BRIGHT+sym+Fore.RESET+Style.RESET_ALL
    elif flag == 5:
        c5 = Fore.RED+Style.BRIGHT+sym+Fore.RESET+Style.RESET_ALL
    elif flag == 6:
        c6 = Fore.RED+Style.BRIGHT+sym+Fore.RESET+Style.RESET_ALL
    elif flag == 7:
        c7 = Fore.RED+Style.BRIGHT+sym+Fore.RESET+Style.RESET_ALL
    elif flag == 8:
        c8 = Fore.RED+Style.BRIGHT+sym+Fore.RESET+Style.RESET_ALL
    elif flag == 9:
        c9 = Fore.RED+Style.BRIGHT+sym+Fore.RESET+Style.RESET_ALL
    print(f"""
                                          |          | 
                                     {c1}    |     {c2}    |    {c3}
                                 _________|__________|__________
                                          |          |
                                     {c4}    |     {c5}    |    {c6}
                                 _________|__________|__________
                                          |          |
                                     {c7}    |     {c8}    |    {c9}
                                          |          |
                                """)


def symbol(char):
    if char.lower() == 'x':
        lt = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
        return lt
    elif char.lower() == 'o':
        lt = ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']
        return lt
    else:
        print("Enter a Valid Choice!")


def check():
    if (c1 == c2 == c3 or c4 == c5 == c6 or c7 == c8 == c9 or c1 == c4 == c7 or c2 == c5 == c8 or c3 == c6 == c9 or
            c1 == c5 == c9 or c3 == c5 == c7):
        return True
    else:
        return False


while True:
    try:
        c1, c2, c3, c4, c5, c6, c7, c8, c9 = '1', '2', '3', '4', '5', '6', '7', '8', '9'
        flag_lst = []
        j = 0
        board_first = True
        win = False
        user_input = input(Fore.CYAN+"Do You Wanna Play Tic Tac Toe?...... (Yes or No)  ")
        if user_input.lower() == "yes":
            user_input = input(Fore.BLUE+"Choose Character for Player 1?....... (X or O)  "+Fore.RESET)
            if user_input.lower() in ['x', 'o']:
                lt = symbol(user_input)
                for i in lt:
                    if board_first:
                        print(f"""
                                              |          | 
                                         {c1}    |     {c2}    |    {c3}
                                     _________|__________|__________
                                              |          |
                                         {c4}    |     {c5}    |    {c6}
                                     _________|__________|__________
                                              |          |
                                         {c7}    |     {c8}    |    {c9}
                                              |          |
                                    """)
                        board_first = False

                    while True:
                        print(Fore.LIGHTMAGENTA_EX + f"Player {i}")
                        flag = int(input(Fore.YELLOW + "Enter A No." + Fore.RESET))
                        if flag not in flag_lst and flag in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                            board(flag, i)
                            flag_lst.append(flag)
                            j += 1
                            break
                        else:
                            print(Fore.RED+"Please Enter a Valid No.")

                    if check() == True:
                        print(f"Congrats Player {i} Wins !")
                        break

                    elif j == 9:
                        print("Match Draw !")
                        break


            else:
                print("Please Choose Between X or O !... ")

        elif user_input.lower() == "no":
            print(Fore.LIGHTYELLOW_EX+"Thank You Playing with us!")
            break

        else:
            print(Fore.RED+"Invalid Choice!")

    except :
        print(Fore.RED+"Something Not Good!")


