'''Tegen Hilker Readman - AUCSC-113 Project 2'''


def board_builder():  # defines the board_builder function
    '''takes the input of the 2d list'''
    global board  # makes the board a global variable
    board = eval(input('Enter your 2-d board 9x9): '))

    # takes the user's input
    # as a list and then defines the board variable and eval() makes it that
    # #the inputted value will be whatever element that the user inputted, so
    # in this case it will be a list rather than a long string


def display_board():  # defines the grid function
    '''The current board status will be displayed'''
    '''Also builds the grid'''
    print('  {} {} {} {} {} {} {} {} {}'.format('1', '2', '3', '4', '5', '6',
          '7', '8', '9'))  # this print function has the '1 2 3 4 5 6 7 8 9' above the columns
    # this print function prints the separating string in-between the the numbers and the letter values
    print(' +-~-~-~--~-~-~-~-~+')
    for x in board[0:1]:  # this line and the next one is how I print the top row of the grid, it checks the first inputted 'array'
        # then it prints those values that the for loop found, formatted to look like the example grid
        print('1|{} {} {}|{} {} {}|{} {} {}|'.format(
            x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]), sep='')
    for x in board[1:2]:  # this for loop searches and indexes the second list that is embedded into the big list
        # then it prints those values that the for loop found, formatted to look like the example grid
        print('2|{} {} {}|{} {} {}|{} {} {}|'.format(
            x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]), sep='')
      # print(' |-~-|-~-|')#this print function prints the separating string in-between the the first 2 rows and the other 2 rows
    for x in board[2:3]:  # this checks and indexes the third row for the grid or the 2nd value of the 2-d list
        # then it prints those values that the for loop found, formatted to look like the example grid
        print('3|{} {} {}|{} {} {}|{} {} {}|'.format(
            x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]), sep='')
    print(' +-~-~-~--~-~-~-~-~+')
    for x in board[3:4]:  # this checks and indexes the fourth row for the grid or the 3rd value of the 2-d list
        # then it prints those values that the for loop found, formatted to look like the example grid
        print('4|{} {} {}|{} {} {}|{} {} {}|'.format(
            x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]), sep='')
    for x in board[4:5]:
        print('5|{} {} {}|{} {} {}|{} {} {}|'.format(
            x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]), sep='')
    for x in board[5:6]:
        print('6|{} {} {}|{} {} {}|{} {} {}|'.format(
            x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]), sep='')
    print(' +-~-~-~--~-~-~-~-~+')
    for x in board[6:7]:
        print('7|{} {} {}|{} {} {}|{} {} {}|'.format(
            x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]), sep='')
    for x in board[7:8]:
        print('8|{} {} {}|{} {} {}|{} {} {}|'.format(
            x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]), sep='')
    for x in board[8:9]:
        print('9|{} {} {}|{} {} {}|{} {} {}|'.format(
            x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]), sep='')
    print(' +-~-~-~--~-~-~-~-~+')


# defines the horizontal rule checker function
def horizontal_rule_violated(row, col, value):
    '''This function has three input arguments: row (integer), col
    (integer), and value('A, 'B', 'C', or'D'). When value is entered in the
    board[row-1][col-1], if the horizontal rule is violated, this function
    will return True. Otherwise, it will return False. '''
    invert()
    global hcounter  # makes the variable 'hcounter' a global variable
    hcounter = False  # defines the var the value of False
    # checks if the inputted value that the user inputed is in the same horizontal row
    if value in board[row-1]:
        hcounter = True  # changes the variable's value to True so that the loop will break and then restart
        # this and the next 3 lines of code just prints the user's 'horizontal rule error' message
        print('============================')
        print('Horizontal rule broken')
        print('Do it again!')
        print('==============================================')
    revert()


def vertical_rule_violated(row, col, value):
    '''This function has three input arguments: row (integer), col
    (integer), and value('A', 'B', 'C', or 'D'). when the letter value is
    entered in the board[row-1][col-1], if the vertical rule is violated, it
    will return True. Otherwise,it will return False. '''
    invert()
    global vcounter  # makes the var 'vcounter' global so that it is available in the whole project code
    vcounter = False  # defines the var the value of False
    # counts up the rows in the board and assigns an indexing value to them (there is 4)
    for i in range(len(board)):
        # this one was a bit of a grind to figure out how to do but essentially
        if board[i][col-1] == value:
           # the machine checks if the user's inputted value is in the same column that was input, so it checks each row separately
           # ex:it checks from (0,col-1),(1,col-1)(2,col-1)... then if it is ther1e - the machine will run the lines under it
            vcounter = True  # changes the variable's value to True so that the loop will break and then restart
            print('============================')
            print('Vertical rule broken')
            print('Do it again!')
            print('==============================================')
    revert()


