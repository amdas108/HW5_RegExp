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

def get_chords(file_path):
    with open(file_path, mode = 'r') as f:
        text = f.read()

    pattern = (
        r'(?<![A-Za-z])'
        r'[A-H](?:#|b)?'
        r'(?:maj|min|m|dim|aug|sus\d*)?'
        r'\d*(?:/[A-H](?:#|b)?)?'
        r'(?![A-Za-z])'
    )

    chords = set(re.findall(pattern, text))
    print(chords)
    
    return chords
