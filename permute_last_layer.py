import moves
from print_cube import print_cube

algorithms_for_pll = ["R' F R' B2 R F' R' B2 R2",
                      "R2 B2 R F R' B2 R F' R",
                      "R2 U R2 U D R2 U' R2 U R2 U' D' R2 U R2 U2 R2",
                      "R' U R U' R2 F' U' F U R F R' F' R2",
                      "D' R2 U R' U R' U' R U' R2 U' D R' U R",
                      "R' U' R U D' R2 U R' U R U' R U' R2 D",
                      "R2 U' R U' R U R' U R2 D' U R U' R' D",
                      "R U R' U' D R2 U' R U' R' U R' U R2 D'",
                      "R2 U2 R U2 R2 U2 R2 U2 R U2 R2",
                      "R' U L' U2 R U' R' U2 R L",
                      "R U2 R' U' R U2 L' U R' U' L",
                      "L U' R U2 L' U R' L U' R U2 L' U R'",
                      "R' U L' U2 R U' L R' U L' U2 R U' L",
                      "L U2 L' U2 L F' L' U' L U L F L2",
                      "R' U2 R U2 R' F R U R' U' R' F' R2",
                      "R U R' U' R' F R2 U' R' U' R U R' F'",
                      "R2 U' R' U' R U R U R U' R",
                      "R2 U R U R' U' R' U' R' U R'",
                      "R U2 R' D R U' R U' R U R2 D R' U' R D2",
                      "F R' F R2 U' R' U' R U R' F' R U R' U' F'",
                      "R' U' R2 U R U R' U' R U R U' R U' R'",
                      ""]


def do_permute_last_layer(cube):
    orientation_move = ""
    finishing_moves = ""
    step_done = 0
    full_solution = ''

    for x in range(4):
        temp_cube = [y[:] for y in cube]
        if x == 0:
            orientation_move = ""

        if x == 1:
            orientation_move = 'U'
            moves.make_moves('U', cube)

        if x == 2:
            orientation_move = 'U2'
            moves.make_moves('U', cube)

        if x == 3:
            orientation_move = "U'"
            moves.make_moves('U', cube)

        for algo in algorithms_for_pll:
            temp_cube = [x[:] for x in cube]
            moves.make_moves(algo, temp_cube)
            if temp_cube[3][0] == temp_cube[3][1] == temp_cube[3][2] and \
                    temp_cube[3][3] == temp_cube[3][4] == temp_cube[3][5] and \
                    temp_cube[3][6] == temp_cube[3][7] == temp_cube[3][8] and \
                    temp_cube[3][9] == temp_cube[3][10] == temp_cube[3][11]:
                for turn in range(4):
                    if turn == 0:
                        finishing_moves = ""
                    if turn == 1:
                        finishing_moves = 'U'
                        moves.make_moves('U', temp_cube)

                    if turn == 2:
                        finishing_moves = 'U2'
                        moves.make_moves('U', temp_cube)

                    if turn == 3:
                        finishing_moves = "U'"
                        moves.make_moves('U', temp_cube)

                    if temp_cube[3][0] == 'b':
                        break

                full_solution = orientation_move + " " + algo + " " + finishing_moves
                moves.make_moves(algo + " " + finishing_moves, cube)
                step_done = 1
                break
        if step_done == 1:
            break

    return full_solution