def square_rule_violated(row, col, value):
    '''This function has three input arguments: row (integer), col
    (integer), and value('A', 'B', 'C', or 'D'). When the letter value is
    entered in the board[row-1][col-1], if the square rule is violated, it
    will return True. Otherwise,it will return False. '''
    str(value)
    invert()
    global scounter
    scounter = False
    # the way this function works, rather than checking every single case like I did in the first project
    # I just make the machine reassign the column value to the left column of the mini square
    # if that makes sense, if not just send me an email and I can try to explain it in better detail
    leftCol = [0, 3, 6]
    midCol = [1, 4, 7]
    rightCol = [2, 5, 8]
    topRow = [0, 3, 6]
    midRow = [1, 4, 7]
    bottomRow = [2, 5, 8]
    scol = 0
    if col-1 in leftCol:
        scol = 0
    elif col-1 in midCol:
        scol = col-1
    elif col-1 in rightCol:
        scol = col-2
    if row-1 in topRow:  # if the user's row input is in the top left mini square #
        # the machine will check if the user's input value will be in the 4X4 mini square
        if value in board[row-1][scol-1:scol+2]:
            scounter = True  # redefines the var to True so that the loop will restart
            # this and the next 3 lines of code just prints the user's 'square rule error' message
            print('============================')
            print('Square rule violated.')
            print('Do it again!')
            print('==============================================')

        if value in board[row][scol-1:scol+2]:
           # it's the same deal here but it checks the other row in the 'square'
            scounter = True  # redefines the var to True so that the loop will restart
            # this and the next 3 lines of code just prints the user's 'square rule error' message
            print('============================')
            print('Square rule violated.')
            print('Do it again!')
            print('==============================================')

        if value in board[row+1][scol-1:scol+2]:
           # it's the same deal here but it checks the other row in the 'square'
            scounter = True  # redefines the var to True so that the loop will restart
            # this and the next 3 lines of code just prints the user's 'square rule error' message
            print('============================')
            print('Square rule violated.')
            print('Do it again!')
            print('==============================================')

    elif row-1 in midRow:  # if the user's row input is in the top left mini square but on the bottom half
        # the machine will check if the user's input value will be in the 4X4 mini square
        if value in board[row-2][scol-1:scol+2]:
            # this and the next 3 lines of code just prints the user's 'square rule error' message
            print('============================')
            print('Square rule violated.')
            print('Do it again!')
            print('==============================================')
            scounter = True  # redefines the var to True so that the loop will restart
        if value in board[row-1][scol-1:scol+2]:
           # it's the same deal here but it checks the other row in the 'square'
            # this and the next 3 lines of code just prints the user's 'square rule error' message
            print('============================')
            print('Square rule violated.')
            print('Do it again!')
            print('==============================================')
            scounter = True  # redefines the var to True so that the loop will restart
        if value in board[row][scol-1:scol+2]:
           # it's the same deal here but it checks the other row in the 'square'
            # this and the next 3 lines of code just prints the user's 'square rule error' message
            print('============================')
            print('Square rule violated.')
            print('Do it again!')
            print('==============================================')
            scounter = True  # redefines the var to True so that the loop will restart
    elif row-1 in bottomRow:  # if the user's row input is in the bottom left mini square but on the bottom half
        # the machine will check if the user's input value will be in the 4X4 mini square
        if value in board[row-3][scol-1:scol+2]:
            # this and the next 3 lines of code just prints the user's 'square rule error' message
            print('============================')
            print('Square rule violated.')
            print('Do it again!')
            print('==============================================')
            scounter = True  # defines the var to True so that the loop will restart
        if value in board[row-2][scol-1:scol+2]:
           # it's the same deal here but it checks the other row in the 'square'
            # this and the next 3 lines of code just prints the user's 'square rule error' message
            print('============================')
            print('Square rule violated.')
            print('Do it again!')
            print('==============================================')
            scounter = True  # redefines the var to True so that the loop will restart
        if value in board[row-1][scol-1:scol+2]:
           # it's the same deal here but it checks the other row in the 'square'
            # this and the next 3 lines of code just prints the user's 'square rule error' message
            print('============================')
            print('Square rule violated.')
            print('Do it again!')
            print('==============================================')
            scounter = True  # redefines the var to True so that the loop will restart

    revert()


