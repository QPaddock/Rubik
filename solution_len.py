def solution_len(str):
    count = 0

    for s in str:
        if (s == 'R' or s == 'F' or s == 'L' or s == 'D' or s == 'B' or s == 'U'):
            count += 1

    return count
