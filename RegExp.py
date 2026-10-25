def rus2salt_translator(text):
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

    return result