def alreadyThere(row, col):
    '''checks if the user's input is already there'''
    global alrThe
    alrThe = False
    invert()

    if ' ' != board[(row-1)][(col-1)]:
        print('Your input is wrong! The spot is not empty.\n')
        alrThe = True

    revert()


def highlight(inputed_vals):
    '''hightlight the user's first input'''
    Background_Red = "\033[41m"
    Bold_Cyan = "\033[1;36m"
    original_color = "\033[0m"  # original colour
    Cyan = "\033[0;36m"  # Cyan
    highlightedVal = inputed_vals[0]
    highlightedVal = int(highlightedVal)
    colouredVals = ['\x1b[0;36m1\x1b[0m', '\x1b[0;36m2\x1b[0m', '\x1b[0;36m3\x1b[0m', '\x1b[0;36m4\x1b[0m',
                    '\x1b[0;36m5\x1b[0m', '\x1b[0;36m6\x1b[0m', '\x1b[0;36m7\x1b[0m', '\x1b[0;36m8\x1b[0m', '\x1b[0;36m9\x1b[0m']
    invert()
    for t in range(len(board)):
        for s in range(len(board[t])):
            if highlightedVal == board[t][s]:
                hx = t
                hy = s
                str(highlightedVal)
                board[hx][hy] = Background_Red+Bold_Cyan + \
                    str(highlightedVal)+original_color


def revertHighlight():
    '''reverts the highlight function'''
    highlightedVals = ['\x1b[41m\x1b[1;36m1\x1b[0m', '\x1b[41m\x1b[1;36m2\x1b[0m', '\x1b[41m\x1b[1;36m3\x1b[0m', '\x1b[41m\x1b[1;36m4\x1b[0m',
                       '\x1b[41m\x1b[1;36m5\x1b[0m', '\x1b[41m\x1b[1;36m6\x1b[0m', '\x1b[41m\x1b[1;36m7\x1b[0m', '\x1b[41m\x1b[1;36m8\x1b[0m', '\x1b[41m\x1b[1;36m9\x1b[0m']
    for w in range(len(highlightedVals)):
        for e in range(len(board)):
            for r in range(len(board[e])):
                if board[e][r] == highlightedVals[w]:
                    board[e][r] = w+1
    revert()
# changes the highlighted values to just a regular uncoloured value then reverts the user inputted ones


def invert():
    ''''makes all the values to no colour so that the machine can properly check'''
   # the way this function works it that it cycles through all the possible coloured value's
   # then the board and if it finds one of the coloured values in the board - it switches it to it's uncoloured value
    colouredVals = ['\x1b[0;36m1\x1b[0m', '\x1b[0;36m2\x1b[0m', '\x1b[0;36m3\x1b[0m', '\x1b[0;36m4\x1b[0m',
                    '\x1b[0;36m5\x1b[0m', '\x1b[0;36m6\x1b[0m', '\x1b[0;36m7\x1b[0m', '\x1b[0;36m8\x1b[0m', '\x1b[0;36m9\x1b[0m']
    for i in range(len(colouredVals)):
        for n in range(len(board)):
            for m in range(len(board[n])):
                if board[n][m] == colouredVals[i]:
                    # have to do i+1 other wise every value that the machine assignes will be off by -1
                    board[n][m] = i+1


def revert():
    '''reverts the invert function so that once the machine checks all the values, the user is still displayed their inputed vals'''
    # this one works a bit different, I have a list going in the background that tracks every user input that goes through
    # so then when the function is called, it changes the board to what the respective values from the stored values are
    Cyan = "\033[0;36m"  # Cyan
    original_color = "\033[0m"  # original colour
    for i in range(len(storedInp)):
        a = eval(storedInp[i][0])
        b = eval(storedInp[i][1])
        c = storedInp[i][2]
        board[(a-1)][(b-1)] = Cyan+c+original_color


def all_cells_filled():  # defines the function 'all_cells_filled
    '''If all cells are filled in, return True. Otherwise, return False'''
    emptyval = ' '  # assigned the variable 'emptyval' to just a single space
    # so basically for this function, I have it checking through the board for the empty value or just a single space
    # and when it finds one, it adds one to the counter, so then once there is none there anymore it will redefines the var to True and end the whole game
    global gameprogress  # makes the variable callable in the whole function
    gameprogress = False  # defines the var to False for now
    for x in board:  # indexes the 9 'bigger' lists aka the rows
        # indexes and counts the 81 strings that are inside the list
        if emptyval in x:  # checks if there the empty value in the strings
            gameprogress = gameprogress+1  # if so then it adds one to the tally
        if gameprogress == 0:  # if there is no more 'spaces' or empty values then it will redefine the function to True
            gameprogress = True


