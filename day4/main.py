"""
You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input).
"""

from dataclasses import dataclass, field
from collections import defaultdict

EXAMPLE = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


@dataclass
class BingoNumber:
    marked: bool = False
    number: int = -1


@dataclass
class BingoBoard:
    numbers: dict[int, BingoNumber] = field(default_factory=dict)
    rows: list[list[BingoNumber]] = field(default_factory=list)
    columns: list[list[BingoNumber]] = field(default_factory=list)
    last_num: int = -1
    won: bool = False

    def winner(self):
        if self.won:
            return self.won
        for row in self.rows:
            if all([num.marked for num in row]):
                self.won = True
                return True
        for col in self.columns:
            if all([num.marked for num in col]):
                self.won = True
                return True
        return False

    def strBoard(self):
        str_rep = "########################\r\n"
        for r in self.rows:
            str_rep += " ".join([str(num.number) for num in r]) + "\r\n"
        str_rep += "\r\n"

        for r in self.rows:
            l = list()
            for num in r:
                if num.marked:
                    l.append("1")
                else:
                    l.append("0")
            str_rep += " ".join(l) + "\r\n"
        return str_rep + "########################\r\n"

    def call(self, number: int):
        if self.won is not True:
            self.last_num = number
            try:
                self.numbers[number].marked = True
                return self.winner()
            except KeyError:
                return False
        else:
            return True

    def score(self):
        """
        The score of the winning board can now be calculated. 
        Start by finding the sum of all unmarked numbers on that board; 
        in this case, the sum is 188. 
        Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.
        """
        sum_of_unmarked = 0
        for v in self.numbers.values():
            if v.marked is False:
                sum_of_unmarked += v.number
        return sum_of_unmarked * self.last_num


def create_nested_lists(num_rows=5) -> list[BingoBoard]:
    return [list() for _ in range(num_rows)]


def create_boards(board_strings):
    boards: list[BingoBoard] = list()

    numbers: dict[int, BingoNumber] = dict()
    rows: list[list[BingoNumber]] = create_nested_lists()
    columns: list[list[BingoNumber]] = create_nested_lists()
    row_idx = 0
    for line in board_strings:
        if line == "":
            boards.append(BingoBoard(numbers, rows, columns))
            numbers: dict[int, BingoNumber] = dict()
            rows: list[list[BingoNumber]] = create_nested_lists()
            columns: list[list[BingoNumber]] = create_nested_lists()
            row_idx = 0
            continue
        for col_idx, str_num in enumerate(line.split()):
            int_num = int(str_num)
            numbers[int_num] = BingoNumber(number=int_num)
            rows[row_idx].append(numbers[int_num])
            columns[col_idx].append(numbers[int_num])

        row_idx += 1
    boards.append(BingoBoard(numbers, rows, columns))
    return boards


def part1():
    #input_list = EXAMPLE.splitlines()
    input_list = list()
    with open("day4/input.txt", "r", encoding="utf-8") as f:
        for l in f.readlines():
            input_list.append(l.strip())

    calls = input_list[0].split(",")

    board_strings = input_list[2:]

    boards = create_boards(board_strings)

    for board in boards:
        print(board.strBoard())

    for str_num in calls:
        int_num = int(str_num)
        for board in boards:
            if board.call(int_num):
                print(board.strBoard())
                print(board.score())

                return None


def part2():
    #input_list = EXAMPLE.splitlines()
    input_list = list()
    with open("day4/input.txt", "r", encoding="utf-8") as f:
        for l in f.readlines():
            input_list.append(l.strip())

    calls = input_list[0].split(",")

    board_strings = input_list[2:]

    boards = create_boards(board_strings)

    # for board in boards:
    #     print(board.strBoard())

    valid_boards = list(boards)

    last_board: BingoBoard = None
    #print(f"Boards: {len(boards)}")
    for str_num in calls:
        int_num = int(str_num)
        print(int_num)
        for board in boards:
            if board not in valid_boards:
                continue
            if board.call(int_num):
                last_board = valid_boards.pop(valid_boards.index(board))
                #print(f"Boards: {len(boards)}")
        if len(valid_boards) == 0:
            break
    print(last_board.strBoard())
    print(last_board.score())


def main():
    part2()


if __name__ == "__main__":
    main()
