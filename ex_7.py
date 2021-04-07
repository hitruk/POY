import re

def one():
    """Извлечение адресов электронной почты"""

    str = "Please contact info@sololearn.com for assistance"
    pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
    # [\w\.]+ соответствует одному и более символу слова, точке или черточке.
    match = re.search(pattern, str)
    if match:
        print(match.group())

def main():
    one()

if __name__ == "__main__":
    main()