def hint():
    '''takes a row and a colum input and displays all possible values there '''
    original_color = "\033[0m"  # original colour
    Bold_Red = "\033[1;31m"
    Background_Cyan = "\033[46m"
    while True:
        hintedNeeded = input(
            'Type the cell\'s row number and column number for which you want a hint: ')
       # basicaly follows along all the input runes

        global hintRow
        global hintCol

        workingVals = []
        if len(hintedNeeded) == 0:
            print('Hey, you didn\'t input anything, please try again.')
            continue
        elif hintedNeeded[0] not in validColInp:
            print('Your input is wrong! The first input value is wrong!\n')
            continue

        elif len(hintedNeeded) != 3:
            print('Your input is wrong! The input length is not 3.\n')
            continue
        elif ' ' not in hintedNeeded[1]:
            print('Your input is wrong! You did not input two separte numbers.\n')
            continue

        elif hintedNeeded[2] not in validColInp:
            print('Your input is wrong! The second input value is wrong!\n')
            continue
        elif ' ' not in hintedNeeded[1]:
            print('Your input is wrong! You did not input two separte numbers.\n')
            continue
        else:
            hintRow = int(hintedNeeded[0])
            hintCol = int(hintedNeeded[2])
            if ' ' != board[(hintRow-1)][(hintCol-1)]:
                print('Your input is wrong! The spot is not empty.\n')
                continue
            else:
                global m
            # so the way this works is there is a for loop that runs through the all valid value inputs
            # and if it violates one of the three rules, it skips that value
            # if not it and the value works, it will append it to the list
            # I had to add the .pop(0) as because 0 was always being used as a value input, easy fix I know but at the time I didn't want to change anything
                for m in range(len(validValInp)+1):
                    hintVerify((hintRow), (hintCol), m)
                    if verified == True:
                        continue
                    else:
                        workingVals.append(m)
                workingVals.pop(0)
                # then it will highlight the valid inputs when it prints
                printedMessage = Bold_Red+Background_Cyan + \
                    str(workingVals)+original_color
                if len(workingVals) == 1:
                    print('Your possible values at {},{} is {}\n'.format(
                        hintRow, hintCol, printedMessage))
                else:
                    print('Your possible values at {},{} are {}\n'.format(
                        hintRow, hintCol, printedMessage))

            break  # ends the hint function and returns to the main sudoku function


def hintVerify(hintRow, hintCol, m):
    '''verifying the hinted values-basically my three main functions from project one tailored to just finding a good hint'''
    invert()
    global verified
    verified = False  # defines the var the value of False
    # checks if the inputted value that the user inputed is in the same horizontal row
    if m in board[hintRow-1]:
        verified = True
    # counts up the rows in the board and assigns an indexing value to them (there is 4)
    for i in range(len(board)):
        if board[i][hintCol-1] == m:
            verified = True
    lCol = [0, 3, 6]
    mCol = [1, 4, 7]
    rCol = [2, 5, 8]
    tRow = [0, 3, 6]
    mRow = [1, 4, 7]
    bRow = [2, 5, 8]
    hcol = 0
    if hintCol-1 in lCol:
        hcol = 0
    elif hintCol-1 in mCol:
        hcol = hintCol-1
    elif hintCol-1 in rCol:
        hcol = hintCol-2
    if hintRow-1 in tRow:  # if the user's row input is in the top left mini square #
        # the machine will check if the user's input value will be in the 4X4 mini square
        if m in board[hintRow-1][hcol-1:hcol+2]:
            verified = True  # redefines the var to True so that the loop will restart
        if m in board[hintRow][hcol-1:hcol+2]:
            # it's the same deal here but it checks the other row in the 'square'
            verified = True  # redefines the var to True so that the loop will restart
        if m in board[hintRow+1][hcol-1:hcol+2]:
            # it's the same deal here but it checks the other row in the 'square'
            verified = True  # redefines the var to True so that the loop will restart

    elif hintRow-1 in mRow:  # if the user's row input is in the top left mini square but on the bottom half
        # the machine will check if the user's input value will be in the 4X4 mini square
        if m in board[hintRow-2][hcol-1:hcol+2]:
            verified = True  # redefines the var to True so that the loop will restart
        if m in board[hintRow-1][hcol-1:hcol+2]:
            # it's the same deal here but it checks the other row in the 'square'

            verified = True  # redefines the var to True so that the loop will restart
        if m in board[hintRow][hcol-1:hcol+2]:
            # it's the same deal here but it checks the other row in the 'square'

            verified = True  # redefines the var to True so that the loop will restart
    elif hintRow-1 in bRow:  # if the user's row input is in the bottom left mini square but on the bottom half
        # the machine will check if the user's input value will be in the 4X4 mini square
        if m in board[hintRow-3][hcol-1:hcol+2]:
            verified = True  # redefines the var to True so that the loop will restart
        if m in board[hintRow-2][hcol-1:hcol+2]:
            # it's the same deal here but it checks the other row in the 'square
            verified = True  # redefines the var to True so that the loop will restart
        if m in board[hintRow-1][hcol-1:hcol+2]:
            # it's the same deal here but it checks the other row in the 'square'
            verified = True  # redefines the var to True so that the loop will restart
    revert()


