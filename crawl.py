moves = ["R", "R'", "L", "L'", "F", "F'", "U", "U'", "B",
         "B'", "D", "D'", 'R2', 'D2', 'F2', 'U2', 'L2', 'B2']


def next(temp_solution, s):
    if s != "":
        temp_solution = temp_solution + " " + s
    crawl.append(temp_solution)

    for move in moves:
        if len(temp_solution.split()) != 0:
            if temp_solution.split()[len(temp_solution.split()) - 1][0] == move[0]:
                continue
        if len(temp_solution.split()) > 1:
            if ((temp_solution.split()[len(temp_solution.split()) - 2][0] == "R" and temp_solution.split()[len(temp_solution.split())-1][0] == "L" and move[0] == "R") or
                (temp_solution.split()[len(temp_solution.split())-2][0] == "L" and temp_solution.split()[len(temp_solution.split())-1][0] == "R" and move[0] == "L") or
                (temp_solution.split()[len(temp_solution.split())-2][0] == "F" and temp_solution.split()[len(temp_solution.split())-1][0] == "B" and move[0] == "F") or
                (temp_solution.split()[len(temp_solution.split())-2][0] == "B" and temp_solution.split()[len(temp_solution.split())-1][0] == "F" and move[0] == "B") or
                (temp_solution.split()[len(temp_solution.split())-2][0] == "U" and temp_solution.split()[len(temp_solution.split())-1][0] == "D" and move[0] == "U") or
                    (temp_solution.split()[len(temp_solution.split())-2][0] == "D" and temp_solution.split()[len(temp_solution.split())-1][0] == "U" and move[0] == "D")):
                continue

        if len(temp_solution.split()) > 2:
            break

        next(temp_solution, move)


crawl = []
temp_solution = ""
s = ""

next(temp_solution, s)
