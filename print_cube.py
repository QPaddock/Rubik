import colorama


def print_cube(cube):
    s = []
    for i in cube:
        for j in i:
            if j == "w":
                s.append(colorama.Fore.WHITE +
                         'D' + colorama.Fore.RESET + "│")
            elif j == "g":
                s.append(colorama.Fore.GREEN + 'F' + colorama.Fore.RESET + "│")
            elif j == "r":
                s.append(colorama.Fore.RED + 'L' + colorama.Fore.RESET + "│")
            elif j == "y":
                s.append(colorama.Fore.YELLOW +
                         'U' + colorama.Fore.RESET + "│")
            elif j == "b":
                s.append(colorama.Fore.BLUE + 'B' + colorama.Fore.RESET + "│")
            elif j == "m":
                s.append(colorama.Fore.MAGENTA + 'R' +
                         colorama.Fore.RESET + "│")

    r = '\n            │' + "".join(s[0:3]) + '\n            │' + "".join(
        s[3:6]) + '\n            │' + "".join(s[6:9]) + '\n│'
    r += "".join(s[9:12]) + "".join(s[12:15]) + "".join(s[15:18]) + "".join(s[18:21]) + '\n│' +\
         "".join(s[21:24]) + "".join(s[24:27]) + "".join(s[27:30]) + "".join(s[30:33]) \
        + '\n│' + "".join(s[33:36]) + "".join(s[36:39]) + \
        "".join(s[39:42]) + "".join(s[42:45]) + '\n'
    r += '            │' + "".join(s[45:48]) + '\n            │' + "".join(
        s[48:51]) + '\n            │' + "".join(s[51:54]) + '\n'

    colorama.init()
    print(r)
    colorama.deinit()