def sudoku():  # defines the function 'sudoku'
    '''creates an interactive 9x9 sudoku game'''
    Cyan = "\033[0;36m"  # Cyan
    original_color = "\033[0m"  # original colour
    global validRowInp
    global validColInp
    global validValInp
    validRowInp = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'h']
    validColInp = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    validValInp = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    global storedInp
    storedInp = []
    board_builder()  # this calls the function 'grid_builder' which asks the user for their grid that they want to build
    display_board()  # once grid builder is finished running, the machine calls the grid function which uses the user's input and prints the grid

    while True:  # while loop that makes the function normally run forever if nothing out of ordinary happens
        global inputed_vals
        # this asks the user for their inputed choices to fill up the empty spaces
        inputed_vals = input(
            'Type a row number, a column number, and a letter (eg., 1 2 5:) (If you type only one number, all the cells having that number will be highlighted on the board) (If you want a hint,type h): ')
        inputed_vals = str(inputed_vals)
        if len(inputed_vals) == 0:
            print('Hey, you didn\'t input anything, please try again.')
            continue
        elif inputed_vals[0] == 'h':
            '''hint'''
            print('=================================HINT=========================\n')
            hint()
            continue

        elif ' ' in inputed_vals[0]:
            print('Whoops, try again.')
            continue
        
        elif inputed_vals[0] not in validRowInp:
            print('Your input is wrong! The first input value is wrong.\n')
            continue

        elif len(inputed_vals) == 1:
            highlight(inputed_vals)
            display_board()
            revertHighlight()
            continue
        elif len(inputed_vals) == 3:
            ('Print your input is wrong! The input lenght is not 5')
            continue
        elif inputed_vals[2] not in validColInp:
            print('Your input is wrong! The second input value is wrong\n')
            continue

        elif ' ' not in inputed_vals[1]:
            print('Your input is wrong! You did not input three separate numbers.\n')
            continue

        elif ' ' not in inputed_vals[3]:
            print('Your input is wrong! You did not input three separate numbers.\n')
            continue

        elif len(inputed_vals) != 5:
            print('Your input is Wrong! The input length is not 5\n')
            continue
        elif len(inputed_vals) > 5:
            print('Your input is Wrong! The input length is not 5\n')
            continue

        elif inputed_vals[4] not in validValInp:
            print('Your input is wrong! The third input is wrong.\n')
            continue

        else:
            global row  # makes the user's row value callable across the whole program
            global col  # makes the user's column value callable across the whole program
            global value  # makes the user's letter that they inputted callable across the whole program

            # this takes the row value that the user inputted and assigned it the integer value that was inputted
            row = eval(inputed_vals[0])
            # this takes the column value that the user inputted and assigned it the integer value that was inputted
            col = eval(inputed_vals[2])
            # this takes the user's letter input that they want to replace and assigned it to the 'value' variable
            value = int(inputed_vals[4])
            alreadyThere(row, col)
            if alrThe == True:
                continue

            horizontal_rule_violated(row, col, value)
            if hcounter == True:
                continue

            vertical_rule_violated(row, col, value)
            if vcounter == True:
                continue

            square_rule_violated(row, col, value)
            if scounter == True:
                continue

            else:  # the else function is for when the user's input is a valid input

                # have to make the value a string so it is able to change colour
                value = str(value)
                board[(row)-1][(col)-1] = Cyan+value + \
                    original_color  # this replaces
                storedInp.append(inputed_vals.split())
                # the row and column's letter value with the user's input letter,
                # it is -1 for both as in order to make it work as list's indexes start at 0
            display_board()

        # then when all of that is done, the machine will check if the user completed the game yet
            all_cells_filled()
            if gameprogress == True:  # if so, the machine will display the board and then print the congratulations message
                print('==============================================')
                print('You solved this Sudoku! Congratulations!!!')
                print('==============================================')
                break  # then after all said is done the machine ends the program and returns to the terminal


sudoku()
