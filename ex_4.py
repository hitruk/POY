import re


# Метасимволы: *, +, ?, { и }

def ex_one():
    """
    Метасимвол: * - ноль и более упоминаний
    """
    pattern = r"egg(spam)*"

    if re.match(pattern, "egg"):
        print("Match 1")
    if re.match(pattern, "eggspamspamegg"):
        print("Match 2")
    if re.match(pattern, "spam"):
        print("Match 3")


def ex_two():
    """
    Метасимвол: + - одно и более упоминаний
    """
    pattern = r"g+"

    if re.match(pattern, "g"):
        print("Match 1")
    if re.match(pattern, "gggggggggg"):
        print("Match 2")
    if re.match(pattern, "abc"):
        print("Match 3")


def ex_three():
    """
    Метасимвол: ? - ноль или одно упоминание
    """
    pattern = r"ice(-)?cream"

    if re.match(pattern, "ice-cream"):
        print("Match 1")
    if re.match(pattern, "icecream"):
        print("Match 2")
    if re.match(pattern, "sausages"):
        print("Match 3")
    if re.match(pattern, "ice--ice"):
        print("Match 4")


def ex_four():
    """
    Метасимвол: {} - упоминания объекта поиска между x и y;
    {x,y} упоминание объекта поиска между x и y;
    {0,1} == ?
    """

    pattern = r"9{1,3}$"

    if re.match(pattern, "9"):
        print("Match 1")
    if re.match(pattern, "999"):
        print("Match 2")
    if re.match(pattern, "9999"):
        print("Match 3")


def main():
    # ex_one()
    # ex_two()
    # ex_three()
    ex_four()


if __name__ == "__main__":
    main()
