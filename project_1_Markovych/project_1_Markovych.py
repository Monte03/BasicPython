from random import randrange

def display_board(board):
    line = "+-------+-------+-------+"
    for row in board:
        print(line)
        print("|       |       |       |")
        print("|   " + "   |   ".join(row) + "   |")
        print("|       |       |       |")
    print(line)


def enter_move(board):
    while True:
        move = input("Введите свой ход (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            row, col = divmod(int(move) - 1, 3)
            if board[row][col] not in ['O', 'X']:
                board[row][col] = 'O'
                break
            else:
                print("Площадь уже занята, попробуйте еще раз.")
        else:
            print("Неверный ход, введите число от 1 до 9.")

def make_list_of_free_fields(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] not in ['O', 'X']]

def victory_for(board, sign):
    win_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    for combination in win_combinations:
        if all(board[row][col] == sign for row, col in combination):
            return True
    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = free_fields[randrange(len(free_fields))]
        board[row][col] = 'X'

def main():
    board = [
        ['1', '2', '3'],
        ['4', 'X', '6'],
        ['7', '8', '9']
    ]
    
    display_board(board)
    
    while True:
        enter_move(board)
        display_board(board)
        if victory_for(board, 'O'):
            print("Поздравляем! Вы выиграли!")
            break
        elif not make_list_of_free_fields(board):
            print("Это ничья!")
            break
        
        print("Ход компьютера:")
        draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print("Компьютер победил!")
            break
        elif not make_list_of_free_fields(board):
            print("Это ничья!")
            break

main()