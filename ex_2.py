# Метасимволы

import re


def ex_one():
    """
    .(точка) - означает любой символ, исключая символ новой строки (\n)
    r"dfd" - сырая строка начинается с "r"
    """
    pattern = r"gr.y"
    if re.match(pattern, "grey"):
        print("Match 1")

    if re.match(pattern, "gray"):
        print("Match 2")

    if re.match(pattern, "blue"):
        print("Match 3")

def ex_two():
    """
    ^ - начало строки
    $ - конец строки
    """
    pattern = r"^gr.y$"

    if re.match(pattern, "grey"):
        print("Match 1")

    if re.match(pattern, "gray"):
        print("Match 2")

    if re.match(pattern, "stingray"):
        print("Match 3")

def main():
    ex_one()
    ex_two()


if __name__ == "__main__":
    main()
