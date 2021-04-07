# Специальные последовательности
import re


def one():
    """
    \17 - Специальные последовательности, где n от 1 до 99
    """
    # ПРИМЕР РАБОТЫ! это работает так
    # pattern = r"(a)(b) \1 \1 \2 \1 \2"
    # (a) == \1
    # (b) == \2
    # ab  # это первый шаг берем (a)(b)
    # (a) == \1, (b) == \2
    # ab \1(a) \1(a) \2(b) \1(a) \2(b) : abaabab

    pattern = r"(.+) \1"

    match = re.match(pattern, "word word")
    if match:
        print("Match 1")

    match = re.match(pattern, "!? !?")
    if match:
        print("Match 2")

    match = re.match(pattern, "abc cde")
    if match:
        print("Match 3")


def two():
    """
    \d - это digits, цифры
    \s - это spaces, пробелы
    \w - это word characters, символы слов,
    в режиме ASCII им соответствуют [0-9], [\n\r\f\v] и [a-zA-Z0-9_]
    в режиме Unicode они соответствуют другим символам.
    \w - соответствует символам с диакритикой.
    \D\S\W - имеют противоположное значение, например: \D - все кроме цифр
    """

    pattern = r"(\D+\d)"

    match = re.match(pattern, "Hi 999!")

    if match:
        print("Match 1")

    match = re.match(pattern, "1, 23, 456!")
    if match:
        print("Match 2")

    match = re.match(pattern, " ! $?")
    if match:
        print("Match 3")

def three():
    """
    \A и \Z - последовательности означают начало и конец строки.
    \b - последовательность соотвестствует пустой строке между ссимводами \w и \W или
    символами \w и началом или концом строки.
    \B - последовательность соответствует пустой строке в любом другом месте.
    Внимание!!!
    \b все не буквенно цифровые символы являются разделителями слов.
    """
    pattern = r"\b(cat)\b"

    match = re.search(pattern, "The cat sat!")
    if match:
        print("Match 1")

    match = re.search(pattern, "We s>cat<tered?")
    if match:
        print("Match 2")

    match = re.search(pattern, "We scattered.")
    if match:
        print("Match 3")

def main():
    # one()
    # two()
    three()


if __name__ == "__main__":
    main()