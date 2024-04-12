from curses import wrapper

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 10):
        v = i-10
        try:
            stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))
        except Exception as e:
            print(e)

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)