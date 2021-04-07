import re

def example_one():

    # Убрать все пробелы в text
    text = "Танкисты                            112"
    pattern = r"(\s+)"
    new_foo = re.sub(pattern, " ", text)
    print(new_foo)
    p = 'ПЕРЕИМЕНОВАНИЕ ДИРЕКТОРИИ'
    print(p.lower())

def main():
    example_one()

if __name__ == "__main__":
    main()