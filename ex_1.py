import re


def ex_one():
    """
    Функция re.match() есть ли совпадение в начале строки.
    Нет совпадений выводит: None
    """
    pattern = r"spam"

    if re.match(pattern, "spamspamspam"):
        print("Match")
    else:
        print("No match")


def ex_two():
    """
    re.search() поиск набора символов в любом месте строки
    re.findall() возвращает список слов, который совпал в строке
    возвращает список всех подстрок, которые совпадают с искомым набором символов
    """
    pattern = r"spam"

    if re.search(pattern, "eggspamsausagespam"):
        print("Match")
    else:
        print("No match")

    print(re.findall(pattern, "eggspamsausagespam"))  # выводит ['spam', 'spam']


def ex_three():
    """
    group возвращает начальную и конечную строку
    start возвращает начальную позицию первого совпадения, например 4
    end возвращает конечную позицию, например 6
    span возвращает кортеж от начальной до конечной позиции первого совпадения, например (4, 6)
    """

    pattern = r"pam"

    match = re.search(pattern, "eggspamsausage")
    if match:
        print(match.group())
        print(match.start())
        print(match.end())
        print(match.span())


def ex_four():
    """
    sub заменяет все упоминания набора символов в строке на repl
    re.sub(pattern, repl, string, count=0), count сделать указанное количество замен
    """
    str = "My name is David. Hi David."
    pattern = r"David"
    newstr = re.sub(pattern, "Amy", str)
    print(newstr)
    newstr_one = re.sub(pattern, "Amy", str, count=1)  # count сделать указанное количество замен
    print(newstr_one)


def main():
    # ex_one()
    # ex_two()
    ex_three()
    ex_four()


if __name__ == "__main__":
    main()
