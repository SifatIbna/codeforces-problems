# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    t = int(input())
    for i in range(0, t):
        n = int(input())
        k = int(input())
        if n <k :
            print(k-n)
        elif n%2 == k%2 :
            print(0)
        else:
            print(1)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
