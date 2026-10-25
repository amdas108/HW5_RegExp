import re
from pathlib import Path

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

def rename_files(files_path):
    directory = Path(files_path)
    pattern = r'Mix-(G\d+)_S\d+_L\d+_(R[12])_001\.fastq'
    new_pattern = r'\1_\2.fastq'

    for file in directory.iterdir():
        if re.search(pattern, file.name):
            new_name = re.sub(pattern, new_pattern, file.name)
            print(new_name)

    