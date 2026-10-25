import re

def rus2salt(text):
    pattern = r'[АЕЁИОУЫЭЮЯаеёиоуыэюя]'
    result = ''
    for letter in text:
        if re.match(pattern, letter):
            if letter.isupper():
                result += letter + 'C' + letter
            else:
                result += letter + 'c' + letter
        else:
            result += letter
    print(result)
    return result
