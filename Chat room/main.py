# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def remove_duplicate(s):
    word = ""
    if 'll' in s:
        for ch in s:
            if ch not in word:
                word += ch
        return word, True
    else:
        return word, False


def hello(s):
    hello = ""
    for i in range(0, len(s)):
        if s[i] == 'h' and s[i] not in hello:
            hello += 'h'
            i = s.index('h')
        elif s[i] == 'e' and s[i] not in hello and 'h' in hello:
            hello += 'e'
            i = s.index('e')
        elif s[i] == 'l' and 'h' in hello and 'e' in hello:
            hello += 'l'
        elif s[i] == 'o' and s[i] not in hello and 'h' in hello and 'e' in hello and 'l' in hello:
            hello += 'o'
            i = s.index('o')
        else:
            pass
    # print(hello)
    return hello.count('l') >= 2 and "".join(dict.fromkeys(hello)) == 'helo'


def chat_room(s):
    if 'h' in s:
        if 'e' in s[s.index('h'):]:
            if 'l' in s[s.index('e'):]:
                if 'l' in s[s.index('l')+1:]:
                    if 'o' in s[s.index('l'):]:
                        return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = input()
    if hello(s):
        print('YES')
    else:
        print('NO')
    # print(hello(s))
# if 'hello' in s:
#     print(True)
# print("".join(dict.fromkeys(s)))
# word, index = remove_duplicate(s)
# print(index)
# print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
