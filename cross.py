import crawl
import moves
from print_cube import print_cube


def make_cross(cube):
    max = 0
    cross_solution = ""
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
        cross_solution = cross_solution + maxi
        moves.make_moves(maxi, cube)
    return cross_solution


def happiness(cube, mix):
    move_score = 0

    if cube[6][7] == "w" and cube[5][7] == "g":
        move_score = move_score + 25

    if cube[7][6] == "w" and cube[5][4] == "r":
        move_score = move_score + 25

    if cube[7][8] == "w" and cube[5][10] == "m":
        move_score = move_score + 25

    if cube[8][7] == "w" and cube[5][1] == "b":
        move_score = move_score + 25

    if cube[4][0] == "w":
        move_score = move_score + 2

    if cube[4][2] == "w":
        move_score = move_score + 2

    if cube[4][3] == "w":
        move_score = move_score + 2

    if cube[4][5] == "w":
        move_score = move_score + 2

    if cube[4][6] == "w":
        move_score = move_score + 2

    if cube[4][8] == "w":
        move_score = move_score + 2

    if cube[4][9] == "w":
        move_score = move_score + 2

    if cube[4][11] == "w":
        move_score = move_score + 2

    if len(mix.split(" ")) == 3:
        move_score = move_score+0.04

    if len(mix.split(" ")) == 2:
        move_score = move_score+0.07

    if len(mix.split(" ")) == 1:
        move_score = move_score+0.09

    for i in mix.split(" "):
        if "2" in i:
            move_score = move_score - 0.01

    return move_score
