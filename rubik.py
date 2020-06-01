from print_cube import print_cube
import moves
import cross
import first_2_layers
import orient_last_layer
import permute_last_layer
from shorten_solution import shorten
from solution_len import solution_len

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

mix = input("Enter Scramble (U, U', B, B', L, L', F, F', R, R', D, D') :\n")

moves.make_moves(mix, cube)

full_solution = ""

print_cube(cube)

full_solution += cross.make_cross(cube) + " "

print("Cross made...")
print_cube(cube)

full_solution += first_2_layers.do_first_2_layers(cube) + " "

print("First 2 Layers done...")
print_cube(cube)

full_solution += orient_last_layer.do_orient_last_layer(cube) + " "

print("Orient Last Layer done...")
print_cube(cube)

full_solution += permute_last_layer.do_permute_last_layer(cube)

print("Permute Last Layer done...")
print_cube(cube)

full_solution = shorten(full_solution)

print("\n\nSolution:\n" + full_solution)
print("\n\nSolution Length:\n", solution_len(full_solution))
