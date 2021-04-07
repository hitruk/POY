import re

# Gloria
PHRASE = str(input("Введите слово начинающиеся на \"gl\": "))

pattern = r"gl"

if re.match(pattern, PHRASE):
    print("Match")
else:
    print("No match")