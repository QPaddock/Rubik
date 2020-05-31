from print_cube import print_cube

temp_cube = [["" for i in range(12)] for j in range(9)]


def make_moves(mix, cube):
    if valid_mix(mix) == False:
        print("Invalid Mix...")
        return

    for twist in mix.split():
        if twist == "R":
            right_turn(cube)
        if twist == "L":
            left_turn(cube)
        if twist == "F":
            front_turn(cube)
        if twist == "B":
            back_turn(cube)
        if twist == "U":
            up_turn(cube)
        if twist == "D":
            down_turn(cube)
        if twist == "R2":
            right_turn(cube)
            right_turn(cube)
        if twist == "L2":
            left_turn(cube)
            left_turn(cube)
        if twist == "F2":
            front_turn(cube)
            front_turn(cube)
        if twist == "B2":
            back_turn(cube)
            back_turn(cube)
        if twist == "U2":
            up_turn(cube)
            up_turn(cube)
        if twist == "D2":
            down_turn(cube)
            down_turn(cube)
        if twist == "R'":
            right_turn(cube)
            right_turn(cube)
            right_turn(cube)
        if twist == "L'":
            left_turn(cube)
            left_turn(cube)
            left_turn(cube)
        if twist == "F'":
            front_turn(cube)
            front_turn(cube)
            front_turn(cube)
        if twist == "B'":
            back_turn(cube)
            back_turn(cube)
            back_turn(cube)
        if twist == "U'":
            up_turn(cube)
            up_turn(cube)
            up_turn(cube)
        if twist == "D'":
            down_turn(cube)
            down_turn(cube)
            down_turn(cube)


def valid_mix(mix):
    for twist in mix.split():
        if (twist != 'R' and twist != "R'" and twist != 'L' and twist != "L'"
                and twist != 'F' and twist != "F'"
                and twist != 'B' and twist != "B'" and twist != 'U'
                and twist != "U'" and twist != 'D' and twist != "D'"
                and twist != "R2" and twist != "L2" and twist != "F2"
                and twist != "B2" and twist != "U2" and twist != "D2"):
            return False

    return True


def right_turn(new_cube):
    temp_cube = [x[:] for x in new_cube]
    new_cube[0][8] = temp_cube[3][8]
    new_cube[1][8] = temp_cube[4][8]
    new_cube[2][8] = temp_cube[5][8]
    new_cube[3][0] = temp_cube[2][8]
    new_cube[3][8] = temp_cube[6][8]
    new_cube[3][9] = temp_cube[5][9]
    new_cube[3][10] = temp_cube[4][9]
    new_cube[3][11] = temp_cube[3][9]
    new_cube[4][0] = temp_cube[1][8]
    new_cube[4][8] = temp_cube[7][8]
    new_cube[4][9] = temp_cube[5][10]
    new_cube[4][11] = temp_cube[3][10]
    new_cube[5][0] = temp_cube[0][8]
    new_cube[5][8] = temp_cube[8][8]
    new_cube[5][9] = temp_cube[5][11]
    new_cube[5][10] = temp_cube[4][11]
    new_cube[5][11] = temp_cube[3][11]
    new_cube[6][8] = temp_cube[5][0]
    new_cube[7][8] = temp_cube[4][0]
    new_cube[8][8] = temp_cube[3][0]


def left_turn(new_cube):
    temp_cube = [x[:] for x in new_cube]
    new_cube[0][6] = temp_cube[5][2]
    new_cube[1][6] = temp_cube[4][2]
    new_cube[2][6] = temp_cube[3][2]
    new_cube[3][2] = temp_cube[8][6]
    new_cube[3][3] = temp_cube[5][3]
    new_cube[3][4] = temp_cube[4][3]
    new_cube[3][5] = temp_cube[3][3]
    new_cube[3][6] = temp_cube[0][6]
    new_cube[4][2] = temp_cube[7][6]
    new_cube[4][3] = temp_cube[5][4]
    new_cube[4][5] = temp_cube[3][4]
    new_cube[4][6] = temp_cube[1][6]
    new_cube[5][2] = temp_cube[6][6]
    new_cube[5][3] = temp_cube[5][5]
    new_cube[5][4] = temp_cube[4][5]
    new_cube[5][5] = temp_cube[3][5]
    new_cube[5][6] = temp_cube[2][6]
    new_cube[6][6] = temp_cube[3][6]
    new_cube[7][6] = temp_cube[4][6]
    new_cube[8][6] = temp_cube[5][6]


