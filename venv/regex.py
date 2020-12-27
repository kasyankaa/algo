import re

text_1 = "He is slim shady"
pattern_1 = "slim"

text_2 = "Tytsdgyuaigyauywgy"
pattern_2 = "gy"


def re_match(pattern, text):
    return ([(a.start( ), (a.end( ) - 1)) for a in list(re.finditer(pattern, text))])


print(re_match(pattern_1, text_1))
print(re_match(pattern_2, text_2))
