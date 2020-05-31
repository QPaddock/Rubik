import moves
import cross
import first_2_layers
from print_cube import print_cube

cube = [["" for i in range(12)] for j in range(9)]

for i in range(0, 9):
    for j in range(0, 12):
        if j > 5 and j < 9 and i < 3:
            cube[i][j] = 'y'
        if i > 2 and i < 6:
            if j < 3:
                cube[i][j] = 'b'
            if j > 2 and j < 6:
                cube[i][j] = 'r'
            if j > 5 and j < 9:
                cube[i][j] = 'g'
            if j > 8 and j < 12:
                cube[i][j] = 'm'
        if j > 5 and j < 9 and i > 5:
            cube[i][j] = 'w'

mix = input("Enter Scramble (U, U', B, B', L, L', F, F', R, R', D, D') : ")

moves.make_moves(mix, cube)

print_cube(cube)

cross.make_cross(cube)

print("Cross made: ")
print_cube(cube)


first_2_layers.do_first_2_layers(cube)

print("First 2 Layers done: ")
print_cube(cube)