def front_turn(new_cube):
    temp_cube = [x[:] for x in new_cube]
    new_cube[2][5] = temp_cube[6][5]
    new_cube[2][6] = temp_cube[5][5]
    new_cube[2][7] = temp_cube[4][5]
    new_cube[2][8] = temp_cube[3][5]
    new_cube[2][9] = temp_cube[2][5]
    new_cube[3][5] = temp_cube[6][6]
    new_cube[3][6] = temp_cube[5][6]
    new_cube[3][7] = temp_cube[4][6]
    new_cube[3][8] = temp_cube[3][6]
    new_cube[3][9] = temp_cube[2][6]
    new_cube[4][5] = temp_cube[6][7]
    new_cube[4][6] = temp_cube[5][7]
    new_cube[4][8] = temp_cube[3][7]
    new_cube[4][9] = temp_cube[2][7]
    new_cube[5][5] = temp_cube[6][8]
    new_cube[5][6] = temp_cube[5][8]
    new_cube[5][7] = temp_cube[4][8]
    new_cube[5][8] = temp_cube[3][8]
    new_cube[5][9] = temp_cube[2][8]
    new_cube[6][5] = temp_cube[6][9]
    new_cube[6][6] = temp_cube[5][9]
    new_cube[6][7] = temp_cube[4][9]
    new_cube[6][8] = temp_cube[3][9]
    new_cube[6][9] = temp_cube[2][9]


def back_turn(new_cube):
    temp_cube = [x[:] for x in new_cube]
    new_cube[0][6] = temp_cube[3][11]
    new_cube[0][7] = temp_cube[4][11]
    new_cube[0][8] = temp_cube[5][11]
    new_cube[3][0] = temp_cube[5][0]
    new_cube[3][1] = temp_cube[4][0]
    new_cube[3][2] = temp_cube[3][0]
    new_cube[3][3] = temp_cube[0][8]
    new_cube[3][11] = temp_cube[8][8]
    new_cube[4][0] = temp_cube[5][1]
    new_cube[4][2] = temp_cube[3][1]
    new_cube[4][3] = temp_cube[0][7]
    new_cube[4][11] = temp_cube[8][7]
    new_cube[5][0] = temp_cube[5][2]
    new_cube[5][1] = temp_cube[4][2]
    new_cube[5][2] = temp_cube[3][2]
    new_cube[5][3] = temp_cube[0][6]
    new_cube[5][11] = temp_cube[8][6]
    new_cube[8][6] = temp_cube[3][3]
    new_cube[8][7] = temp_cube[4][3]
    new_cube[8][8] = temp_cube[5][3]


def up_turn(new_cube):
    temp_cube = [x[:] for x in new_cube]
    new_cube[0][6] = temp_cube[2][6]
    new_cube[0][7] = temp_cube[1][6]
    new_cube[0][8] = temp_cube[0][6]
    new_cube[1][6] = temp_cube[2][7]
    new_cube[1][8] = temp_cube[0][7]
    new_cube[2][6] = temp_cube[2][8]
    new_cube[2][7] = temp_cube[1][8]
    new_cube[2][8] = temp_cube[0][8]
    new_cube[3][0] = temp_cube[3][3]
    new_cube[3][1] = temp_cube[3][4]
    new_cube[3][2] = temp_cube[3][5]
    new_cube[3][3] = temp_cube[3][6]
    new_cube[3][4] = temp_cube[3][7]
    new_cube[3][5] = temp_cube[3][8]
    new_cube[3][6] = temp_cube[3][9]
    new_cube[3][7] = temp_cube[3][10]
    new_cube[3][8] = temp_cube[3][11]
    new_cube[3][9] = temp_cube[3][0]
    new_cube[3][10] = temp_cube[3][1]
    new_cube[3][11] = temp_cube[3][2]


def down_turn(new_cube):
    temp_cube = [x[:] for x in new_cube]
    new_cube[5][0] = temp_cube[5][9]
    new_cube[5][1] = temp_cube[5][10]
    new_cube[5][2] = temp_cube[5][11]
    new_cube[5][3] = temp_cube[5][0]
    new_cube[5][4] = temp_cube[5][1]
    new_cube[5][5] = temp_cube[5][2]
    new_cube[5][6] = temp_cube[5][3]
    new_cube[5][7] = temp_cube[5][4]
    new_cube[5][8] = temp_cube[5][5]
    new_cube[5][9] = temp_cube[5][6]
    new_cube[5][10] = temp_cube[5][7]
    new_cube[5][11] = temp_cube[5][8]
    new_cube[6][6] = temp_cube[8][6]
    new_cube[6][7] = temp_cube[7][6]
    new_cube[6][8] = temp_cube[6][6]
    new_cube[7][6] = temp_cube[8][7]
    new_cube[7][8] = temp_cube[6][7]
    new_cube[8][6] = temp_cube[8][8]
    new_cube[8][7] = temp_cube[7][8]
    new_cube[8][8] = temp_cube[6][8]
