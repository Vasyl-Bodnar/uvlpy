import math
from uvlpy.uvlpy import System

def transpose(lst):
    """Assumes square input"""
    res = lst.copy()
    size = math.floor(math.sqrt(len(lst)))
    for i in range(0, size):
        for j in range(0, i):
            res[i * size + j], res[j * size + i] = lst[j * size + i], lst[i * size + j]
    return res


def draw_board(lst):
    for i in range(0, 3):
        for n in range(0, 3):
            for j in range(0, 3):
                for k in range(0, 3):
                    print(lst[i * 27 + n * 9 + j * 3 + k], end=",")
                print("|||", end="")
            print("")
        print("|" * 27)


def main():
    sys = System(keep_work=False)
    sudoku = sys.make_vars(*([list(range(1, 10))] * 81))
    for i in range(1, 10):
        for j in range(0, 9):
            for k in range(0, 9):
                cell = sudoku[j * 9 + k]
                cell.val_constr(
                    i, *[c != i for c in sudoku[j * 9 : j * 9 + 9] if c != cell]
                )
                cell.val_constr(
                    i,
                    *[
                        c != i
                        for c in transpose(sudoku)[k * 9 : k * 9 + 9]
                        if c != cell
                    ],
                )
                cell.val_constr(
                    i,
                    *[
                        c != i
                        for c in sudoku[
                            (j // 3) * 27 + (k // 3) * 3 : (j // 3) * 27
                            + (k // 3) * 3
                            + 3
                        ]
                        + sudoku[
                            (j // 3) * 27 + 9 + (k // 3) * 3 : (j // 3) * 27
                            + 9
                            + (k // 3) * 3
                            + 3
                        ]
                        + sudoku[
                            (j // 3) * 27 + 18 + (k // 3) * 3 : (j // 3) * 27
                            + 18
                            + (k // 3) * 3
                            + 3
                        ]
                        if c != cell
                    ],
                )
    sys.constr(
        sudoku[0] == 1,
        sudoku[4] == 4,
        sudoku[6] == 5,
        sudoku[10] == 6,
        sudoku[15] == 2,
        sudoku[18] == 9,
        sudoku[21] == 3,
        sudoku[25] == 4,
        sudoku[26] == 6,
        sudoku[28] == 7,
        sudoku[31] == 1,
        sudoku[34] == 9,
        sudoku[35] == 4,
        sudoku[38] == 1,
        sudoku[39] == 2,
        sudoku[52] == 5,
        sudoku[55] == 9,
        sudoku[58] == 2,
        sudoku[61] == 1,
        sudoku[62] == 7,
        sudoku[63] == 3,
        sudoku[68] == 8,
        sudoku[78] == 6,
    )
    sys.constr(*[c.to_constr() for c in sudoku])
    draw_board(sys.execute(*sudoku))


if __name__ == "__main__":
    main()
