
#  5. Группы

import re

def one():
    """
    group() или group(0) - возвращает все найденные совпадения
    group(n), где n > 0, вернет, n - группу
    """

    pattern = r"a(bc)(de)(f(g)h)i"

    match = re.match(pattern, "abcdefghijklmnop")

    if match:
        print(match.group())
        print(match.group(0))
        print(match.group(1))
        print(match.group(2))
        print(match.groups())


def two():
    """
    Именованные группы (?P<name>...), где name - имя группы, а ... содержание группы
    Незахватывающие группы (?:...), их нельзяполучить по методу группы (group(n))
    """

    pattern = r"(?P<first>abc)(?:def)(ghi)"

    match = re.match(pattern, "abcdefghi")
    if match:
        print(match.group("first"))
        print(match.groups())


def three():
    """
    Метасимвол: | имеет значение "или"
    """

    pattern = r"gr(a|e)y"

    match = re.match(pattern, "gray")
    if match:
        print("Match 1")

    match = re.match(pattern, "grey")
    if match:
        print("Match 2")

    match = re.match(pattern, "griy")
    if match:
        print("Match 3")

def main():
    # one()
    two()
    # three()

if __name__ == "__main__":
    main()