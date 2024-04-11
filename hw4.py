def rep_char(c, n):
    print(c * n)

def draw_line_string(msg):
    line1 = f"Hello, {name},"
    line2 = f"Welcome to seoul"

    nstr = len(line1) if(len(line1) > len(line2)) else len(line2)

    rep_char('-', nstr + 2)
    print(f" {line1:^{nstr}} ")
    print(f" {line2:<{nstr}} ")
    rep_char('-', nstr + 2)


name = input("Input his/her name: ")
draw_line_string(name)


