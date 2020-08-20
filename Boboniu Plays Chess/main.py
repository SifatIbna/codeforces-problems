# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def move_column():
    pass


def move_row():
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    val = input()
    inputs = val.split(' ')
    n, m, Sx, Sy = int(inputs[0]), int(inputs[1]), int(inputs[2]), int(inputs[3])
    print(Sx,'',Sy)
    dir = True
    for i in range(0, n):
        if i != Sx-1:
            print(i+1, '', Sy)
    for i in range(0,m):
        if i == Sy-1:
            continue
        if dir:

            for j in reversed(range(0,n)):
                print(j+1, '', i+1)
            dir = False
        else:

            for j in range(0,n):
                print(j+1, '',i+1)
            dir = True
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
