# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def check_the_string(s):
    if (s.find('a') + 1) and s.find('b') and s.find('c') and s.find('a') < s.find('b') < s.find('c'):
        if 'a' in s[s.find('c'):] or 'b' in s[s.find('c'):]:
            print('NO')
        elif 'a' in s[s.find('b'):]:
            print('NO')
        else:
            if s.count('a') == s.count('c') or s.count('b') == s.count('c'):
                print('YES')
            else:
                print('NO')
    else:
        print('NO')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = input()
    check_the_string(s)
    # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
