board = list(range(1,10))

def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-------------")


def play(board):
    player_answer = input(str("Куда поставим " + player_token+"? "))
    try:
        player_answer = int(player_answer)
    except:
        print("Некорректный ввод. Вы уверены, что ввели число?")

    if player_answer >= 1 and player_answer <= 9:
        if (str(board[player_answer-1]) not in "XO"):


            board[player_answer - 1] = player_token
            valid = True
        else:
            print("Эта клеточка уже занята")
    else:
        print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

count = 0


valid = False
while not valid:
    count += 1
    if count % 2 != 0:
        player_token = "X"
    else:
        player_token = "Y"
    draw_board(board)
    play(board)
    valid = check_win(board)

if count == 9:
    print("Конец игры. НИЧЬЯ!")
else:
    print("Конец игры")
    print("выиграл :", (player_token))

