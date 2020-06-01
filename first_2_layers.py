import crawl
import moves


def do_first_2_layers(cube):
    max = 0
    full_solution = ""
    while(max < 100):
        max = 0
        maxi = ""
        for i in crawl.crawl:
            temp_cube = [x[:] for x in cube]
            moves.make_moves(i, temp_cube)
            hap = happiness(temp_cube, i)
            if hap >= max:
                max = hap
                maxi = i
        full_solution = full_solution+maxi
        moves.make_moves(maxi, cube)
    return full_solution


def happiness(cube, mix):
    move_score = 0
    if ((cube[6][7] == "w" and cube[5][7] == "g") and
        (cube[7][6] == "w" and cube[5][4] == "r") and
        (cube[7][8] == "w" and cube[5][10] == "m")
            and (cube[8][7] == "w" and cube[5][1] == "b")):
        move_score = move_score+60
    if (cube[6][6] == "w" and cube[5][5] == "r" and cube[4][5] == "r" and cube[4][6] == "g" and cube[5][6] == "g"):
        move_score = move_score+10
    if (cube[6][8] == "w" and cube[5][8] == "g" and cube[4][8] == "g" and cube[5][9] == "m" and cube[4][9] == "m"):
        move_score = move_score+10
    if (cube[8][8] == "w" and cube[4][0] == "b" and cube[5][0] == "b" and cube[4][11] == "m" and cube[5][11] == "m"):
        move_score = move_score+10
    if (cube[8][6] == "w" and cube[5][2] == "b" and cube[4][2] == "b" and cube[5][3] == "r" and cube[4][3] == "r"):
        move_score = move_score+10

    if (cube[3][3] == "w"):
        if((cube[0][6] == cube[2][7] and cube[3][2] == cube[3][7]) or
           (cube[0][6] == cube[1][8] and cube[3][2] == cube[3][10])):
            if (cube[6][6] == "w" and cube[5][5] == "r" and cube[4][5] == "r"
                    and cube[4][6] == "g" and cube[5][6] == "g"):
                move_score = move_score+0.01
            else:
                move_score = move_score+0.05
        if(cube[0][6] == cube[1][6] and cube[3][2] == cube[3][4]):
            if (cube[8][8] == "w" and cube[4][0] == "b" and cube[5][0] == "b"
                    and cube[4][11] == "m" and cube[5][11] == "m"):
                move_score = move_score+0.0001
            else:
                move_score = move_score+0.0005
        if ((cube[3][1] == cube[3][2]) and (cube[0][6] == cube[0][7])):
            if cube[0][7] == "b":
                move_score = move_score + 3
            else:
                move_score = move_score + 1
        if (cube[0][6] == cube[3][7] and cube[3][2] == cube[2][7]):
            if cube[3][2] == "b":
                move_score = move_score+3
            else:
                move_score = move_score+1
        if ((cube[0][6] == cube[3][10] and cube[3][2] == cube[1][8]) or
                (cube[0][6] == cube[3][1] and cube[3][2] == cube[0][7])):
            if (cube[6][6] == "w" and cube[5][5] == "r" and cube[4][5] == "r"
                    and cube[4][6] == "g" and cube[5][6] == "g"):
                move_score = move_score+0.01
            else:
                move_score = move_score+0.05
        if (cube[0][6] == cube[3][4] and cube[3][2] == cube[1][6]):
            if (cube[8][8] == "w" and cube[4][0] == "b" and cube[5][0] == "b"
                    and cube[4][11] == "m" and cube[5][11] == "m"):
                move_score = move_score+0.0001
            else:
                move_score = move_score+0.0005

    if (cube[3][0] == "w"):
        if ((cube[0][8] == cube[2][7] and cube[3][11] == cube[3][7]) or
                (cube[0][8] == cube[1][6] and cube[3][11] == cube[3][4])):
            if (cube[8][6] == "w" and cube[5][2] == "b" and cube[4][2] == "b"
                    and cube[5][3] == "r" and cube[4][3] == "r"):
                move_score = move_score + 0.01
            else:
                move_score = move_score + 0.05
        if (cube[0][8] == cube[0][7] and cube[3][11] == cube[3][1]):
            if (cube[6][8] == "w" and cube[5][8] == "g" and cube[4][8] == "g"
                    and cube[5][9] == "m" and cube[4][9] == "m"):
                move_score = move_score + 0.0001
            else:
                move_score = move_score + 0.0005
        if ((cube[0][8] == cube[1][8]) and (cube[3][10] == cube[3][11])):
            if cube[1][8] == "m":
                move_score = move_score + 3
            else:
                move_score = move_score + 1
        if (cube[0][8] == cube[3][4] and cube[3][11] == cube[1][6]):
            if cube[3][11] == "m":
                move_score = move_score + 3
            else:
                move_score = move_score + 1
        if ((cube[0][8] == cube[3][7] and cube[3][11] == cube[2][7]) or
                (cube[0][8] == cube[3][10] and cube[3][11] == cube[1][8])):
            if (cube[8][6] == "w" and cube[5][2] == "b" and cube[4][2] == "b"
                    and cube[5][3] == "r" and cube[4][2] == "r"):
                move_score = move_score + 0.01
            else:
                move_score = move_score + 0.05
        if (cube[0][8] == cube[3][1] and cube[3][11] == cube[0][7]):
            if (cube[6][8] == "w" and cube[5][8] == "g" and cube[4][8] == "g"
                    and cube[5][9] == "m" and cube[4][9] == "m"):
                move_score = move_score + 0.0001
            else:
                move_score = move_score + 0.0005

    if (cube[3][2] == "w"):
        if ((cube[0][6] == cube[2][7] and cube[3][3] == cube[3][7]) or
                (cube[0][6] == cube[1][8] and cube[3][3] == cube[3][10])):
            if (cube[8][8] == "w" and cube[4][0] == "b" and cube[5][0] == "b"
                    and cube[4][11] == "m" and cube[5][11] == "m"):
                move_score = move_score+0.01
            else:
                move_score = move_score+0.05
        if(cube[0][6] == cube[0][7] and cube[3][1] == cube[3][3]):
            if (cube[6][6] == "w" and cube[5][5] == "r" and cube[4][5] == "r"
                    and cube[4][6] == "g" and cube[5][6] == "g"):
                move_score = move_score + 0.0001
            else:
                move_score = move_score + 0.0005
        if ((cube[3][3] == cube[3][4]) and (cube[0][6] == cube[1][6])):
            if cube[1][6] == "r":
                move_score = move_score + 3
            else:
                move_score = move_score + 1
        if (cube[0][6] == cube[3][10] and cube[3][3] == cube[1][8]):
            if cube[3][3] == "r":
                move_score = move_score + 3
            else:
                move_score = move_score + 1
        if ((cube[0][6] == cube[3][7] and cube[3][3] == cube[2][7]) or
                (cube[0][6] == cube[3][4] and cube[3][3] == cube[1][6])):
            if (cube[8][8] == "w" and cube[4][0] == "b" and cube[5][0] == "b"
                    and cube[4][11] == "m" and cube[5][11] == "m"):
                move_score = move_score + 0.01
            else:
                move_score = move_score + 0.05
        if (cube[0][6] == cube[3][1] and cube[3][3] == cube[0][7]):
            if (cube[6][6] == "w" and cube[5][5] == "r" and cube[4][5] == "r"
                    and cube[4][6] == "g" and cube[5][6] == "g"):
                move_score = move_score + 0.0001
            else:
                move_score = move_score + 0.0005

    if (cube[3][5] == "w"):
        if ((cube[2][6] == cube[0][7] and cube[3][6] == cube[3][1]) or
                (cube[2][6] == cube[1][8] and cube[3][6] == cube[3][10])):
            if (cube[8][6] == "w" and cube[5][2] == "b" and cube[4][2] == "b"
                    and cube[5][3] == "r" and cube[4][3] == "r"):
                move_score = move_score+0.01
            else:
                move_score = move_score+0.05
        if (cube[2][6] == cube[1][6] and cube[3][6] == cube[3][4]):
            if (cube[6][8] == "w" and cube[5][8] == "g" and cube[4][8] == "g"
                    and cube[5][9] == "m" and cube[4][9] == "m"):
                move_score = move_score + 0.0001
            else:
                move_score = move_score + 0.0005
        if ((cube[3][6] == cube[3][7]) and (cube[2][6] == cube[2][7])):
            if cube[2][7] == "g":
                move_score = move_score + 3
            else:
                move_score = move_score + 1
        if (cube[2][6] == cube[3][1] and cube[3][6] == cube[0][7]):
            if cube[3][6] == "g":
                move_score = move_score + 3
            else:
                move_score = move_score + 1
        if ((cube[2][6] == cube[3][10] and cube[3][6] == cube[1][8]) or
                (cube[2][6] == cube[3][7] and cube[3][6] == cube[2][7])):
            if (cube[8][6] == "w" and cube[5][2] == "b" and cube[4][2] == "b"
                    and cube[5][3] == "r" and cube[4][2] == "r"):
                move_score = move_score + 0.01
            else:
                move_score = move_score + 0.05
        if (cube[2][6] == cube[3][4] and cube[3][6] == cube[1][6]):
            if (cube[6][8] == "w" and cube[5][8] == "g" and cube[4][8] == "g"
                    and cube[5][9] == "m" and cube[4][9] == "m"):
                move_score = move_score + 0.0001
            else:
                move_score = move_score + 0.0005

    if (cube[3][6] == "w"):
        if ((cube[2][6] == cube[0][7] and cube[3][5] == cube[3][1]) or
                (cube[2][6] == cube[1][8] and cube[3][5] == cube[3][10])):
            if (cube[6][8] == "w" and cube[5][8] == "g" and cube[4][8] == "g"
                    and cube[5][9] == "m" and cube[4][9] == "m"):
                move_score = move_score+0.01
            else:
                move_score = move_score+0.05
        if(cube[2][6] == cube[2][7] and cube[3][5] == cube[3][7]):
            if (cube[8][6] == "w" and cube[5][2] == "b" and cube[4][2] == "b"
                    and cube[5][3] == "r" and cube[4][2] == "r"):
                move_score = move_score + 0.0001
            else:
                move_score = move_score + 0.0005
        if ((cube[3][5] == cube[3][4]) and (cube[2][6] == cube[1][6])):
            if cube[1][6] == "r":
                move_score = move_score + 3
            else:
                move_score = move_score + 1
        if (cube[2][6] == cube[3][10] and cube[3][5] == cube[1][8]):
            if cube[3][5] == "r":
                move_score = move_score + 3
            else:
                move_score = move_score + 1
        if ((cube[2][6] == cube[3][1] and cube[3][5] == cube[0][7]) or
                (cube[2][6] == cube[3][4] and cube[3][5] == cube[1][6])):
            if (cube[6][8] == "w" and cube[5][8] == "g" and cube[4][8] == "g"
                    and cube[5][9] == "m" and cube[4][9] == "m"):
                move_score = move_score + 0.01
            else:
                move_score = move_score + 0.05
        if (cube[2][6] == cube[3][7] and cube[3][5] == cube[2][7]):
            if (cube[8][6] == "w" and cube[5][2] == "b" and cube[4][2] == "b"
                    and cube[5][3] == "r" and cube[4][2] == "r"):
                move_score = move_score + 0.0001
            else:
                move_score = move_score + 0.0005

    if (cube[3][8] == "w"):
        if ((cube[2][8] == cube[0][7] and cube[3][9] == cube[3][1]) or
                (cube[2][8] == cube[1][6] and cube[3][9] == cube[3][4])):
            if (cube[6][6] == "w" and cube[5][5] == "r" and cube[4][5] == "r"
                    and cube[4][6] == "g" and cube[5][6] == "g"):
                move_score = move_score+0.01
            else:
                move_score = move_score+0.05
        if(cube[2][8] == cube[2][7] and cube[3][9] == cube[3][7]):
            if (cube[8][8] == "w" and cube[4][0] == "b" and cube[5][0] == "b"
                    and cube[4][11] == "m" and cube[5][11] == "m"):
                move_score = move_score + 0.0001
            else:
                move_score = move_score + 0.0005
        if ((cube[3][9] == cube[3][10]) and (cube[2][8] == cube[1][8])):
            if cube[1][8] == "m":
                move_score = move_score + 3
            else:
                move_score = move_score + 1
        if (cube[2][8] == cube[3][4] and cube[3][9] == cube[1][6]):
            if cube[3][9] == "m":
                move_score = move_score + 3
            else:
                move_score = move_score + 1
        if ((cube[2][8] == cube[3][1] and cube[3][9] == cube[0][7]) or
                (cube[2][8] == cube[3][10] and cube[3][9] == cube[1][8])):
            if (cube[6][6] == "w" and cube[5][5] == "r" and cube[4][5] == "r"
                    and cube[4][6] == "g" and cube[5][6] == "g"):
                move_score = move_score + 0.01
            else:
                move_score = move_score + 0.05
        if (cube[2][8] == cube[3][7] and cube[3][9] == cube[2][7]):
            if (cube[8][8] == "w" and cube[4][0] == "b" and cube[5][0] == "b"
                    and cube[4][11] == "m" and cube[5][11] == "m"):
                move_score = move_score + 0.0001
            else:
                move_score = move_score + 0.0005

    if (cube[3][9] == "w"):
        if ((cube[2][8] == cube[0][7] and cube[3][8] == cube[3][1]) or
                (cube[2][8] == cube[1][6] and cube[3][8] == cube[3][4])):
            if (cube[8][8] == "w" and cube[4][0] == "b" and cube[5][0] == "b"
                    and cube[4][11] == "m" and cube[5][11] == "m"):
                move_score = move_score+0.01
            else:
                move_score = move_score+0.05
        if(cube[2][8] == cube[1][8] and cube[3][8] == cube[3][10]):
            if (cube[6][6] == "w" and cube[5][5] == "r" and cube[4][5] == "r"
                    and cube[4][6] == "g" and cube[5][6] == "g"):
                move_score = move_score + 0.0001
            else:
                move_score = move_score + 0.0005
        if ((cube[3][8] == cube[3][7]) and (cube[2][7] == cube[2][8])):
            if cube[2][7] == "g":
                move_score = move_score + 3
            else:
                move_score = move_score + 1
        if (cube[2][8] == cube[3][1] and cube[3][8] == cube[0][7]):
            if cube[3][8] == "g":
                move_score = move_score + 3
            else:
                move_score = move_score + 1
        if ((cube[2][8] == cube[3][4] and cube[3][8] == cube[1][6]) or
                (cube[2][8] == cube[3][7] and cube[3][8] == cube[2][7])):
            if (cube[8][8] == "w" and cube[4][0] == "b" and cube[5][0] == "b"
                    and cube[4][11] == "m" and cube[5][11] == "m"):
                move_score = move_score + 0.01
            else:
                move_score = move_score + 0.05
        if (cube[2][8] == cube[3][10] and cube[3][8] == cube[1][8]):
            if (cube[6][6] == "w" and cube[5][5] == "r" and cube[4][5] == "r"
                    and cube[4][6] == "g" and cube[5][6] == "g"):
                move_score = move_score + 0.0001
            else:
                move_score = move_score + 0.0005

    if (cube[3][11] == "w"):
        if ((cube[0][8] == cube[1][6] and cube[3][0] == cube[3][4]) or
                (cube[0][8] == cube[2][7] and cube[3][0] == cube[3][7])):
            if (cube[6][8] == "w" and cube[5][8] == "g" and cube[4][8] == "g"
                    and cube[5][9] == "m" and cube[4][9] == "m"):
                move_score = move_score+0.01
            else:
                move_score = move_score+0.05
        if(cube[0][8] == cube[1][8] and cube[3][0] == cube[3][10]):
            if (cube[8][6] == "w" and cube[5][2] == "b" and cube[4][2] == "b"
                    and cube[5][3] == "r" and cube[4][2] == "r"):
                move_score = move_score + 0.0001
            else:
                move_score = move_score + 0.0005
        if ((cube[3][0] == cube[3][1]) and (cube[0][7] == cube[0][8])):
            if cube[0][7] == "b":
                move_score = move_score + 3
            else:
                move_score = move_score + 1
        if (cube[0][8] == cube[3][7] and cube[3][0] == cube[2][7]):
            if cube[3][0] == "b":
                move_score = move_score + 3
            else:
                move_score = move_score + 1
        if ((cube[0][8] == cube[3][4] and cube[3][0] == cube[1][6]) or
                (cube[0][8] == cube[3][1] and cube[3][0] == cube[0][7])):
            if (cube[6][8] == "w" and cube[5][8] == "g" and cube[4][8] == "g"
                    and cube[5][9] == "m" and cube[4][9] == "m"):
                move_score = move_score + 0.01
            else:
                move_score = move_score + 0.05
        if (cube[0][8] == cube[3][10] and cube[3][0] == cube[1][8]):
            if (cube[8][6] == "w" and cube[5][2] == "b" and cube[4][2] == "b"
                    and cube[5][3] == "r" and cube[4][2] == "r"):
                move_score = move_score + 0.0001
            else:
                move_score = move_score + 0.0005

    # w on top

    if cube[0][6] == "w":
        if (((cube[3][2] == cube[2][7]) and (cube[3][3] == cube[3][7])) or ((cube[3][2] == cube[3][7]) and (cube[3][3] == cube[2][7]))):
            if cube[3][7] == "g":
                move_score = move_score + 0.05
            else:
                move_score = move_score + 0.01
        if (((cube[3][2] == cube[1][8]) and (cube[3][3] == cube[3][10])) or ((cube[3][2] == cube[3][10]) and (cube[3][3] == cube[1][8]))):
            if cube[3][10] == "m":
                move_score = move_score + 0.05
            else:
                move_score = move_score + 0.01
        if ((((cube[3][2] == cube[1][6]) and (cube[3][3] == cube[3][4])) or ((cube[3][2] == cube[3][4]) and (cube[3][3] == cube[1][6]))) or
                (((cube[3][2] == cube[0][7]) and (cube[3][3] == cube[3][1])) or ((cube[3][2] == cube[3][1]) and (cube[3][3] == cube[0][7])))):
            if (cube[8][6] == "w" and cube[5][2] == "b" and cube[4][2] == "b"
                    and cube[5][3] == "r" and cube[4][2] == "r"):
                move_score = move_score+0.0005
            else:
                move_score = move_score+0.0001

    if cube[2][6] == "w":
        if (((cube[3][5] == cube[0][7]) and (cube[3][6] == cube[3][1])) or ((cube[3][5] == cube[3][1]) and (cube[3][6] == cube[0][7]))):
            if cube[3][1] == "b":
                move_score = move_score + 0.05
            else:
                move_score = move_score + 0.01
        if (((cube[3][5] == cube[1][8]) and (cube[3][6] == cube[3][10])) or ((cube[3][5] == cube[3][10]) and (cube[3][6] == cube[1][8]))):
            if cube[3][10] == "m":
                move_score = move_score + 0.05
            else:
                move_score = move_score + 0.01
        if ((((cube[3][5] == cube[1][6]) and (cube[3][6] == cube[3][4])) or ((cube[3][5] == cube[3][4]) and (cube[3][6] == cube[1][6]))) or
                (((cube[3][5] == cube[2][7]) and (cube[3][6] == cube[3][7])) or ((cube[3][5] == cube[3][7]) and (cube[3][6] == cube[2][7])))):
            if (cube[6][6] == "w" and cube[5][5] == "r" and cube[4][5] == "r"
                    and cube[4][6] == "g" and cube[5][6] == "g"):
                move_score = move_score+0.0005
            else:
                move_score = move_score+0.0001

    if cube[2][8] == "w":
        if (((cube[3][8] == cube[0][7]) and (cube[3][9] == cube[3][1])) or ((cube[3][8] == cube[3][1]) and (cube[3][9] == cube[0][7]))):
            if cube[3][1] == "b":
                move_score = move_score+0.05
            else:
                move_score = move_score+0.01
        if (((cube[3][8] == cube[1][6]) and (cube[3][9] == cube[3][4])) or ((cube[3][8] == cube[3][4]) and (cube[3][9] == cube[1][6]))):
            if cube[3][4] == "r":
                move_score = move_score+0.05
            else:
                move_score = move_score+0.01
        if ((((cube[3][8] == cube[1][8]) and (cube[3][9] == cube[3][10])) or ((cube[3][8] == cube[3][10]) and (cube[3][9] == cube[1][8]))) or
                (((cube[3][8] == cube[2][7]) and (cube[3][9] == cube[3][7])) or ((cube[3][8] == cube[3][7]) and (cube[3][9] == cube[2][7])))):
            if (cube[6][8] == "w" and cube[5][8] == "g" and cube[4][8] == "g"
                    and cube[5][9] == "m" and cube[4][9] == "m"):
                move_score = move_score+0.0005
            else:
                move_score = move_score+0.0001

    if cube[0][8] == "w":
        if (((cube[3][0] == cube[1][6]) and (cube[3][11] == cube[3][4])) or ((cube[3][0] == cube[3][4]) and (cube[3][11] == cube[1][6]))):
            if cube[3][4] == "r":
                move_score = move_score+0.05
            else:
                move_score = move_score+0.01
        if (((cube[3][0] == cube[2][7]) and (cube[3][11] == cube[3][7])) or ((cube[3][0] == cube[3][7]) and (cube[3][11] == cube[2][7]))):
            if cube[3][7] == "g":
                move_score = move_score+0.05
            else:
                move_score = move_score+0.01
        if ((((cube[3][0] == cube[1][8]) and (cube[3][11] == cube[3][10])) or ((cube[3][0] == cube[3][10]) and (cube[3][11] == cube[1][8]))) or
                (((cube[3][0] == cube[0][7]) and (cube[3][11] == cube[3][1])) or ((cube[3][0] == cube[3][1]) and (cube[3][11] == cube[0][7])))):
            if (cube[8][8] == "w" and cube[4][0] == "b" and cube[5][0] == "b"
                    and cube[4][11] == "m" and cube[5][11] == "m"):
                move_score = move_score+0.0005
            else:
                move_score = move_score+0.0001

    if len(mix.split(" ")) == 3:
        move_score = move_score+0.00004
    if len(mix.split(" ")) == 2:
        move_score = move_score+0.00007
    if len(mix.split(" ")) == 1:
        move_score = move_score+0.00009
    for i in mix.split(" "):
        if "2" in i:
            move_score = move_score - 0.00001
    return move_score
