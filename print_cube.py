import colorama


def print_cube(cube):
    s = []
    for i in cube:
        for j in i:
            if j == "y":
                s.append(colorama.Fore.LIGHTYELLOW_EX +
                         'U' + colorama.Fore.RESET + "│")
            elif j == "g":
                s.append(colorama.Fore.GREEN + 'R' + colorama.Fore.RESET + "│")
            elif j == "r":
                s.append(colorama.Fore.RED + 'F' + colorama.Fore.RESET + "│")
            elif j == "w":
                s.append(colorama.Fore.LIGHTWHITE_EX +
                         'D' + colorama.Fore.RESET + "│")
            elif j == "b":
                s.append(colorama.Fore.BLUE + 'L' + colorama.Fore.RESET + "│")
            elif j == "m":
                s.append(colorama.Fore.MAGENTA + 'B' +
                         colorama.Fore.RESET + "│")

    r = '\n            │' + "".join(s[0:3]) + '\n            │' + \
        "".join(s[3:6]) + '\n            │' + "".join(s[6:9]) + '\n│'
    r += "".join(s[18:21]) + "".join(s[9:12]) + "".join(s[12:15]) + "".join(s[15:18]) + '\n│' +\
         "".join(s[30:33]) + "".join(s[21:24]) + "".join(s[24:27]) + "".join(s[27:30]) \
        + '\n│' + "".join(s[42:45]) + "".join(s[33:36]) + "".join(s[36:39]) + \
        "".join(s[39:42]) + '\n'
    r += '            │' + "".join(s[45:48]) + '\n            │' + \
        "".join(s[48:51]) + '\n            │' + "".join(s[51:54]) + '\n'

    colorama.init()
    print(r)
    colorama.deinit()
