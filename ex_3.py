import re


# КЛАСС СИМВОЛОВ

def ex_one():
    """
    [] класс символов, поиск символов из набора символов, например:
    """

    pattern = r"[aeiou]"

    if re.search(pattern, "grey"):
        print("Match 1")
    if re.search(pattern, "qwertyuiop"):
        print("Match 2")
    if re.search(pattern, "rhythm myths"):
        print("Match 3")


def ex_two():
    """
    Класс символов, поиск символов в заданном диапазоне
    [a-z] поиск любой строчной буквы
    [G-P] поиск любого символа верхнего регистра от G до P
    [0-9] поиск любой цифры
    [A-Za-z] поиск любой буквы алфавита верхнего или нижнего регистра
    """
    pattern = r"[A-Z][A-Z][0-9]"

    if re.search(pattern, "LS8"):
        print("Match 1")
    if re.search(pattern, "E3"):
        print("Match 2")
    if re.search(pattern, "1ab"):
        print("Match 3")


def ex_three():
    """
    Инвертировать класс символов
    r"[^A-Z]" ищет любой символ, кроме символа класса
    """
    pattern = r"[^A-Z]"

    if re.search(pattern, "this is all quiet"):
        print("Match 1")
    if re.search(pattern, "AbCdEfG123"):
        print("Match 2")
    if re.search(pattern, "THISISALLSHOUTING"):
        print("Match3")
    if re.search(pattern, "ABZ"):
        print("Match4")


def main():
    # ex_one()
    # ex_two()
    ex_three()


if __name__ == "__main__":
    main()
